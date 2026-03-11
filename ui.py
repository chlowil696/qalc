# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(400, 400))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.equation_edit = QLineEdit(self.centralwidget)
        self.equation_edit.setObjectName(u"equation_edit")
        self.equation_edit.setMinimumSize(QSize(0, 48))
        self.equation_edit.setMaximumSize(QSize(16777215, 48))
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setPointSize(18)
        self.equation_edit.setFont(font)
        self.equation_edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.equation_edit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.equation_edit)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.subtract = QPushButton(self.centralwidget)
        self.subtract.setObjectName(u"subtract")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtract.sizePolicy().hasHeightForWidth())
        self.subtract.setSizePolicy(sizePolicy)
        self.subtract.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.subtract, 3, 3, 1, 1)

        self.six = QPushButton(self.centralwidget)
        self.six.setObjectName(u"six")
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.six, 2, 2, 1, 1)

        self.three = QPushButton(self.centralwidget)
        self.three.setObjectName(u"three")
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.three, 3, 2, 1, 1)

        self.seven = QPushButton(self.centralwidget)
        self.seven.setObjectName(u"seven")
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.seven, 1, 0, 1, 1)

        self.nine = QPushButton(self.centralwidget)
        self.nine.setObjectName(u"nine")
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.nine, 1, 2, 1, 1)

        self.divide = QPushButton(self.centralwidget)
        self.divide.setObjectName(u"divide")
        sizePolicy.setHeightForWidth(self.divide.sizePolicy().hasHeightForWidth())
        self.divide.setSizePolicy(sizePolicy)
        self.divide.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.divide, 1, 3, 1, 1)

        self.decimal = QPushButton(self.centralwidget)
        self.decimal.setObjectName(u"decimal")
        sizePolicy.setHeightForWidth(self.decimal.sizePolicy().hasHeightForWidth())
        self.decimal.setSizePolicy(sizePolicy)
        self.decimal.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.decimal, 4, 0, 1, 1)

        self.five = QPushButton(self.centralwidget)
        self.five.setObjectName(u"five")
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.five, 2, 1, 1, 1)

        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.clear, 4, 2, 1, 1)

        self.equals = QPushButton(self.centralwidget)
        self.equals.setObjectName(u"equals")
        sizePolicy.setHeightForWidth(self.equals.sizePolicy().hasHeightForWidth())
        self.equals.setSizePolicy(sizePolicy)
        self.equals.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.equals, 4, 3, 1, 1)

        self.zero = QPushButton(self.centralwidget)
        self.zero.setObjectName(u"zero")
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.zero, 4, 1, 1, 1)

        self.two = QPushButton(self.centralwidget)
        self.two.setObjectName(u"two")
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.two, 3, 1, 1, 1)

        self.four = QPushButton(self.centralwidget)
        self.four.setObjectName(u"four")
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.four, 2, 0, 1, 1)

        self.add = QPushButton(self.centralwidget)
        self.add.setObjectName(u"add")
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.add, 2, 3, 1, 1)

        self.one = QPushButton(self.centralwidget)
        self.one.setObjectName(u"one")
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.one, 3, 0, 1, 1)

        self.eight = QPushButton(self.centralwidget)
        self.eight.setObjectName(u"eight")
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.eight, 1, 1, 1, 1)

        self.left_para = QPushButton(self.centralwidget)
        self.left_para.setObjectName(u"left_para")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_para.sizePolicy().hasHeightForWidth())
        self.left_para.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.left_para, 0, 1, 1, 1)

        self.exponent = QPushButton(self.centralwidget)
        self.exponent.setObjectName(u"exponent")
        sizePolicy1.setHeightForWidth(self.exponent.sizePolicy().hasHeightForWidth())
        self.exponent.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.exponent, 0, 0, 1, 1)

        self.right_para = QPushButton(self.centralwidget)
        self.right_para.setObjectName(u"right_para")
        sizePolicy1.setHeightForWidth(self.right_para.sizePolicy().hasHeightForWidth())
        self.right_para.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.right_para, 0, 2, 1, 1)

        self.multiply = QPushButton(self.centralwidget)
        self.multiply.setObjectName(u"multiply")
        sizePolicy1.setHeightForWidth(self.multiply.sizePolicy().hasHeightForWidth())
        self.multiply.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.multiply, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qalc", None))
        self.equation_edit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.subtract.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.decimal.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.left_para.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.exponent.setText(QCoreApplication.translate("MainWindow", u"x^", None))
        self.right_para.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
    # retranslateUi

