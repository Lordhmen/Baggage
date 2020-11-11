from os import system

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem

from data_base import *
from main_ui import *


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Установить валидатор
        pDoubleLineEdit = self.ui.lineEdit
        pDoubleValidator = QDoubleValidator(self)
        pDoubleLineEdit.setValidator(pDoubleValidator)

        p2DoubleLineEdit = self.ui.lineEdit_2
        p2DoubleValidator = QDoubleValidator(self)
        p2DoubleLineEdit.setValidator(p2DoubleValidator)

        p3DoubleLineEdit = self.ui.lineEdit_3
        p3DoubleValidator = QDoubleValidator(self)
        p3DoubleLineEdit.setValidator(p3DoubleValidator)

        self.ui.pushButton.clicked.connect(self.create_table)
        self.ui.pushButton_2.clicked.connect(self.creat_diagrama)
        self.ui.action_3.triggered.connect(self.close)
        self.ui.action_2.triggered.connect(self.about)
        self.ui.action_4.triggered.connect(self.open_file)
        self.ui.action_5.triggered.connect(self.avtor)

    def creat_diagrama(self):
        system('diagrama.py')

    def avtor(self):
        system('avtor.py')

    def about(self):
        system('about.py')

    def open_file(self):
        system('data_base.txt')

    def create_table(self):
        global data_base
        file = "data_base.txt"
        try:
            data_base = create_date_base(file)
            summm = self.ui.lineEdit.text()
            summ = summm.replace(",", ".")
            summ = float(summ)
            t_w = 0  # Переменная для посчета общего веса багажа
            for i in data_base:
                i.append(int(i[4]) * summ)
                t_w += int(i[4])  # Сумируем вес багажа всех пассажиров
            t_c = t_w * summ  # Находим стоимость всего багажа
            self.ui.lineEdit_2.setText(str(t_w))
            self.ui.lineEdit_3.setText(str(t_c))
            data_base.sort(key=lambda x: int(x[5]))
            self.ui.tableWidget.setRowCount(len(data_base))
            h = 0
            for i in data_base:
                self.ui.tableWidget.setItem(h, 0, QTableWidgetItem(i[0]))
                self.ui.tableWidget.setItem(h, 1, QTableWidgetItem(i[1]))
                self.ui.tableWidget.setItem(h, 2, QTableWidgetItem(i[2]))
                self.ui.tableWidget.setItem(h, 3, QTableWidgetItem(i[3]))
                self.ui.tableWidget.setItem(h, 4, QTableWidgetItem(i[4]))
                self.ui.tableWidget.setItem(h, 5, QTableWidgetItem(str(i[5])))
                h += 1
        except:
            system('error.py')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
