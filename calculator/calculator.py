import sys

from PyQt5.QtWidgets import (QApplication,
                             QComboBox,
                             QDialog,
                             QDialogButtonBox,
                             QFormLayout,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             QMenu,
                             QMenuBar,
                             QMessageBox,
                             QPushButton,
                             QSpinBox,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon

from processor import Processor

class App(QWidget):

    def __init__(self):
        super().__init__()

        self._processor = Processor()

        self.title = 'PyQt5 calculator'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create display
        self.textbox = QLabel(self)
        self.textbox.setAlignment(Qt.AlignRight)
        self.textbox.setStyleSheet('font-size: 40px;'
                                   'color: #66ff66;;'
                                   'background-color: #222222;'
                                   'border: 2px solid #111111;'
                                   'padding-right: 4px;'
                                   'text-align: right;')

        # Create buttons
        self.createButtonsGrid()

        # Add to main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.textbox)
        mainLayout.addWidget(self.buttonsGroupBox)
        self.setLayout(mainLayout)

        self.show()

    def createButtonsGrid(self):
        self.buttonsGroupBox = QGroupBox()

        layout = QGridLayout()

        for i, button_label in enumerate('C   789/456*123-.0=+'):
            if button_label != ' ':
                button = QPushButton(button_label)
                button.setStyleSheet('font-size: 40px;'
                                     'background-color: #ffffff;'
                                     'border: 2px solid #222222;'
                                     'border-radius: 6px;'
                                     'text-align: center;'
                                     'vertical-align: middle')
                button.setFixedSize(60, 60)
                button.clicked.connect(self.on_click)
                layout.addWidget(button, i//4, i%4)

        self.buttonsGroupBox.setLayout(layout)


    @pyqtSlot()
    def on_click(self):
        buttonPressed = self.sender().text()
        self._processor.keyPressed(buttonPressed);
        self.textbox.setText(self._processor.getResult())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())