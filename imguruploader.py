import keyboard
import os
import pyimgur
import pyperclip
import sys
from PyQt4.QtGui import QPixmap, QApplication
from PyQt4.QtCore import QObject, SIGNAL
from datetime import datetime
from config import CLIENT_ID


app = QApplication(sys.argv)
desktop = app.desktop()



def detect_screens(desktop):
    
    screen_count = desktop.screenCount()
    screen_geos = [desktop.screenGeometry(i) for i in range(screen_count)]
    screen_geos.sort(key=lambda screen: screen.left())
    return screen_geos


def detect_screen_count_change():

    screen_count = desktop.screenCount()
    with open('screen_count.txt', 'a') as f:
        f.write('Screen Count: {}\n'.format(screen_count))


def save_screen(screen_id):

    if screen_id > desktop.screenCount():
        return
    
    date = datetime.now()
    filename = date.strftime('%m-%d-%Y_%Hh-%Mm-%Ss.jpg')

    im = pyimgur.Imgur(CLIENT_ID)
    
    screen = detect_screens(desktop)[screen_id - 1] 
    picture = QPixmap.grabWindow(desktop.winId(), x=screen.x(), y=screen.y(),
                                 width=screen.width(), height=screen.height())
    success = picture.save('pictures/' + filename, 'jpg')
    
    if success:
        uploaded_image = im.upload_image('pictures/' + filename, title='Thowaway Title')
        link = uploaded_image.link
        pyperclip.copy(link)
        
        with open('link_log.txt', 'a') as f:
            f.write(filename + ' --> ' + link + '\n')
        
    else:
        with open('link_log.txt', 'a') as f:
            f.write(filename + ' --> failure\n')
        
    
if __name__ == '__main__':

    if sys.executable.endswith('pythonw.exe'):
        sys.stdout = open(os.devnull, 'w');
        sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-'+os.path.basename(sys.argv[0])), 'w')

    QObject.connect(desktop, SIGNAL('screenCountChanged()'), detect_screen_count_change)

    for i in range(1, desktop.screenCount() + 1):
        keyboard.add_hotkey('alt+shift+{}'.format(i), save_screen, args=[i])
         
    keyboard.wait('alt+shift+q')
