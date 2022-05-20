from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
                             QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QMessageBox)
class JoinWidget(QWidget):
    FILE_NAME = 'Member.txt'
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('회원가입')
        self.initUi()
        self.readFile()
        
        self.btn.clicked.connect(self.onJoin)
        
    def initUi(self):
        joinbox = QGroupBox('ID, Password 설정')
        
        #id
        idbox = QHBoxLayout()
        idbox.addWidget(QLabel('ID'))
        self.id = QLineEdit()
        idbox.addWidget(self.id)
        
        #pw
        pwbox = QHBoxLayout()
        pwbox.addWidget(QLabel('PW'))
        self.pw = QLineEdit()
        pwbox.addWidget(self.pw)
        
        vbox = QVBoxLayout()
        vbox.addLayout(idbox)
        vbox.addLayout(pwbox)
        self.btn = QPushButton('회원가입')
        vbox.addWidget(self.btn)
        joinbox.setLayout(vbox)
        
        #check member
        membox = QGroupBox('가입된 회원 정보')
        self.table = QTableWidget()
        label = ('ID', 'PW')
        self.table.setColumnCount(len(label))
        self.table.setHorizontalHeaderLabels(label)
        self.table.setAlternatingRowColors(True)
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        membox.setLayout(vbox)
        
        #all layout
        vbox = QVBoxLayout()
        vbox.addWidget(joinbox)
        vbox.addWidget(membox)
        
        self.setLayout(vbox)
    def readFile(self):
        try:
            f = open(JoinWidget.FILE_NAME, 'r', encoding = 'utf-8')
        except FileNotFoundError as e:
            print(e)
            f = open(JoinWidget.FILE_NAME, 'w', encoding='utf-8')
            f.close()
        else:
            row = self.table.rowCount()
            while True:
                line = f.readline()
                
                if not line:
                    break
                line = line.replace('\n', '')
                id, pw = line.split(' ')
                self.table.setRowCount(row+1)
                self.table.setItem(row, 0, QTableWidgetItem(id))
                self.table.setItem(row, 1, QTableWidgetItem(pw))
                row += 1
            f.close()
    def writeFile(self, id, pw):
        with open(JoinWidget.FILE_NAME, 'a', encoding='utf-8') as f:
            member = f'{id} {pw}\n'
            f.write(member)
    def onJoin(self):
        id = self.id.text()
        pw = self.pw.text()
        
        if id and pw and not self.findIDs(id):
            row = self.table.rowCount()
            self.table.setRowCount(row+1)
            self.table.setItem(row, 0, QTableWidgetItem(id))
            self.table.setItem(row, 1, QTableWidgetItem(pw))
            self.writeFile(id,pw)
            self.id.clear()
            self.pw.clear()
        else:
            QMessageBox.information(self, 'Error!', '아이디(중복), 비번을 입력하세요!', QMessageBox.Ok)
    def findIDs(self, id):
        row = self.table.rowCount()
        bOverlap = False
        for r in range(row):
            id_item = self.table.item(r,0)
            if id==id_item.text():
                bOverlap = True
                break
        return bOverlap