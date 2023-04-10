import requests
import json
import time
import sys
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QPoint
from getNames import get_names

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.tt = ThreadTask(main_window=self.ui)
        self.ui.complited = False

        self.get_names = get_names()
        self.load_weapons()

        self.ui.runTask.clicked.connect(self.start_thread)
        self.ui.stopTask.clicked.connect(self.stop_thread)
        self.ui.closeAppButton.clicked.connect(self.close_app)
        self.ui.minimizeAppButton.clicked.connect(self.minimize_app)

    def minimize_app(self):
        self.showMinimized()

    def close_app(self):
        self.close()

    def start_thread(self):
        self.tt.start()

    def stop_thread(self):
        self.ui.complited = True
        self.tt.quit()

    def load_weapons(self):
        self.ui.comboBox.addItems(self.get_names)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def focus(self):
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

class ThreadTask(QThread):

    def __init__(self, main_window, parrent=None):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.url = "https://api.warframe.market/v1/auctions/search?type=riven&weapon_url_name=" \
                   + self.main_window.comboBox.currentText() + "&polarity=any&sort_by=price_asc"
        self.main_window.complited = False
        while (self.main_window.complited == False):
            self.responce = requests.get(self.url).text
            self.data = json.loads(self.responce)
            for self.auction in self.data["payload"]["auctions"]:
                if self.auction["owner"]["status"] == "ingame":
                    if self.auction["buyout_price"] != None and self.auction["buyout_price"] <= int(self.main_window.spinBox.text()):
                        self.price_auction = self.auction["buyout_price"]
                        self.print_auction = "price: " + str(self.price_auction) + "\n" + \
                                        "contact: " + "/w " + self.auction["owner"]["ingame_name"] + " hi, i want buy riven for " + self.main_window.comboBox.currentText() + "\n"
                        self.main_window.plainTextEdit.textCursor().insertText(self.print_auction)
                        self.main_window.complited = True

                    else:
                        continue
                else:
                    continue

            time.sleep(3)  # Terms of use warframe.market API forbid make a request more than 3 seconds

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()




