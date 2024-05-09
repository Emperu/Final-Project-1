from PyQt5.QtWidgets import QMainWindow, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QMessageBox, QErrorMessage, QHBoxLayout, QFormLayout
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtCore import Qt
from logic import vote
from logic import john_votes, jane_votes, total_votes
from logic import process_vote



class GuiWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 250)

        self.label_title = QLabel("VOTING APPLICATION")
        font = QFont()
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.label_ID = QLabel("ID: ")
        self.lineEdit = QLineEdit()
        self.lineEdit.setValidator(QIntValidator())

        id_layout = QHBoxLayout()
        id_layout.addWidget(self.label_ID)
        id_layout.addWidget(self.lineEdit)

        self.radioButtonJohn = QRadioButton("John")
        self.radioButtonJane = QRadioButton("Jane")

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.radioButtonJohn)
        radio_layout.addWidget(self.radioButtonJane)

        center_radio_layout = QHBoxLayout()
        center_radio_layout.addStretch(1)
        center_radio_layout.addLayout(radio_layout)
        center_radio_layout.addStretch(1)

        self.pushButton_vote = QPushButton("SUBMIT VOTE")
        self.pushButton_vote.clicked.connect(self.buttonClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addLayout(id_layout)
        layout.addLayout(center_radio_layout)
        layout.addWidget(self.pushButton_vote)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.label_John_votes = QLabel("John Votes: 0")
        self.label_Jane_votes = QLabel("Jane Votes: 0")
        self.label_total_votes = QLabel("Total Votes: 0")

        self.label_John_votes.setAlignment(Qt.AlignCenter)
        self.label_Jane_votes.setAlignment(Qt.AlignCenter)
        self.label_total_votes.setAlignment(Qt.AlignCenter)

        self.label_John_votes.setStyleSheet('color: green; font-size: 14px;')
        self.label_Jane_votes.setStyleSheet('color: green; font-size: 14px;')
        self.label_total_votes.setStyleSheet('color: green; font-size: 14px;')

        layout.addWidget(self.label_John_votes)
        layout.addWidget(self.label_Jane_votes)
        layout.addWidget(self.label_total_votes)

    def buttonClicked(self):
        id_code = self.lineEdit.text()
        candidate = 0
        if self.radioButtonJohn.isChecked():
            candidate = 1
        elif self.radioButtonJane.isChecked():
            candidate = 2

        labels = [self.label_John_votes, self.label_Jane_votes, self.label_total_votes]

        error_message = process_vote(id_code, candidate, self, labels)
        if error_message:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage(error_message)
            error_dialog.exec()
