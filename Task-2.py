#NUMBER GUESSING GAME

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import random

class GuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.number = random.randint(1, 100)
        self.attempts = 0

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Number Guessing Game')

        self.label = QLabel('Guess a number between 1 and 100:', self)
        self.label.setFont(QFont('Arial', 12))
        self.label.move(50, 30)

        self.input = QLineEdit(self)
        self.input.move(150, 70)

        self.button = QPushButton('Guess', self)
        self.button.move(180, 100)
        self.button.clicked.connect(self.checkGuess)

        self.show()

    def checkGuess(self):
        guess = int(self.input.text())
        self.attempts += 1

        if guess < self.number:
            self.label.setText('Too low, try again.')
        elif guess > self.number:
            self.label.setText('Too high, try again.')
        else:
            self.label.setText(f'You guessed the number in {self.attempts} attempts.')
            self.label.setDisabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessingGame()
    sys.exit(app.exec_())
