from PyQt5.QtWidgets import QApplication, QMainWindow,  QSlider, QVBoxLayout, QLabel, QMessageBox, QWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from view.AppPVC_view_ui import PVC_view
from PyQt5.QtWidgets import QDesktopWidget
from view.floatingWidget import FloatingWidget
import sys

from view.slider_window import SliderWindow


class AppPVCViewMain(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller
        self.view = PVC_view()
        self.view.setupUi(self)

        screen = QDesktopWidget().screenGeometry()
        width, height = screen.width(), screen.height()
        x = (width - self.width()) / 2
        y = (height - self.height()) / 2
        self.move(x, y)
        # screen = QDesktopWidget().screenGeometry()
        # width, height = screen.width(), screen.height()
        # x = (width - self.width()) / 2
        # y = (height - self.height()) / 2
        # self.move(x, y)

        self.view.actionOpen.triggered.connect(self.controller.onOpen)
        self.view.actionSave_As.triggered.connect(
            lambda: self.controller.onSaveAs(self.view.label_2))
        self.view.actionExit.triggered.connect(self.controller.onExit)

        self.view.actionAverage.triggered.connect(
            lambda: self.controller.onImageProces("average"))
        self.view.actionLuminance.triggered.connect(
            lambda: self.controller.onImageProces("luminance"))
        self.view.actionLightness.triggered.connect(
            lambda: self.controller.onImageProces("lightness"))
        self.view.actionInvers.triggered.connect(
            lambda: self.controller.onImageProces("invers"))

        self.view.actionContrast.triggered.connect(
            lambda: self.sliderWindow("contrast"))

        self.view.actionBrightness.triggered.connect(
            lambda: self.sliderWindow("brightness"))

        self.view.actionHistogram_Equalization.triggered.connect(
            self.controller.imageHistogram)

        self.view.actionVertikal.triggered.connect(
            self.controller.onFlipVertical)
        self.view.actionHorizontal.triggered.connect(
            self.controller.onFlipHorizontal)

        # self.view.actionAritmatika.triggered.connect(
        #     self.controller.onAritmatikaPage)
        self.view.actionAritmatika.triggered.connect(
            self.show_middle_label)

        self.model.image_result_changed.connect(self.on_image_result)
        self.model.image_path_changed.connect(self.on_image_change)

        self.view.label_3.mousePressEvent = self.lable3Open


    def lable3Open(self, event):
        if event.button() == Qt.LeftButton:
            self.controller.onOpen()
   

    def sliderWindow(self, route):
        sliderW = SliderWindow(self)
        sliderW.show()
        sliderW.button.clicked.connect(
            lambda: self.controller.brightnessRoute(route, sliderW.slider.value()))

    def show_middle_label(self):
        self.resize(1425, 518)
        x_window = (QtWidgets.QDesktopWidget().width() - self.width()) / 2
        y_window = (QtWidgets.QDesktopWidget().height() - self.height()) / 2
        self.move(x_window, y_window)
        self.view.label_2.setGeometry(950, 20, 451, 441)
        self.view.label_3.show()

    @pyqtSlot(str)
    def on_image_change(self, value):
        pixmap = QPixmap(value)
        self.view.label.setPixmap(pixmap)

    @pyqtSlot(str)
    def on_image_change2(self, value):
        pixmap = QPixmap(value)
        self.view.label_3.setPixmap(pixmap)

    @pyqtSlot(QPixmap)
    def on_image_result(self, value):
        self.view.label_2.setPixmap(value)
