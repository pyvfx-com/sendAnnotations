import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtGui import QCursor, QPixmap, Qt
from PySide2.QtCore import QRect
from PySide2.QtWidgets import QApplication, QColorDialog
from widgets.sendAnnotationUI import Ui_Form
from utils.drawingWidget import DrawingWidget
from utils.sendEmail import sendEmail as seml
from utils.user_db import htmldigger_database as db
from icons import pixmap_rc


class send_screenshot(Ui_Form, QWidget):
    def __init__(self, file_path=None):
        """InIt method for sent_annotation tool class.
            :param Str image_path: Image path.
        """
        super(send_screenshot, self).__init__()
        self.screen_grab = file_path or self.check_path()
        self.close_button = None
        self.dialog = None
        self.oc_panel = None
        self.label_active = None
        self.color_dialog = None
        self.text_widget = None
        self.text_label_status = None
        self.text_label = None
        self.setupUi(self)
        self.usrs = db.name_list()
        self.setWindowTitle(f"Show: dev Quick annotation send v1.7.38 ({os.getenv('USER')})")
        pixmap = QPixmap(self.screen_grab)
        self.image_board = DrawingWidget()
        self.verticalLayout_drawing.addWidget(self.image_board)
        self.verticalLayout_drawing.setContentsMargins(0, 0, 0, 0)
        self.pen.clicked.connect(lambda: self.image_board.change_mode(eraser=False))
        self.eresar.clicked.connect(lambda: self.image_board.change_mode(eraser=True))
        self.text.clicked.connect(self.launch_text_box)
        self.color.clicked.connect(self.open_color_panel)

        self.uname.currentIndexChanged.connect(self.get_receiver)
        self.send.clicked.connect(
            lambda: self.save_image(receiver=self.get_receiver(), sender=self.sender_email()))
        self.brush_size_slider.setValue(self.image_board.pen_size)
        self.brush_size_slider.valueChanged.connect(self.set_pen_size)
        self.all_users()
        self.w_size = int(pixmap.width())
        self.h_size = int(pixmap.height())
        self.label.setPixmap(pixmap)
        self.label.resize(self.w_size, self.h_size)
        self.resize(pixmap.size())
        self.setMaximumSize(pixmap.size())
        self.setMinimumSize(pixmap.size())

    def open_color_panel(self):
        """Opens color panel

        :return: None.
        """
        color_dialog = QColorDialog.getColor()
        if color_dialog.isValid():
            self.image_board.set_pen_color(color_dialog)
            self.set_button_color(color_dialog.name())
        else:
            pass

    def check_path(self):
        screenshot_path = os.path.expanduser("~/.cache/screenshot/")
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)

        fullpath = os.path.join(
            screenshot_path,
            os.listdir(os.path.expanduser("~/.cache/screenshot/"))[0]
        )
        return fullpath

    def set_button_color(self, hexValue):
        """Sets color for picker button.

        :param Str hexValue: Hexa color value.
        :return: None.
        """
        style_sheet = "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," \
                      "stop: 0 {0}, stop: 1 #dadbde);" \
                      "\nborder: 1px solid #565A6C;" \
                      "\nborder-radius: 14px;".format(hexValue)
        self.color.setStyleSheet(style_sheet)

    def set_pen_size(self):
        """Sets pen size.

        :return: None.
        """
        pen_size = self.brush_size_slider.value()
        self.image_board.set_pen_size(pen_size)

    # Text Setups from here.
    def launch_text_box(self):
        """Opens text box.

        :return: None.
        """
        if not self.text_label:
            self.text_label = QLabel(self)
            self.text_label.show()
            self.text_label_status = True
            self.font_dialog()

    def font_dialog(self):
        """Opens font dialog box.

        :return: None.
        """
        self.dialog = QDialog()
        self.dialog.setWindowTitle('Annotation message.')
        self.text_widget = QTextEdit()
        self.close_button = QPushButton("close")
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_widget)
        text_layout.addWidget(self.close_button)
        self.dialog.setLayout(text_layout)
        self.text_widget.textChanged.connect(self.add_text_label)
        self.dialog.exec_()
        self.close_button.clicked.connect(self.dialog.close())

    def add_text_label(self):
        """Adds text label on image label.

        :return: None.
        """
        label_text = self.text_widget.toPlainText()
        self.text_label.setText(label_text)
        self.text_label.adjustSize()

    def set_font_label(self):
        """Sets font style.

        :return: None.
        """
        ok, font = QFontDialog.getFont()
        if ok:
            self.text_label.setFont(font)
            self.text_label.adjustSize()

    def enterEvent(self, event):
        """Changes cursor when mouse enters in text label.

        :param event: Event.
        :return: None.
        """
        try:
            self.text_label.setCursor(QCursor(Qt.OpenHandCursor))
        except AttributeError:
            pass

    def mousePressEvent(self, event):
        """Sets cursor when mouse clicks on text label.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton and self.text_label_status:
            self.label_active = True
            self.text_label.setCursor(QCursor(Qt.ClosedHandCursor))
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Moves text label as per mouse movement.

        :param event: Event.
        :return: None.
        """
        if self.label_active and self.text_label_status:
            self.text_label.move(event.pos())
        else:
            super().mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Reverts the cursor type when mouse release.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton and self.text_label_status:
            self.text_label.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseDoubleClickEvent(self, event):
        """Opens the dialog box when double-clicks on text label.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton and self.label_active:
            self.font_dialog()
        else:
            super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event):
        """Deletes the text label "Z" when key pressed.

        :param event: Event.
        :return: None.
        """
        if event.key() == Qt.Key_Delete:
            self.text_label.close()
            self.text_label = None
        else:
            super().keyPressEvent(event)

    def all_users(self):
        """Fetch all users (Global)
            List of global users.
        :return: None
        """
        all_user = list()
        all_user.insert(0, " ")
        for usr in self.usrs:
            all_user.append("{}".format(usr))
        self.uname.addItems(all_user)

    def get_receiver(self):
        text = self.uname.currentText()
        user_data = db.get_data_by_name(text)
        if user_data:
            return user_data['email']

    @staticmethod
    def sender_email():
        emailid = "htmldigger@gmail.com"
        return emailid

    def save_image(self, receiver=None, sender=None):
        """Saves image draw.
        :return: None.
        """
        send = sender
        rece = receiver
        crop_rect = QRect(0, 0, self.w_size, self.h_size)
        pix = self.grab(self.frame_drawing.geometry())
        cropped_image = pix.copy(crop_rect)
        cropped_image.save(self.screen_grab, quality=-1)
        seml(
            Annotation=self.screen_grab,
            Sender=send,
            Receiver=rece
        )
        self.close()


if __name__ == '__main__':
    """It will bring last window grab.
    """
    app = QApplication(sys.argv)
    widgets = send_screenshot()
    widgets.show()
    sys.exit(app.exec_())
