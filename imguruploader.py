import keyboard
import os
import pyimgur
import pyperclip
import sys
from PyQt4.QtGui import QPixmap, QApplication
from datetime import datetime
from config import CLIENT_ID


def detect_screens(desktop):
    
    screen_count = desktop.screenCount()

    SCREEN_COUNT = screen_count
    
    screen_geos = [desktop.screenGeometry(i) for i in range(screen_count)]
    screen_geos.sort(key=lambda screen: screen.left())
    return screen_geos
    

def save_screen(screen_id):
    
    date = datetime.now()
    filename = date.strftime('%m-%d-%Y_%Hh-%Mm-%Ss.jpg')
    
    app = QApplication(sys.argv)
    desktop = app.desktop()

    im = pyimgur.Imgur(CLIENT_ID)

    '''---------------
    screen1width = desktop.screenGeometry(0).width()
    screen2width = desktop.screenGeometry(1).width()
    screen3width = desktop.screenGeometry(2).width()

    if screen_id == 1:
        QPixmap.grabWindow(desktop.winId(), x=-screen3width, width=screen3width).save('pictures/' + filename, 'jpg')
    elif screen_id == 2:
        QPixmap.grabWindow(QApplication.desktop().winId()).save('pictures/' + filename, 'jpg')
    else:
        QPixmap.grabWindow(desktop.winId(), x=screen2width).save('pictures/' + filename, 'jpg')
    -----------------'''
    screen_widget = desktop.screen()
    screens = detect_screens(desktop)

    print('screen_id: {}'.format(screen_id))
    print('screen geo: {}'.format(screens[screen_id - 1]))
    
    picture = QPixmap.grabWidget(screen_widget, screens[screen_id - 1])
    print(picture)
    success = picture.save('pictures/' + filename, 'jpg')
    if success:
        print('it succeeded')
    else:
        print('it failed')

    '''uploaded_image = im.upload_image('pictures/' + filename, title='Thowaway Title')
    link = uploaded_image.link

    pyperclip.copy(link)
    with open('link_log.txt', 'a') as f:
        f.write(filename + ' --> ' + link + '\n')'''
        
    
if __name__ == '__main__':

    if sys.executable.endswith('pythonw.exe'):
        sys.stdout = open(os.devnull, 'w');
        sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-'+os.path.basename(sys.argv[0])), 'w')

   
    keyboard.add_hotkey('alt+shift+1', save_screen, args=[1])
    keyboard.add_hotkey('alt+shift+2', save_screen, args=[2])
    keyboard.add_hotkey('alt+shift+3', save_screen, args=[3])
    '''----------
    app = QApplication(sys.argv)
    desktop = app.desktop()
    screen_count = desktop.screenCount()

    for i in range(1, screen_count + 1):
        print('screens: {}'.format(screen_count))
        print('added screen {} to hotkeys'.format(i))
        keyboard.add_hotkey('alt+shift+{}'.format(i), save_screen, args=[i])
        -----------'''
    
    keyboard.wait('alt+shift+q')
