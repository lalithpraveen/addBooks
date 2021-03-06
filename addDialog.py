# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addBookDialog(object):
    def setupUi(self, addBookDialog):
        addBookDialog.setObjectName("addBookDialog")
        addBookDialog.resize(679, 514)
        self.layoutWidget = QtWidgets.QWidget(addBookDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(41, 21, 591, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_book = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.add_book.setFont(font)
        self.add_book.setAlignment(QtCore.Qt.AlignCenter)
        self.add_book.setObjectName("add_book")
        self.verticalLayout.addWidget(self.add_book)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.id = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.name = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.description = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.isbn = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.isbn.setFont(font)
        self.isbn.setObjectName("isbn")
        self.pagecount = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pagecount.setFont(font)
        self.pagecount.setObjectName("pagecount")
        self.issued = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.issued.setFont(font)
        self.issued.setObjectName("issued")
        self.author = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.author.setFont(font)
        self.author.setObjectName("author")
        self.year = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.year.setFont(font)
        self.year.setObjectName("year")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.id_spinBox = QtWidgets.QSpinBox(self.splitter)
        self.id_spinBox.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.id_spinBox.setFont(font)
        self.id_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.id_spinBox.setMaximum(1000)
        self.id_spinBox.setObjectName("id_spinBox")
        self.name_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_input.setFont(font)
        self.name_input.setText("")
        self.name_input.setObjectName("name_input")
        self.description_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.description_input.setFont(font)
        self.description_input.setText("")
        self.description_input.setObjectName("description_input")
        self.isbn_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.isbn_input.setFont(font)
        self.isbn_input.setObjectName("isbn_input")
        self.pagecount_spinBox = QtWidgets.QSpinBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pagecount_spinBox.setFont(font)
        self.pagecount_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pagecount_spinBox.setMaximum(9900)
        self.pagecount_spinBox.setObjectName("pagecount_spinBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.yes_radioButton.setFont(font)
        self.yes_radioButton.setObjectName("yes_radioButton")
        self.horizontalLayout.addWidget(self.yes_radioButton)
        self.no_radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.no_radioButton.setFont(font)
        self.no_radioButton.setObjectName("no_radioButton")
        self.horizontalLayout.addWidget(self.no_radioButton)
        self.author_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.author_input.setFont(font)
        self.author_input.setObjectName("author_input")
        self.year_spinBox = QtWidgets.QSpinBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.year_spinBox.setFont(font)
        self.year_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.year_spinBox.setMaximum(5000)
        self.year_spinBox.setObjectName("year_spinBox")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addBookDialog)
        self.buttonBox.accepted.connect(addBookDialog.accept)
        self.buttonBox.rejected.connect(addBookDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addBookDialog)

    def retranslateUi(self, addBookDialog):
        _translate = QtCore.QCoreApplication.translate
        addBookDialog.setWindowTitle(_translate("addBookDialog", "Add Book Dialog"))
        self.add_book.setText(_translate("addBookDialog", "Add Book"))
        self.id.setText(_translate("addBookDialog", "ID"))
        self.name.setText(_translate("addBookDialog", "Name"))
        self.description.setText(_translate("addBookDialog", "Description"))
        self.isbn.setText(_translate("addBookDialog", "ISBN"))
        self.pagecount.setText(_translate("addBookDialog", "Page Count"))
        self.issued.setText(_translate("addBookDialog", "Issued"))
        self.author.setText(_translate("addBookDialog", "Author"))
        self.year.setText(_translate("addBookDialog", "Year"))
        self.name_input.setPlaceholderText(_translate("addBookDialog", "Enter your book Title"))
        self.description_input.setPlaceholderText(_translate("addBookDialog", "Enter your book Description"))
        self.isbn_input.setPlaceholderText(_translate("addBookDialog", "Enter your book ISBN"))
        self.yes_radioButton.setText(_translate("addBookDialog", "Yes"))
        self.no_radioButton.setText(_translate("addBookDialog", "No"))
        self.author_input.setPlaceholderText(_translate("addBookDialog", "Enter your book Author"))
