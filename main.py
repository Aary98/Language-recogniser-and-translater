import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import*
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import speech_recognition as sr
# pip install pyaudio speech_recognition seleniu pyts3


class WebClass(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.showMaximized()
        self.setWindowIcon(QIcon('"img-55.png"'))
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl('https://google.com'))
        self.menu = QToolBar()
        self.addToolBar(self.menu)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setShortcut(QKeySequence("Ctrl+B"))
        self.menu.addAction(back_btn)

        next_btn = QAction('Next', self)
        next_btn.triggered.connect(self.browser.forward)
        next_btn.setShortcut(QKeySequence("Ctrl+F"))
        self.menu.addAction(next_btn)

        reload_btn = QAction('Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setShortcut(QKeySequence("Ctrl+R"))
        self.menu.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.home_url)
        home_btn.setShortcut(QKeySequence("Ctrl+H"))
        self.menu.addAction(home_btn)

        zoom_in_btn = QAction('Zoom In', self)
        zoom_in_btn.triggered.connect(self.zoom_in)
        zoom_in_btn.setShortcut(QKeySequence("Ctrl+"))
        self.menu.addAction(zoom_in_btn)

        zoom_out_btn = QAction('Zoom Out', self)
        zoom_out_btn.triggered.connect(self.zoom_out)
        zoom_out_btn.setShortcut(QKeySequence("Ctrl+-"))
        self.menu.addAction(zoom_out_btn)

        find_btn = QAction('Find in Page', self)
        find_btn.triggered.connect(self.find_in_page)
        find_btn.setShortcut(QKeySequence("Ctrl+Shift+F"))
        self.menu.addAction(find_btn)

        mic_btn = QAction(QIcon('mic.png'), 'Voice Input', self)
        mic_btn.triggered.connect(self.voice_control)
        mic_btn.setShortcut(QKeySequence("Ctrl+V"))
        self.menu.addAction(mic_btn)

        self.find_txt = QLineEdit()
        self.find_txt.returnPressed.connect(self.find_in_page)
        self.menu.addWidget(self.find_txt)
        self.url_txt = QLineEdit()
        self.url_txt.returnPressed.connect(self.navigate_url)
        self.menu.addWidget(self.url_txt)
        self.browser.urlChanged.connect(self.update_url)

        self.recognizer = sr.Recognizer()


    def home_url(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_url(self):
        self.browser.setUrl(QUrl(self.url_txt.text()))

    def update_url(self, u):
        self.url_txt.setText(u.toString())

    def find_in_page(self):
        text = self.find_txt.text()
        self.browser.findText(text)

    def zoom_in(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def zoom_out(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def voice_control(self):
        with sr.Microphone() as source:
            print("Speak now...")
            audio = self.recognizer.listen(source,timeout=2)

        try:
            # recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(audio)
            print("You said: ", text)

            if "back" in text:
                self.browser.back()
            elif "forward" in text:
                self.browser.forward()
            elif "reload" in text:
                self.browser.reload()
            elif "home" in text:
                self.home_url()
            else:
                self.browser.setUrl(
                    QUrl('https://www.google.com/search?q=' + text))

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



WebApp = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser - Devloped By Arun_More")
obj = WebClass()
obj.show()
obj.voice_control() # call the voice control function
WebApp.exec_()