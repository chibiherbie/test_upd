import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from some import privet

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)


def upd():
    pass


def main():
    window = MainWindow()
    window.show()

    app.exec()


update = False
if __name__ == '__main__':
    if not update:
        print(privet)
        main()
    upd()





