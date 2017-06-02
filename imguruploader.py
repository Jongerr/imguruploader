import sys
from PyQt4.QtGui import QPixmap, QApplication
from datetime import datetime


date = datetime.now()
filename = date.strftime('%d-%m-%Y_%Hh-%Mm-%Ss.jpg')
app = QApplication(sys.argv)
desktop = app.desktop()
screen1 = desktop.screenGeometry(0).width()
screen2 = desktop.screenGeometry(1).width()
screen3 = desktop.screenGeometry(2).width()
print('Screen1 width: {0}\nScreen2 width: {1}\nScreen3 width: {2}\n'.format(screen1, screen2, screen3))
print('It\'s working!')
#QPixmap.grabWindow(QApplication.desktop().winId()).save(filename, 'jpg')
QPixmap.grabWindow(desktop.winId(), x=-screen3, width=screen3).save('pictures/' + filename, 'jpg')
