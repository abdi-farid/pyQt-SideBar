#########################################################
# IMPORTS 
#########################################################
import sys
import os 
import resource_rc
#from PySide2 import *

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect



#########################################################
# IMPORT GUI FILE
from interface_ui import *
#########################################################





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ###########################################
        # Remove window title bar
        ###########################################
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)


        ###########################################
        # set main background to transparent
        ###########################################
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        ###########################################
        # shadow effect style
        ###########################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 92, 157, 550))
        
        ###########################################
        # apply shadow to central widget 
        ###########################################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)


        self.setWindowIcon(QtGui.QIcon(':/icons/icons/activity.svg'))
        self.setWindowTitle('Moder UI GES')
        


        QSizeGrip(self.ui.size_grip)


        self.ui.minimize_window_button.clicked.connect(lambda :self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda :self.close())
        self.ui.exit_button.clicked.connect(lambda :self.close())
        


        ###########################################
        # Restore/Maximize  window 
        ###########################################
        self.ui.restore_window_button.clicked.connect(lambda : self.restore_or_maximize_window())
        
        ###########################################
        # function to move window with mouse 
        ###########################################
        def moveWindow(e):
            if self.isMaximized()==False:
                if e.buttons() ==  Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow



        self.ui.open_close_sidebar_button.clicked.connect(lambda : self.slideLeftMenu())

        




        self.show()


    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()

        if width == 0:
            newWidth =  200
            self.ui.open_close_sidebar_button.setIcon(QtGui.QIcon(':/icons/icons/chevron-left.svg'))
        else :
            newWidth =  0
            self.ui.open_close_sidebar_button.setIcon(QtGui.QIcon(':/icons/icons/align-left.svg'))

        # self.animation = 

        self.ui.slide_menu_container.setFixedWidth(newWidth)



    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()


    def restore_or_maximize_window(self):
            if  self.isMaximized():
                self.showNormal()
                self.ui.restore_window_button.setIcon(QtGui.QIcon(':/icons/icons/maximize-2.svg'))

            else : 
                self.showMaximized()
                self.ui.restore_window_button.setIcon(QtGui.QIcon(':/icons/icons/minimize-2.svg'))
        



#########################################################
# EXECUTE THE APP
#########################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())




#########################################################







#########################################################






#########################################################

