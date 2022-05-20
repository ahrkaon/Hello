from PyQt5.QtWidgets import QApplication, QTabWidget
from join import JoinWidget
from login import LoginWidget
import sys

class Form(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Practice")
        
        join = JoinWidget()
        login = LoginWidget(self, JoinWidget.FILE_NAME)
        self.addTab(join, join.windowTitle())
        self.addTab(login, login.windowTitle())
    def onFail(self):
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())