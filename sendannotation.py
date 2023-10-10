import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from sendAnnotations.annotation_window import send_screenshot
from utils.validation import ScreenshotFolderCreator as sfc

folder = sfc.create_screenshot_folder()


class ScreenShot(QWidget):
    def __init__(self):
        super(ScreenShot, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        self.showMaximized()
        self.isDrawing = False
        self.setCursor(Qt.CrossCursor)
        self.startPoint = QPoint()
        self.endPoint = QPoint()

    def paintEvent(self, event):
        """Paint Event draws the widget.

        :param event: Event.
        :return: None.
        """
        self.bmask = QBitmap(self.geometry().size())
        self.bmask.fill(Qt.black)
        self.mask = self.bmask.copy()
        mask_painter = QPainter(self.mask)
        pen = QPen()
        pen.setStyle(Qt.NoPen)
        mask_painter.setPen(pen)
        brush = QBrush(Qt.white)
        mask_painter.setBrush(brush)
        mask_painter.drawRect(QRect(self.startPoint, self.endPoint))
        self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        """
        Enables the drawing mode.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True

    def mouseMoveEvent(self, event):
        """
        Draws the rect on the widget.

        :param event: Event
        :return: None.
        """
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        global check
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()

            # Use QScreen::grabWindow to capture the primary screen
            screen = QApplication.primaryScreen()
            screenshot = screen.grabWindow(0, self.startPoint.x(), self.startPoint.y(),
                                           self.endPoint.x() - self.startPoint.x(),
                                           self.endPoint.y() - self.startPoint.y())

            temp_path = os.path.expanduser("~/.cache/screenshot/") or folder
            if not os.path.exists(temp_path):
                os.makedirs(temp_path)
            else:
                pass
            s_path = "{}{}.jpg".format(temp_path, "annotation")
            screenshot.save(s_path, 'JPG')
            saved_image = QPixmap(temp_path)
            self.resize(saved_image.width(), saved_image.height())
            self.close()
            send_screenshot(saved_image).show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = ScreenShot()
    tool.show()
    sys.exit(app.exec_())
