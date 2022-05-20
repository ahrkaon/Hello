from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import pyqtSignal

class LoginWidget(QWidget):
    close_signal = pyqtSignal()
    
    def __init__(self, parent, filename):
        super().__init__()
        self.setWindowTitle('로그인')
        self.parent = parent
        self.fn = filename
        self.cnt = 0
        
        self.initUi()
        
        #signal
        
        self.btn.clicked.connect(self.onLogin)
        self.close_signal.connect(self.parent.onFail)
    
    def initUi(self):
        #id
        idbox = QHBoxLayout()
        idbox.addWidget(QLabel('ID'))
        self.id = QLineEdit()
        idbox.addWidget(self.id)
        
        #pw
        pwbox = QHBoxLayout()
        pwbox.addWidget(QLabel('PW'))
        self.pw = QLineEdit()
        self.pw.setEchoMode(QLineEdit.Password)
        pwbox.addWidget(self.pw)
        
        vbox = QVBoxLayout()
        vbox.addLayout(idbox)
        vbox.addLayout(pwbox)
        
        self.btn = QPushButton('로그인')
        vbox.addWidget(self.btn)
        
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(spacer)
        self.setLayout(vbox)
        
    def onLogin(self):
        id = self.id.text()
        pw = self.pw.text()
        
        if id and pw:
            member = self.readFile()
            bFind = False
            for _id, _pw in member:
                if id == _id and pw == _pw:
                    bFind = True
                    break
            if bFind:
                QMessageBox.information(self, '환영합니다!', '로그인 성공', QMessageBox.Ok)
            else:
                self.cnt += 1
                txt = f'로그인 {self.cnt} 회 실패'
                QMessageBox.critical(self, 'ID, PW가 맞지 않습니다!', txt, QMessageBox.Ok)
                if self.cnt>=3:
                    self.close_signal.emit()
    def readFile(self):
        member = []
        with open(self.fn, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                
                if not line:
                    break
                line = line.replace('\n', '')
                id, pw = line.split(' ')
                member.append((id, pw))
        return member

