from PyQt5.QtWidgets import QMainWindow, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QMessageBox, QErrorMessage, QHBoxLayout, QFormLayout
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtCore import Qt
from logic import vote
from logic import john_votes, jane_votes, total_votes



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

        # Create a horizontal box layout for the ID label and input field
        id_layout = QHBoxLayout()
        id_layout.addWidget(self.label_ID)
        id_layout.addWidget(self.lineEdit)

        self.radioButtonJohn = QRadioButton("John")
        self.radioButtonJane = QRadioButton("Jane")

        # Replace QHBoxLayout with QVBoxLayout for the radio buttons
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.radioButtonJohn)
        radio_layout.addWidget(self.radioButtonJane)

        # Create a QHBoxLayout and add QVBoxLayout into it for centering radio buttons.
        center_radio_layout = QHBoxLayout()
        center_radio_layout.addStretch(1)
        center_radio_layout.addLayout(radio_layout)
        center_radio_layout.addStretch(1)

        self.pushButton_vote = QPushButton("SUBMIT VOTE")
        self.pushButton_vote.clicked.connect(self.buttonClicked)

        # Use QVBoxLayout for the main layout and add the new layouts
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

        if id_code == "":
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Please enter an ID.')
            return

        candidate = 0
        if self.radioButtonJohn.isChecked():
            candidate = 1
        elif self.radioButtonJane.isChecked():
            candidate = 2

        # Check if a candidate is selected
        if candidate == 0:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Please select a candidate.')
            return

        vote(candidate, id_code, self)

        from logic import john_votes, jane_votes, total_votes
        self.label_John_votes.setText(f"John Votes: {john_votes}")
        self.label_Jane_votes.setText(f"Jane Votes: {jane_votes}")
        self.label_total_votes.setText(f"Total Votes: {total_votes}")


