import sys
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os
import webbrowser
from feature import takeCommand
from inner import Ui_Form


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# terminalUi.terminalPrint(voices[1].id)
state=None
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning boss..")
        ui.terminalPrint("Good morning boss..")
    elif hour>=12 and hour<=18:
        speak("good afternoon boss")
        ui.terminalPrint("good afternoon boss")
    else:
        speak("good evening boss ")
        ui.terminalPrint("good evening boss")
    ui.terminalPrint("")
    speak(" how may i assist you today")  
    ui.terminalPrint(" how may i assist you today")  


class assistantMainClass(QThread):
    def __init__(self):
        super(assistantMainClass,self).__init__()  
    def run(self):
        self.runAssistant()
       

    def speechrecognition(self):
     while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("listening..")
            r.pause_threshold=0.8
            audio=r.listen(source)
        try:
           ui.terminalPrint("Recognizing..")
           query = r.recognize_google(audio,language="en-in")     
           ui.terminalPrint(f"you said: {query}\n")
           

        #    speak(self.query)
        except Exception as e:
            ui.terminalPrint("say it again boss")
            speak("say it again boss")
            return None
        return query
    
    def runAssistant(self):
        obj=takeCommand()
        wishMe()
        while True:
          self.user_command = self.speechrecognition()  # Call the function from the other file
          obj.execute_command(self.user_command)
       
startRunning=assistantMainClass()
class assistantGui(QWidget):
    def __init__(self):
        super(assistantGui,self).__init__()
        self.Ui= Ui_Form()
        self.Ui.setupUi(self)   
        self.Ui.exit.clicked.connect(self.close)
        self.Ui.pushButton.clicked.connect(self.commandFromTerminal)
        self.Ui.movie=QtGui.QMovie("E:\\myWorks\\voiceAssistantCode\\images\\image_processing20200610-21965-29u8be.gif")
        self.Ui.label.setMovie(self.Ui.movie)
        self.Ui.movie.start()      
       
        startRunning.start()

    def terminalPrint(self,text):
        self.Ui.textTerminal.appendPlainText(f"optimus:{text}")   

    def commandFromTerminal(self):
        cmd=self.Ui.lineEdit.text()   
        if cmd:
            self.Ui.lineEdit.clear() 
            self.Ui.textTerminal.appendPlainText(f"you typed:{cmd}") 

            if cmd == 'exit':
                ui.close()
            elif cmd == 'help':
                self.terminalPrint("I CAN PERFORM VARIOUS TASK WHICH IS PROGRAM INSIDE ME..\n"
                                   "LIKE: TIME,WEATHER,OPENING WINDOWS APPLICATIONS,OPENING WEB SITE" )
                speak("I CAN PERFORM VARIOUS TASK WHICH IS PROGRAM INSIDE ME..\n"
                                   "LIKE: TIME  ,WEATHER  ,OPENING  WINDOWS APPLICATIONS  ,OPENING WEB SITES")
            elif cmd == "what is the time":
                strtime=datetime.datetime.now().strftime('%H:%M:%S')
                speak(strtime)
                ui.terminalPrint(strtime)
            elif cmd == "open youtube":
                webbrowser.open("https://www.youtube.com/")
                ui.terminalPrint("opening you tube")
                speak("opening you tube")
            elif cmd =="open chatGpt":
                webbrowser.open("https://chat.openai.com/")
                ui.terminalPrint("opening chatgpt")
                speak("opening chat gpt")
            elif cmd =="open note pad":
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories")
                ui.terminalPrint("opening notepad")
                speak("opening notepad")
            
            
            else:

                pass
        else:
            pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=assistantGui()
    ui.show()
    sys.exit(app.exec_())
   
