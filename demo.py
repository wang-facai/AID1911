import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from day16 import untitled

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.setWindowTitle("nmsl")
    mainWindow.show()
    sys.exit(app.exec_())
