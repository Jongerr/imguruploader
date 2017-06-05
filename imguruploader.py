import os
import sys
import keyboard
from PyQt4.QtGui import QPixmap, QApplication
from datetime import datetime


def save_screen(screen_id):
    
    date = datetime.now()
    filename = date.strftime('%m-%d-%Y_%Hh-%Mm-%Ss.jpg')
    
    app = QApplication(sys.argv)
    desktop = app.desktop()
    
    screen1 = desktop.screenGeometry(0).width()
    screen2 = desktop.screenGeometry(1).width()
    screen3 = desktop.screenGeometry(2).width()

    if screen_id == 1:
        QPixmap.grabWindow(desktop.winId(), x=-screen3, width=screen3).save('pictures/' + filename, 'jpg')
    elif screen_id == 2:
        QPixmap.grabWindow(QApplication.desktop().winId()).save('pictures/' + filename, 'jpg')
    else:
        QPixmap.grabWindow(desktop.winId(), x=screen2).save('pictures/' + filename, 'jpg')
        
    
if __name__ == '__main__':

    if sys.executable.endswith('pythonw.exe'):
        sys.stdout = open(os.devnull, 'w');
        sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-'+os.path.basename(sys.argv[0])), 'w')

    keyboard.add_abbreviation('tsm', 'Team Solo Mid')
    keyboard.add_hotkey('alt+shift+1', save_screen, args=[1])
    keyboard.add_hotkey('alt+shift+2', save_screen, args=[2])
    keyboard.add_hotkey('alt+shift+3', save_screen, args=[3])
    print('starting to wait')
    keyboard.wait('alt+shift+q')
