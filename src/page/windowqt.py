from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLabel,
)

from src.utils.words import words

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
LABEL_WIDTH = 300
LABEL_HEIGHT = 200

class WordWindow(QMainWindow):
    """
        main page of application
    """
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Word Remember")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.layout = QHBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.layout)
        self._showWords()
        #  self._createButtons()
        #  self._createDialog()

    def _showWords(self):
        self._fetch_words()
        for i in self.words:
            for j in ["AlignLeft", "AlignCenter", "AlignRight"]:
                label = QLabel(str(i))
                label.setFixedSize(LABEL_WIDTH, LABEL_HEIGHT)
                print(dir(Qt.AlignmentFlag))
                label.setAlignment(Qt.AlignmentFlag.__getattribute__(j))
                self.layout.addWidget(label)

    def _fetch_words(self):
        self.words = words(3)

