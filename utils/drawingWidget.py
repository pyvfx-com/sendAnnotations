from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class DrawingWidget(QWidget):
    def __init__(self):
        """
        Init method.
        """
        super(DrawingWidget, self).__init__()
        self.drawing = None
        self.label = QLabel(self)
        self.image = QPixmap(1920, 1920)
        self.image.fill(Qt.transparent)
        self.label.setPixmap(self.image)
        self.label.resize(self.image.width(), self.image.height())
        self.setCursor(QCursor(Qt.CrossCursor))

        self.paint_image = QPixmap(self.image.size())
        self.paint_image.fill(Qt.transparent)
        self.last_point = None
        self.pen_color = "#FF0000"
        self.pen_size = 3
        self.eraser = False

        self.paint_label = QLabel(self)
        self.paint_label.setGeometry(self.label.geometry())

    def set_image_label(self, image_path):
        """
        Sets image in image label.

        :param Str image_path: Path of the image.
        :return: None.
        """
        self.image = image_path
        self.paint_image = QPixmap(self.image.size())
        self.paint_image.fill(Qt.transparent)
        self.label.setPixmap(self.image)
        self.label.resize(self.image.width(), self.image.height())
        self.paint_label.setPixmap(self.paint_image)
        self.paint_label.setGeometry(self.label.rect())
        self.setMinimumSize(self.image.size())
        self.update()

    def set_pen_color(self, color):
        """
        Sets the pen color.

        :param Str color: Color value in rgb.
        :return: None.
        """
        self.pen_color = color

    def set_pen_size(self, size):
        """
        Sets pen size.

        :param Int size: Size of pen.
        :return: None.
        """
        self.pen_size = size

    def mousePressEvent(self, event):
        """
        Enables drawing mode.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton:
            self.last_point = self.label.mapFromParent(event.pos())
            self.drawing = True
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Draws and Erases the paint strokes on image.

        :param event: Event.
        :return: None.
        """
        if self.drawing:
            end_point = self.label.mapFromParent(event.pos())
            painter = QPainter(self.paint_image)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.setPen(
                QPen(
                    QColor(self.pen_color),
                    self.pen_size,
                    Qt.SolidLine,
                    Qt.RoundCap,
                    Qt.RoundJoin
                )
            )
            if self.eraser:
                rect = QRect(QPoint(), self.pen_size * QSize())
                rect.moveCenter(event.pos())
                painter.save()
                painter.setCompositionMode(QPainter.CompositionMode_Clear)
                painter.eraseRect(rect)
                painter.restore()
            else:
                line = QLine(self.last_point, end_point)
                painter.drawLine(line)
            self.last_point = end_point
            self.update()

    def mouseReleaseEvent(self, event):
        """
        Disables the drawing mode.

        :param event: Event.
        :return: None.
        """
        if event.button() == Qt.LeftButton:
            self.last_point = None
            self.drawing = False
        else:
            super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        """
        update the pixmap label.

        :param event: Event.
        :return: None.
        """
        self.paint_label.setPixmap(self.paint_image)

    def change_mode(self, eraser):
        """
        Changes the cursor as per mode.

        :param Bool eraser: status of eraser
        :return: None.
        """
        self.eraser = eraser
        if self.eraser:
            pixmap = QPixmap(QSize(1, 1) * self.pen_size)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setPen(QPen(Qt.black, 2))
            painter.setBrush(QBrush(Qt.DiagCrossPattern))
            painter.drawRect(pixmap.rect())
            painter.end()
            cursor = QCursor(pixmap)
            self.setCursor(cursor)
        else:
            self.setCursor(QCursor(Qt.CrossCursor))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tool = DrawingWidget()
    tool.show()
    sys.exit(app.exec_())
