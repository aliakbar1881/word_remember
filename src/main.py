import sys
from  PyQt5.QtWidgets import QApplication

from  src.page.windowqt import WordWindow


def main():
    app = QApplication(sys.argv)
    window = WordWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
