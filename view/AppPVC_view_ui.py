from PyQt5 import QtCore, QtGui, QtWidgets

class PVC_view(object):

    def setupUi(self, Project1):

        Project1.setObjectName("Project1")

        Project1.resize(944, 518)

        self.centralwidget = QtWidgets.QWidget(Project1)

        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(20, 20, 451, 441))

        self.label.setFrameShape(QtWidgets.QFrame.Box)

        self.label.setText("")

        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)

        self.label_2.setGeometry(QtCore.QRect(480, 20, 451, 441))

        self.label_2.setFrameShape(QtWidgets.QFrame.Box)

        self.label_2.setText("")

        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 20, 451, 441))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("Click to pick image")
        self.label_3.setObjectName("label_3")
        self.label_3.hide()

        Project1.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Project1)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 26))

        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)

        self.menuFile.setObjectName("menuFile")

        self.menuView = QtWidgets.QMenu(self.menubar)

        self.menuView.setObjectName("menuView")

        self.menuHistogram = QtWidgets.QMenu(self.menuView)

        self.menuHistogram.setObjectName("menuHistogram")

        self.menuColors = QtWidgets.QMenu(self.menubar)

        self.menuColors.setObjectName("menuColors")

        self.menuRGB = QtWidgets.QMenu(self.menuColors)

        self.menuRGB.setObjectName("menuRGB")

        self.menuRGB_to_Graysclae = QtWidgets.QMenu(self.menuColors)

        self.menuRGB_to_Graysclae.setObjectName("menuRGB_to_Graysclae")

        self.menuBrightness = QtWidgets.QMenu(self.menuColors)

        self.menuBrightness.setObjectName("menuBrightness")

        self.menuBit_Depth = QtWidgets.QMenu(self.menuColors)

        self.menuBit_Depth.setObjectName("menuBit_Depth")

        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)

        self.menuImage_Processing.setObjectName("menuImage_Processing")

        self.menuAritmetical_Operation = QtWidgets.QMenu(self.menubar)

        self.menuAritmetical_Operation.setObjectName(

        "menuAritmetical_Operation")

        self.menuFilter = QtWidgets.QMenu(self.menubar)

        self.menuFilter.setObjectName("menuFilter")

        self.menuEdge_Detection = QtWidgets.QMenu(self.menuFilter)

        self.menuEdge_Detection.setObjectName("menuEdge_Detection")

        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)

        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")

        self.menuEdge_Detection_2 = QtWidgets.QMenu(self.menubar)

        self.menuEdge_Detection_2.setObjectName("menuEdge_Detection_2")

        self.menuMorfologi = QtWidgets.QMenu(self.menubar)

        self.menuMorfologi.setObjectName("menuMorfologi")

        self.menuErosion = QtWidgets.QMenu(self.menuMorfologi)

        self.menuErosion.setObjectName("menuErosion")

        self.menuDilation = QtWidgets.QMenu(self.menuMorfologi)

        self.menuDilation.setObjectName("menuDilation")

        self.menuClosing = QtWidgets.QMenu(self.menuMorfologi)

        self.menuClosing.setObjectName("menuClosing")

        self.menuOpening = QtWidgets.QMenu(self.menuMorfologi)

        self.menuOpening.setObjectName("menuOpening")

        self.menuGeometri = QtWidgets.QMenu(self.menubar)

        self.menuGeometri.setObjectName("menuGeometri")

        self.menuFlip = QtWidgets.QMenu(self.menuGeometri)

        Project1.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Project1)

        self.statusbar.setObjectName("statusbar")

        Project1.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(Project1)

        self.actionOpen.setObjectName("actionOpen")

        self.action_save = QtWidgets.QAction(Project1)

        self.action_save.setObjectName("actionSave")

        self.actionSave_As = QtWidgets.QAction(Project1)

        self.actionSave_As.setObjectName("actionSave_As")

        self.actionExit = QtWidgets.QAction(Project1)

        self.actionExit.setObjectName("actionExit")

        self.actionInput = QtWidgets.QAction(Project1)

        self.actionInput.setObjectName("actionInput")

        self.actionOutput = QtWidgets.QAction(Project1)

        self.actionOutput.setObjectName("actionOutput")

        self.actionInput_Output = QtWidgets.QAction(Project1)

        self.actionInput_Output.setObjectName("actionInput_Output")

        self.actionBrightness_Contrast = QtWidgets.QAction(Project1)

        self.actionBrightness_Contrast.setObjectName(

        "actionBrightness_Contrast")

        self.actionInvers = QtWidgets.QAction(Project1)

        self.actionInvers.setObjectName("actionInvers")

        self.actionLog_Brightness = QtWidgets.QAction(Project1)

        self.actionLog_Brightness.setObjectName("actionLog_Brightness")

        self.actionGamma_Correction = QtWidgets.QAction(Project1)

        self.actionGamma_Correction.setObjectName("actionGamma_Correction")

        self.actionKuning = QtWidgets.QAction(Project1)

        self.actionKuning.setObjectName("actionKuning")

        self.actionOrange = QtWidgets.QAction(Project1)

        self.actionOrange.setObjectName("actionOrange")

        self.actionCyan = QtWidgets.QAction(Project1)

        self.actionCyan.setObjectName("actionCyan")

        self.actionPurple = QtWidgets.QAction(Project1)

        self.actionPurple.setObjectName("actionPurple")

        self.actionGrey = QtWidgets.QAction(Project1)

        self.actionGrey.setObjectName("actionGrey")

        self.actionCoklat = QtWidgets.QAction(Project1)

        self.actionCoklat.setObjectName("actionCoklat")

        self.actionMerah = QtWidgets.QAction(Project1)

        self.actionMerah.setObjectName("actionMerah")

        self.actionAverage = QtWidgets.QAction(Project1)

        self.actionAverage.setObjectName("actionAverage")

        self.actionLightness = QtWidgets.QAction(Project1)

        self.actionLightness.setObjectName("actionLightness")

        self.actionLuminance = QtWidgets.QAction(Project1)

        self.actionLuminance.setObjectName("actionLuminance")

        self.actionContrast = QtWidgets.QAction(Project1)

        self.actionContrast.setObjectName("actionContrast")
        self.actionBrightness = QtWidgets.QAction(Project1)

        self.actionBrightness.setObjectName("actionBrightness")

        self.action1_bit = QtWidgets.QAction(Project1)

        self.action1_bit.setObjectName("action1_bit")

        self.action2_bit = QtWidgets.QAction(Project1)

        self.action2_bit.setObjectName("action2_bit")

        self.action2_bit_2 = QtWidgets.QAction(Project1)

        self.action2_bit_2.setObjectName("action2_bit_2")

        self.action4_bit = QtWidgets.QAction(Project1)

        self.action4_bit.setObjectName("action4_bit")

        self.action5_bit = QtWidgets.QAction(Project1)

        self.action5_bit.setObjectName("action5_bit")

        self.action6_bit = QtWidgets.QAction(Project1)

        self.action6_bit.setObjectName("action6_bit")

        self.action7_bit = QtWidgets.QAction(Project1)

        self.action7_bit.setObjectName("action7_bit")

        self.actionHistogram_Equalization = QtWidgets.QAction(Project1)

        self.actionHistogram_Equalization.setObjectName(

        "actionHistogram_Equalization")

        self.actionFuzzy_HE_RGB = QtWidgets.QAction(Project1)

        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")

        self.actionFuzzy_Grayscale = QtWidgets.QAction(Project1)

        self.actionFuzzy_Grayscale.setObjectName("actionFuzzy_Grayscale")

        self.actionIDENTITY = QtWidgets.QAction(Project1)

        self.actionIDENTITY.setObjectName("actionIDENTITY")

        self.actionSharpen = QtWidgets.QAction(Project1)

        self.actionSharpen.setObjectName("actionSharpen")

        self.actionUnsharp_Masking = QtWidgets.QAction(Project1)

        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")

        self.actionAerage_Filter = QtWidgets.QAction(Project1)

        self.actionAerage_Filter.setObjectName("actionAerage_Filter")

        self.actionLow_Pass_Filter = QtWidgets.QAction(Project1)

        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")

        self.actionHigh_Pass_Filter = QtWidgets.QAction(Project1)

        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")

        self.actionBandstop_Filter = QtWidgets.QAction(Project1)

        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")

        self.actionEdge_Detection_1 = QtWidgets.QAction(Project1)

        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")

        self.actionEdge_Detection_2 = QtWidgets.QAction(Project1)

        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")

        self.actionEdge_Detection_3 = QtWidgets.QAction(Project1)

        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")

        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(Project1)

        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")

        self.actionGaussian_Blur_5x5 = QtWidgets.QAction(Project1)

        self.actionGaussian_Blur_5x5.setObjectName("actionGaussian_Blur_5x5")

        self.actionPrewitt = QtWidgets.QAction(Project1)

        self.actionPrewitt.setObjectName("actionPrewitt")

        self.actionSbbel = QtWidgets.QAction(Project1)

        self.actionSbbel.setObjectName("actionSbbel")

        self.actionSquare_3 = QtWidgets.QAction(Project1)

        self.actionSquare_3.setObjectName("actionSquare_3")

        self.actionSquare_5 = QtWidgets.QAction(Project1)

        self.actionSquare_5.setObjectName("actionSquare_5")

        self.actionCross_3 = QtWidgets.QAction(Project1)

        self.actionCross_3.setObjectName("actionCross_3")

        self.actionSquare_4 = QtWidgets.QAction(Project1)

        self.actionSquare_4.setObjectName("actionSquare_4")

        self.actionSquare_6 = QtWidgets.QAction(Project1)

        self.actionSquare_6.setObjectName("actionSquare_6")

        self.actionCross_4 = QtWidgets.QAction(Project1)

        self.actionCross_4.setObjectName("actionCross_4")

        self.actionSquare_9 = QtWidgets.QAction(Project1)

        self.actionSquare_9.setObjectName("actionSquare_9")

        self.actionSquare_10 = QtWidgets.QAction(Project1)

        self.actionSquare_10.setObjectName("actionSquare_10")

        self.menuFile.addAction(self.actionOpen)

        self.menuFile.addAction(self.action_save)

        self.menuFile.addAction(self.actionSave_As)

        self.menuFile.addAction(self.actionExit)

        self.menuHistogram.addAction(self.actionInput)

        self.menuHistogram.addAction(self.actionOutput)

        self.menuHistogram.addAction(self.actionInput_Output)

        self.menuView.addAction(self.menuHistogram.menuAction())

        self.menuRGB.addAction(self.actionKuning)

        self.menuRGB.addAction(self.actionOrange)

        self.menuRGB.addAction(self.actionCyan)

        self.menuRGB.addAction(self.actionPurple)

        self.menuRGB.addAction(self.actionGrey)

        self.menuRGB.addAction(self.actionCoklat)

        self.menuRGB.addAction(self.actionMerah)

        self.menuRGB_to_Graysclae.addAction(self.actionAverage)

        self.menuRGB_to_Graysclae.addAction(self.actionLightness)

        self.menuRGB_to_Graysclae.addAction(self.actionLuminance)

        self.menuBrightness.addAction(self.actionContrast)
        self.menuBrightness.addAction(self.actionBrightness)

        self.menuBit_Depth.addAction(self.action1_bit)

        self.menuBit_Depth.addAction(self.action2_bit)

        self.menuBit_Depth.addAction(self.action2_bit_2)

        self.menuBit_Depth.addAction(self.action4_bit)

        self.menuBit_Depth.addAction(self.action5_bit)

        self.menuBit_Depth.addAction(self.action6_bit)

        self.menuBit_Depth.addAction(self.action7_bit)

        self.menuColors.addAction(self.menuRGB.menuAction())

        self.menuColors.addAction(self.menuRGB_to_Graysclae.menuAction())

        self.menuColors.addAction(self.menuBrightness.menuAction())

        self.menuColors.addAction(self.actionBrightness_Contrast)

        self.menuColors.addAction(self.actionInvers)

        self.menuColors.addAction(self.actionLog_Brightness)

        self.menuColors.addAction(self.menuBit_Depth.menuAction())

        self.menuColors.addAction(self.actionGamma_Correction)

        self.menuImage_Processing.addAction(self.actionHistogram_Equalization)

        self.menuImage_Processing.addAction(self.actionFuzzy_HE_RGB)

        self.menuImage_Processing.addAction(self.actionFuzzy_Grayscale)

        self.menuEdge_Detection.addAction(self.actionEdge_Detection_1)

        self.menuEdge_Detection.addAction(self.actionEdge_Detection_2)

        self.menuEdge_Detection.addAction(self.actionEdge_Detection_3)

        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x3)

        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_5x5)

        self.menuFilter.addAction(self.actionIDENTITY)

        self.menuFilter.addAction(self.menuEdge_Detection.menuAction())

        self.menuFilter.addAction(self.actionSharpen)

        self.menuFilter.addAction(self.menuGaussian_Blur.menuAction())

        self.menuFilter.addAction(self.actionUnsharp_Masking)

        self.menuFilter.addAction(self.actionAerage_Filter)

        self.menuFilter.addAction(self.actionLow_Pass_Filter)

        self.menuFilter.addAction(self.actionHigh_Pass_Filter)

        self.menuFilter.addAction(self.actionBandstop_Filter)

        self.menuEdge_Detection_2.addAction(self.actionPrewitt)

        self.menuEdge_Detection_2.addAction(self.actionSbbel)

        self.menuErosion.addAction(self.actionSquare_3)

        self.menuErosion.addAction(self.actionSquare_5)

        self.menuErosion.addAction(self.actionCross_3)

        self.menuDilation.addAction(self.actionSquare_4)

        self.menuDilation.addAction(self.actionSquare_6)

        self.menuDilation.addAction(self.actionCross_4)

        self.menuClosing.addAction(self.actionSquare_10)

        self.menuOpening.addAction(self.actionSquare_9)

        self.menuMorfologi.addAction(self.menuErosion.menuAction())

        self.menuMorfologi.addAction(self.menuDilation.menuAction())

        self.menuMorfologi.addAction(self.menuOpening.menuAction())

        self.menuMorfologi.addAction(self.menuClosing.menuAction())

        self.menubar.addAction(self.menuFile.menuAction())

        self.menubar.addAction(self.menuView.menuAction())

        self.menubar.addAction(self.menuColors.menuAction())

        self.menubar.addAction(self.menuImage_Processing.menuAction())

        self.menubar.addAction(self.menuAritmetical_Operation.menuAction())

        self.menubar.addAction(self.menuFilter.menuAction())

        self.menubar.addAction(self.menuEdge_Detection_2.menuAction())

        self.menubar.addAction(self.menuMorfologi.menuAction())

        self.menubar.addAction(self.menuGeometri.menuAction())

        self.actionAritmatika = QtWidgets.QAction(Project1)

        self.actionAritmatika.setObjectName("actionAritmatika")

        self.menuAritmetical_Operation.addAction(self.actionAritmatika)

        self.actionVertikal = QtWidgets.QAction(Project1)

        self.actionVertikal.setObjectName("actionVertikal")

        self.actionHorizontal = QtWidgets.QAction(Project1)

        self.actionHorizontal.setObjectName("actionHorizontal")

        self.actionCrop = QtWidgets.QAction(Project1)

        self.actionCrop.setObjectName("actionCrop")

        self.menuFlip.setObjectName("menuFlip")

        self.menuFlip.addAction(self.actionVertikal)

        self.menuFlip.addAction(self.actionHorizontal)

        self.menuGeometri.addAction(self.menuFlip.menuAction())

        self.menuGeometri.addAction(self.actionCrop)

        self.retranslateUi(Project1)

        QtCore.QMetaObject.connectSlotsByName(Project1)

    def retranslateUi(self, Project1):

        _translate = QtCore.QCoreApplication.translate

        Project1.setWindowTitle(_translate("Project1", "MainWindow"))

        self.menuFile.setTitle(_translate("Project1", "File"))

        self.menuView.setTitle(_translate("Project1", "View"))

        self.menuHistogram.setTitle(_translate("Project1", "Histogram"))

        self.menuColors.setTitle(_translate("Project1", "Colors"))

        self.menuRGB.setTitle(_translate("Project1", "RGB"))

        self.menuRGB_to_Graysclae.setTitle(

        _translate("Project1", "RGB to Graysclae"))

        self.menuBrightness.setTitle(_translate("Project1", "Brightness"))

        self.menuBit_Depth.setTitle(_translate("Project1", "Bit Depth"))

        self.menuImage_Processing.setTitle(

        _translate("Project1", "Image Processing"))

        self.menuAritmetical_Operation.setTitle(

        _translate("Project1", "Aritmetical Operation"))

        self.menuFilter.setTitle(_translate("Project1", "Filter"))

        self.menuEdge_Detection.setTitle(

        _translate("Project1", "Edge Detection"))

        self.menuGaussian_Blur.setTitle(

        _translate("Project1", "Gaussian Blur"))

        self.menuEdge_Detection_2.setTitle(

        _translate("Project1", "Edge Detection"))

        self.menuMorfologi.setTitle(_translate("Project1", "Morfologi"))

        self.menuErosion.setTitle(_translate("Project1", "Erosion"))

        self.menuDilation.setTitle(_translate("Project1", "Dilation"))

        self.menuClosing.setTitle(_translate("Project1", "Closing"))

        self.menuOpening.setTitle(_translate("Project1", "Opening"))

        self.menuGeometri.setTitle(_translate("Project1", "Geometri"))

        self.actionOpen.setText(_translate("Project1", "Open"))

        self.action_save.setText(_translate("Project1", "Save"))

        self.actionSave_As.setText(_translate("Project1", "Save As"))

        self.actionExit.setText(_translate("Project1", "Exit"))

        self.actionInput.setText(_translate("Project1", "Input"))

        self.actionOutput.setText(_translate("Project1", "Output"))

        self.actionInput_Output.setText(_translate("Project1", "Input Output"))

        self.actionBrightness_Contrast.setText(

        _translate("Project1", "Brightness - Contrast"))

        self.actionInvers.setText(_translate("Project1", "Invers"))

        self.actionLog_Brightness.setText(

        _translate("Project1", "Log Brightness"))

        self.actionGamma_Correction.setText(

        _translate("Project1", "Gamma Correction"))

        self.actionKuning.setText(_translate("Project1", "Kuning"))

        self.actionOrange.setText(_translate("Project1", "Orange"))

        self.actionCyan.setText(_translate("Project1", "Cyan"))

        self.actionPurple.setText(_translate("Project1", "Purple"))

        self.actionGrey.setText(_translate("Project1", "Grey"))

        self.actionCoklat.setText(_translate("Project1", "Coklat"))

        self.actionMerah.setText(_translate("Project1", "Merah"))

        self.actionAverage.setText(_translate("Project1", "Average"))

        self.actionLightness.setText(_translate("Project1", "Lightness"))

        self.actionLuminance.setText(_translate("Project1", "Luminance"))

        self.actionContrast.setText(_translate("Project1", "Contrast"))
        self.actionBrightness.setText(_translate("Project1", "Brightness"))

        self.action1_bit.setText(_translate("Project1", "1 bit"))

        self.action2_bit.setText(_translate("Project1", "2 bit"))

        self.action2_bit_2.setText(_translate("Project1", "3 bit"))

        self.action4_bit.setText(_translate("Project1", "4 bit"))

        self.action5_bit.setText(_translate("Project1", "5 bit"))

        self.action6_bit.setText(_translate("Project1", "6 bit"))

        self.action7_bit.setText(_translate("Project1", "7 bit"))

        self.actionHistogram_Equalization.setText(

        _translate("Project1", "Histogram Equalization"))

        self.actionFuzzy_HE_RGB.setText(_translate("Project1", "Fuzzy HE RGB"))

        self.actionFuzzy_Grayscale.setText(

        _translate("Project1", "Fuzzy Grayscale"))

        self.actionIDENTITY.setText(_translate("Project1", "Identity"))

        self.actionSharpen.setText(_translate("Project1", "Sharpen"))

        self.actionUnsharp_Masking.setText(

        _translate("Project1", "Unsharp Masking"))

        self.actionAerage_Filter.setText(

        _translate("Project1", "Average Filter"))

        self.actionLow_Pass_Filter.setText(

        _translate("Project1", "Low Pass Filter"))

        self.actionHigh_Pass_Filter.setText(

        _translate("Project1", "High Pass Filter"))

        self.actionBandstop_Filter.setText(

        _translate("Project1", "Bandstop Filter"))

        self.actionEdge_Detection_1.setText(

        _translate("Project1", "Edge Detection 1"))

        self.actionEdge_Detection_2.setText(

        _translate("Project1", "Edge Detection 2"))

        self.actionEdge_Detection_3.setText(

        _translate("Project1", "Edge Detection 3"))

        self.actionGaussian_Blur_3x3.setText(

        _translate("Project1", "Gaussian Blur 3x3"))

        self.actionGaussian_Blur_5x5.setText(

        _translate("Project1", "Gaussian Blur 5x5"))

        self.actionPrewitt.setText(_translate("Project1", "Prewitt"))

        self.actionSbbel.setText(_translate("Project1", "Sobel"))

        self.actionSquare_3.setText(_translate("Project1", "Square 3"))

        self.actionSquare_5.setText(_translate("Project1", "Square 5"))

        self.actionCross_3.setText(_translate("Project1", "Cross 3"))

        self.actionSquare_4.setText(_translate("Project1", "Square 3"))

        self.actionSquare_6.setText(_translate("Project1", "Square 5"))

        self.actionCross_4.setText(_translate("Project1", "Cross 3"))

        self.actionSquare_9.setText(_translate("Project1", "Square 9"))

        self.actionSquare_10.setText(_translate("Project1", "Square 9"))

        self.actionAritmatika.setText(_translate("Project1", "Aritmatika"))

        self.menuFlip.setTitle(_translate("Project1", "Flip"))

        self.actionCrop.setText(_translate("Project1", "Crop"))

        self.actionVertikal.setText(_translate("Project1", "Vertikal"))

        self.actionHorizontal.setText(_translate("Project1", "Horizontal"))