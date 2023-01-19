import os
import sys

import requests
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from some import privet

VERSION = 2


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me! UPDATE BTN")

        self.setFixedSize(QSize(400, 300))

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

        button.clicked.connect(self.upd)

    def upd(self):
        try:
            link = "https://raw.githubusercontent.com/chibiherbie/test_upd/main/VERSION.txt"
            check = requests.get(link)

            if float(VERSION) < float(check.text):
                print('Обновление')
                filename = os.path.basename(sys.argv[0])

                for file in os.listdir():
                    if file == filename:
                        pass

                    else:
                        os.remove(file)

                exename = 'test_upd.rar'
                code = requests.get(
                    "https://github.com/chibiherbie/test_upd/releases/download/test_tag/test_upd.rar",
                    allow_redirects=True)
                open(exename, 'wb').write(code.content)

                os.remove(sys.argv[0])
                sys.exit()

            else:
                print('Обвновлений нет')

        except Exception as e:
            print(e)

app = QApplication(sys.argv)


def main():
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    print(privet)
    main()






