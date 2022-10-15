from PyQt5.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QWidget,
)
from PyQt5.QtCore import QSize, Qt

from src.utils.words import word_generator
from src.utils.words import add_new_word


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
LABEL_WIDTH = 300
LABEL_HEIGHT = 100
INPUT_HEIGHT = 100


class WordWindow(QMainWindow):
    """
        main page of application
    """
    def __init__(self):
        super().__init__()
        self.words = self._fetch_words()
        self.setWindowTitle("Word Remember")
        self.size = QSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(self.size)
        # add main window of app
        main_layout = QVBoxLayout()
        # add label to pay attention
        self.attention= QLabel("Don't forget reading words")
        font = self.attention.font()
        font.setPointSize(18)
        self.attention.setFont(font)
        self.attention.setFixedSize(QSize(LABEL_WIDTH, INPUT_HEIGHT))
        self.attention.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        main_layout.addWidget(self.attention)
        # add input that get new words to add the db
        self.new_word_input = QLineEdit()
        self.new_word_input.setPlaceholderText('Add New word')
        self.new_word_input.setFixedSize(QSize(LABEL_WIDTH, 100))
        self.new_word_input.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        self.new_word_input.textChanged.connect(self._input_text_changed)
        self.new_word_input.returnPressed.connect(self.press_enter_key)
        self.new_word = None
        # new_word_input
        main_layout.addWidget(self.new_word_input)
        word_content = self.word_content()
        main_layout.addLayout(word_content)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        page = QWidget()
        page.setLayout(main_layout)
        self.setCentralWidget(page)

    def _fetch_words(self):
        """
        yield words from DB
        """
        yield from word_generator()

    def word_content(self):
        """
        add words layer table
        """
        parent_layout = QHBoxLayout()
        r_layout = self.add_content()
        c_layout = self.add_content()
        l_layout = self.add_content()
        for i in [r_layout, c_layout, l_layout]:
            parent_layout.addLayout(i)
        return parent_layout

    def add_content(self):
        """
        add word and definition to page
        """
        try:
            word = next(self.words)
        except StopIteration:
            self.word = self._fetch_words()
        layout = QVBoxLayout()
        word_label = QLabel(word.get('word', "Sth went wrong"))
        font = word_label.font()
        font.setPointSize(14)
        word_label.setFont(font)
        word_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        word_label.setFixedWidth(WINDOW_WIDTH / 3)
        layout.addWidget(word_label)
        definition = QLabel()
        font = definition.font()
        font.setPointSize(10)
        definition.setFont(font)
        definition.setText(word.get('definition', 'Sth went wrong'))
        definition.setFixedSize(QSize(WINDOW_WIDTH / 3, 400))
        layout.addWidget(definition)
        return layout

    def _input_text_changed(self, s: str):
        """
        store new word in temporary variable
        """
        self.new_word = s

    def press_enter_key(self):
        """
        new_word_input return key pressed
        """
        print("Return key pressed")
        result = add_new_word(self.new_word)
        self.attention.setText("Success" if result else "Falied")
        self.new_word_input.clear()
