# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QUrl
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setDocumentMode(True)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen_Project = QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConsole_Visibility = QAction(MainWindow)
        self.actionConsole_Visibility.setObjectName("actionConsole_Visibility")
        self.actionConsole_Visibility.setCheckable(True)
        self.actionConsole_Visibility.setChecked(True)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.directory_path = QLineEdit(self.centralwidget)
        self.directory_path.setObjectName("directory_path")

        self.horizontalLayout.addWidget(self.directory_path)

        self.browse = QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")

        self.horizontalLayout.addWidget(self.browse)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.template_tree = QTreeView(self.centralwidget)
        self.template_tree.setObjectName("template_tree")
        self.template_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.template_tree.setUniformRowHeights(True)
        self.template_tree.setSortingEnabled(True)
        self.template_tree.header().setMinimumSectionSize(20)
        self.template_tree.header().setDefaultSectionSize(150)
        self.template_tree.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.template_tree)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.template_version = QLineEdit(self.centralwidget)
        self.template_version.setObjectName("template_version")
        self.template_version.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.template_version)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.working_tree = QTreeView(self.centralwidget)
        self.working_tree.setObjectName("working_tree")
        self.working_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.working_tree.setUniformRowHeights(True)
        self.working_tree.setSortingEnabled(True)
        self.working_tree.header().setMinimumSectionSize(20)
        self.working_tree.header().setDefaultSectionSize(150)
        self.working_tree.header().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.working_tree)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.directory_version = QLineEdit(self.centralwidget)
        self.directory_version.setObjectName("directory_version")
        self.directory_version.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.directory_version)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.cleanup_working = QPushButton(self.centralwidget)
        self.cleanup_working.setObjectName("cleanup_working")
        self.cleanup_working.setFlat(False)

        self.horizontalLayout_4.addWidget(self.cleanup_working)

        self.copy_template = QPushButton(self.centralwidget)
        self.copy_template.setObjectName("copy_template")

        self.horizontalLayout_4.addWidget(self.copy_template)

        self.add_selected = QPushButton(self.centralwidget)
        self.add_selected.setObjectName("add_selected")

        self.horizontalLayout_4.addWidget(self.add_selected)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menubar.setDefaultUp(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        # self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "projectdiffview", None)
        )
        self.actionPreferences.setText(
            QCoreApplication.translate("MainWindow", "Preferences", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+,", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        # if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+Q", None))
        # endif // QT_CONFIG(shortcut)
        self.actionNew_Project.setText(
            QCoreApplication.translate("MainWindow", "New Project", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionNew_Project.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", "Save", None))
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        self.actionOpen_Project.setText(QCoreApplication.translate("MainWindow", "Open", None))
        # if QT_CONFIG(shortcut)
        self.actionOpen_Project.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(
            QCoreApplication.translate("MainWindow", "Documentation", None)
        )
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.actionConsole_Visibility.setText(
            QCoreApplication.translate("MainWindow", "Console Visibility", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionConsole_Visibility.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+`", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", "Save As", None))
        # if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Shift+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", "Project Directory", None))
        self.browse.setText(QCoreApplication.translate("MainWindow", "Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Template Version:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Folder Version:", None))
        self.cleanup_working.setText(
            QCoreApplication.translate("MainWindow", "Cleanup Folder", None)
        )
        self.copy_template.setText(
            QCoreApplication.translate("MainWindow", "Add All to Folder", None)
        )
        self.add_selected.setText(
            QCoreApplication.translate("MainWindow", "Add Selected to Folder", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "&Help", None))

    # retranslateUi
