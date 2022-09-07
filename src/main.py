import sys
from  PyQt5.QtWidgets import QApplication

from  src.page.windowqt import WordWindow


def main():
    app = QApplication([])
    window = WordWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
