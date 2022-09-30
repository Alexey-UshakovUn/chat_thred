from PyQt5 import QtWidgets
import gui
from client import run


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connect()

        self.pushButton.clicked.connect(self.send)

    def send(self):
        self.textBrowser.append(self.lineEdit.text())
        self.lineEdit.clear()

    def connect(self):
        try:
            run()
        except Exception:
            print('cant')



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()