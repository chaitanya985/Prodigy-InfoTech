# TEMPERATURE CONVERSION PROGRAM

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Temperature Converter')
        self.setGeometry(100, 100, 400, 400)
        layout = QVBoxLayout()

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.from_unit = QComboBox()
        self.from_unit.addItems(['Celsius', 'Fahrenheit', 'Kelvin'])
        layout.addWidget(self.from_unit)

        self.to_unit = QComboBox()
        self.to_unit.addItems(['Celsius', 'Fahrenheit', 'Kelvin'])
        layout.addWidget(self.to_unit)

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_temperature)
        layout.addWidget(self.convert_button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.show()

    def convert_temperature(self):
        try:
            temperature = float(self.input_box.text())
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
                result = (temperature * 9/5) + 32
            elif from_unit == 'Celsius' and to_unit == 'Kelvin':
                result = temperature + 273.15
            elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
                result = (temperature - 32) * 5/9
            elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
                result = (temperature - 32) * 5/9 + 273.15
            elif from_unit == 'Kelvin' and to_unit == 'Celsius':
                result = temperature - 273.15
            elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
                result = (temperature - 273.15) * 9/5 + 32
            else:
                result = temperature

            self.result_label.setText(f'Result: {result} {to_unit}')
        except ValueError:
            self.result_label.setText('Invalid input. Please enter a valid number.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    sys.exit(app.exec_())
