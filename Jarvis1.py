import cv2
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition  as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import pyautogui #pip install pyautogui
import os# import music #pip install music
import random
import instaloader
from datetime import date
import json
from requests import get
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import requests
import subprocess
from urllib.request import urlopen
import wolframalpha #pip install wolframalpha
import time
import pywhatkit #pip install pywhatkit
import PyPDF2
import rotatescreen
import operator
import warnings
from PIL import ImageGrab
import  numpy as np
import winshell
import  win32api
from win32api import GetSystemMetrics
from email.mime import audio
from JarvisMainUi import Ui_Form
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import speedtest

####################  For GUI   #####################################
## `"PyQt5"` is a module that can be used to create graphical user interfaces (GUI).
## and the use of pyqt5 --tool is done as Qt Designer
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
################################################################


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

warnings.filterwarnings("ignore")
engine = pyttsx3.init('sapi5') #to take voice & search in google
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

geocoder_api_id = "da1ad89d7d8c4ba980de65c892cb7e2a"
wolframalpha_app_id = "XQ3763-JGQJTT9AK8"







def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p") #for 24 hrs clock
    speak("The current time is...")
    speak(Time)

def  date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current Date is..")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    speak("Welcome Back Sir!")
    # time_()
    # date_()

    #greetings

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morining Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    
    
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")


def computational_intelligence(question):
        try:
            client = wolframalpha.Client(wolframalpha_app_id)
            answer = client.query(question)
            answer = next(answer.results).text
            print(answer)
            return answer
        except:
            speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
            return None



def join_meet():
    
    opt = Options()

    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")

    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(chrome_options= opt, executable_path='C:\\Users\\Yash\\Desktop\\AI-Assistant\\chromedriver.exe')

    driver.get('https://accounts.google.com/')

    username=driver.find_element_by_id('identifierId')
    username.click()
    username.send_keys('e367117@gmail.com')


    next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
    next.click()
    time.sleep(5)
    password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.click()
    password.send_keys('pbl meet 2021')

    next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
    next.click()
    time.sleep(5)


    driver.get('https://meet.google.com/osm-isnj-pxh')

    time.sleep(5)

    camera = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div/span')
    camera.click()

    time.sleep(5)

    mic = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span')
    mic.click()

    time.sleep(5)

    join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
    join.click()


    
        

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def TakeCommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 0.7
            audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(query)

        except  Exception as e:
            print(e)
            print("Say that again please..")
            speak("Say that again please..")
            return "None"
        return query


    def screenshot(self):
            img = pyautogui.screenshot()
            time_stamp = datetime.datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
            file_name = f'C:\\Users\\Yash\\Desktop\\AI-Assistant\\AI-Screenshots\\{time_stamp}.png'
            img.save(file_name)
        
    def  cpu(self):
        usage = str(psutil.cpu_percent())
        speak("CPU is at" + usage)
        battery = psutil.sensors_battery()
        speak("Battery is at")
        speak(battery.percent)
        
    def joke(self):
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    def whatsapp_msg(self):
        
        speak("Can you please enter phone number of the person to whom you want to send message?")
        phone_no = input("Enter phone number: +91 ")

        phone_no = "+91" + str(phone_no)

        print(phone_no)

        speak("What message do you want to send?")
        msg = TakeCommand()
        print(msg)

        speak("When you want to send message (Now or Later)")
        print("When you want to send message (Now / Later)")

        msg_send_time = TakeCommand()

        if msg_send_time == "now":
            pywhatkit.sendwhatmsg_instantly(phone_no, msg, 15)

        else:
            speak("Enter the time when you want to send the message")
            speak("First Enter the time in hour")
            time_h = int(input("First Enter the time in hour: "))
            speak("Now Enter the time in minutes")
            time_m = int(input("Now Enter the time in minutes: "))

            pywhatkit.sendwhatmsg(phone_no, msg, time_h, time_m, 15)


        speak("Sending the message")
        print("Successfully Sent!")
        speak("Successfully Sent!")

    def pdfreader(self):
        speak("Opening Core Java Fundamentals Book...")
        book = open('C:\\Users\\Yash\\Desktop\\Books\\CoreJavaFunda.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(f"There are total {pages} pages.")
        speak(f"There are total {pages} pages.")
        pg = int(input("Please enter the page number i have to read : "))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        print(text)
        speak(text)


    # def secret_capture(self):
        
    #     width = GetSystemMetrics(0)
    #     height = GetSystemMetrics(1)
    #     time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     file_name = (f'C:\\Users\\Yash\\Desktop\\AI-Assistant\\AI-ScreenRecordings\\{time_stamp}.mp4')
    #     fps = 60.0
    #     fourcc = cv2.VideoWriter_fourcc(*"XVID")
    #     vid_capture = cv2.VideoWriter(file_name, fourcc, fps, (width, height))
    #     cv2.namedWindow("◉ Recording", cv2.WINDOW_NORMAL)

    #     while True:
    #         img = pyautogui.screenshot()
    #         frame = np.array(img)
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         vid_capture.write(frame)
    #         cv2.imshow("◉ Recording", frame)
    #         if cv2.waitKey(10) == ord('q'):
    #             break



        # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')#this is for encoding video captured
        # captured_vid = cv2.VideoWriter(file_name, fourcc , 20.0, (width, height))
        # while True:
        #     img = pyautogui.screenshot()
        #     img = ImageGrab.grab(bbox=(0, 0, width, height))
        #     img_np =  np.array(img)
        #     img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        #     captured_vid.write(img_final)
        #     cv2.imshow('Secret Capture', img_final)
        #     # cv2.imshow('webcam', img_final)
        #     if cv2.waitKey(10) == ord('q'):
        #         speak("Screen Recording is been stopped!")
        #         break
        # vid_capture.release()
        # cv2.destroyAllWindows()
        

    def rotate_screen(self):
        screen = rotatescreen.get_primary_display()
        # screen.rotate_to(0)
        for i in range(13):
            time.sleep(1)
            screen.rotate_to(i*90 % 360)

    def phnumbers(self):

        speak("Enter phone number to track")
        number = input("Enter phone number: +91 ")
        number = "+91" + str(number)
        your_location = phonenumbers.parse(number, "CH")
        
        geocoder = OpenCageGeocode(geocoder_api_id)
        speak(f"User Location is {geocoder.description_for_number(your_location, 'en')}") 
        print(geocoder.description_for_number(your_location, "en"))
        service_provider = phonenumbers.parse(number)
        print(carrier.name_for_number(service_provider, "en"))
        speak(f"Service Provider is {carrier.name_for_number(service_provider, 'en ')}" )


        
        query1 = str(your_location)
        results = geocoder.geocode(query1)
        print(results)

 
    def TaskExecution(self):
    
        wishme()

        while True:
            
            self.query = self.TakeCommand().lower()
            #All the commands will be stroed in lower case in query
            #for easy recognotion
            
            if 'time' in self.query: #tells us time when asked
                time_()
            elif 'date' in self.query: #tells us date when asked
                date_()

            elif 'increase volume' in self.query:
                    speak("Increasing Volume..")
                    for i in range(5):
                        pyautogui.press('volumeup')
            elif 'decrease volume' in self.query:
                    speak("Decreasing Volume..")
                    for i in range(5):
                        pyautogui.press('volumedown')
            elif 'mute' in self.query:
                    speak("Muting...")
                    pyautogui.press('m')
            
            # Mute Yourself
            elif 'mute yourself' in self.query:
                    speak("Muting myself Sir..")
                    pyautogui.password('mute')

            elif 'unmute' in self.query:
                    speak("Unmuting...")
                    pyautogui.press('m')
            
            elif 'meet' in self.query:
                    join_meet()
            

            
            
            elif 'internet speed' in self.query:
                speak("Checking speed...")
                speed = speedtest.Speedtest()
                downloading = speed.download()
                correctDown = int(downloading/800000)
                uploading = speed.upload()
                correctUp = int(uploading/800000)
                print(f"The Downloading speed is {correctDown} mbp s And The Uploading speed is {correctUp} mbp s" )
                speak(f"The Downloading speed is {correctDown} mbp s And The Uploading speed is {correctUp} mbp s" )
                
        
            elif 'wikipedia' in self.query:
                speak("Searching...")
            
                self.query = self.query.replace("wikipedia", "")
                #query=query.replace('wikipedia','')
                result = wikipedia.summary(query, sentences=4)
                speak("According to wikipedia..")
                print(result)
                speak(result)

            elif 'empty recycle bin' in self.query:
                speak("Are you sure you want to empty recycle bin?")
                ans = self.TakeCommand()
                if 'yes' in ans:
                    speak("Emptying the recycle bin...")
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                if 'no' in ans:
                    speak("Okay Sir, I am not Emptying recycle bin")
                    
            
            elif 'track mobile location' in self.query:
                # speak("Searching...")
                phnumbers()
            
            elif 'screen recording' in self.query:
                speak("Starting Screen Recording")
                # secret_capture()
                #  importing the required packages
                import pyautogui
                import cv2
                import numpy as np

                # Specify resolution
                resolution = (1920, 1080)
                # Specify video codec
                codec = cv2.VideoWriter_fourcc(*"XVID")
                # Specify name of Output file
                time_stamp = datetime.datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
                file_name = f"C:\\Users\\Yash\\Desktop\\AI-Assistant\\AI-ScreenRecordings\\Recording {time_stamp}.avi"
                # filename = "Recording.avi"
                # Specify frames rate. We can choose any
                # value and experiment with it
                fps = 60.0
                # Creating a VideoWriter object
                out = cv2.VideoWriter(file_name, codec, fps, resolution)
                # Create an Empty window
                cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
                # Resize this window
                cv2.resizeWindow("Live", 480, 270)
                while True:
                    # Take screenshot using PyAutoGUI
                    img = pyautogui.screenshot()
                    # Convert the screenshot to a numpy array
                    frame = np.array(img)
                    # Convert it from BGR(Blue, Green, Red) to
                    # RGB(Red, Green, Blue)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # Write it to the output file
                    out.write(frame)
                    # Optional: Display the recording screen
                    cv2.imshow('Live', frame)
                    # Stop recording when we press 'q'
                    if cv2.waitKey(1) == ord('q'):
                        break
                # Release the Video writer
                out.release()
                # Destroy all windows
                cv2.destroyAllWindows()


            elif 'rotate screen' in self.query:
                speak("Rotating...")
                rotate_screen()
                speak("Enjoyed this cool stuff?")
                ans = self.TakeCommand()
                if  'yes' in ans:
                    speak("Always ready to swing your mood")
                else:
                    continue
                
            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    mail_content = self.TakeCommand()
                    sender_address = 'e367117@gmail.com'
                    sender_pass = 'pbl meet 2021'
                    speak("Who is the Reciever..")
                    receiver_address=input("Enter Reciever's Email ID:")
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    speak("Do you want to write a subject for sending email?")
                    ans = self.TakeCommand()
                    if  'yes' in ans:
                        subject_msg = self.TakeCommand()
                    if 'no' in ans:
                        subject_msg = None
                    message['Subject'] = subject_msg
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    # message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    speak(mail_content)
                    session.quit()
                    
                    speak("Email has been sent succesfully...")

                except  Exception as e:
                    print(e)
                    speak(" Sorry, Unable to send Email...")
            
        

            elif 'open google' in self.query:
                speak("What should I search?")
                search_Term = self.TakeCommand().lower()
                speak("Opening google..")
                print("Opening google..")
                wb.open('https://www.google.com/search?q='+search_Term)

            elif 'open youtube' in self.query:
                speak("What should I search?")
                search_Term = self.TakeCommand().lower()
                speak("Here we go to YOUTUBE!")
                wb.open('https://youtube.com/results?search_query=' +search_Term)
                
            
            elif 'open stack overflow' in self.query:
                speak("What should I search In Stack Overflow?")
                search_Term = self.TakeCommand().lower()
                print("Opening Stack Overflow..")
                wb.open('https://stackoverflow.com/search?q=' +search_Term)
                
            elif 'whatsapp message' in self.query:
                whatsapp_msg()
            
            elif  'read book' in self.query:
                pdfreader()
            
            elif 'joke' in self.query:
                joke()
                
            elif 'go offline' in self.query:
                speak("Going offline Sir!! have a good day... :)")
                quit()
                
            elif 'ms word' in self.query:
                speak("Opening MS Word...")
                ms_word = r'E:\Word'
                os.startfile(ms_word)
                
            elif 'write a note' in self.query:
                speak("What should I write,Sir?")
                notes = self.TakeCommand()
                file = open('notes.txt', 'w')
                speak("Sir Should I add Date  and Time?")
                ans = self.TakeCommand()
                if 'yes' in ans  or 'sure' in ans:
                    strTime = datetime.datetime.now().strftime("%I:%M:%S")
                    file.write(strTime)
                    file.write(':-')
                    file.write(notes)
                    speak("Done Taking Notes, Sir!")
                else:
                    file.write(notes)
                    
            elif 'show notes' in self.query:
                speak("showing notes")
                file = open('notes.txt' , 'r')
                print(file.read())
                speak(file.read())
                
            elif 'screenshot' in self.query:
                speak("Taking Screenshot...")
                screenshot()
                speak("Screenshot is been taken")
                
            elif 'play movie' in self.query:
                movie_dir= "E:/Test movies"
                movie = os.listdir(movie_dir)
                speak("Which movie should I play?")
                speak("Select a number or say 'random'")
                ans =  self.TakeCommand().lower()
                if 'number' in ans:
                    no = int(ans.replace('number',''))
                elif 'random' in ans:
                    no = random.randint(1,10)
                os.startfile(os.path.join(movie_dir, movie[no]))
                
                
            elif 'thank you' in self.query:
                speak("Welcome, Sir!")
                
            elif  'remember that' in self.query:
                speak("What should I remember?")
                memory = self.TakeCommand()
                speak("You asked to remember " +memory)
                remember = open('memory.txt', 'w')
                remember.write(memory)
                remember.close()
                
            elif 'do you remember anything' in self.query:
                remember = open('memory.txt', 'r')
                speak("You asked me to remember " +remember.read())
                
            elif  'very good' in self.query:
                speak("Thank You Sir!:-)")    
                
            elif 'where is' in self.query:
                self.query= query.replace("where is", "")
                location = self.query
                speak("User asked to locate" + location)
                wb.open_new_tab("https://www.google.com/maps/place/" +location)
                
            elif 'news' in self.query:
                try:
                    jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=b215f9c99b1448159bfec166ffc88898")
                    data = json.load(jsonObj)
                    i = 1
                    
                    speak('Here are some top headlines')
                    print('***************TOP HEADLINES***************'+'\n')
                    for item in data["articles"]:
                        print(str(i)+". "+item["title"]+"\n")
                        print(item["description"]+"\n")
                        speak(item["title"])
                        speak(item["description"])
                        
                        if i == 3:
                            break
                        i += 1
                        
                except Exception as  e:
                    print(str(e))
                    
            elif "calculate" in self.query:
                    question = self.query
                    answer = computational_intelligence(question)
                    speak(answer)
            
                
                
            elif 'spotify' in self.query:
                speak("Opening Spotify...")
                spoti = r'E:\Spotify'   
                os.startfile(spoti)
            elif 'play' in self.query:
                pyautogui.press('space')

            # Pause
            elif 'pause' in self.query:
                pyautogui.press('space')

            # Forward and Backward
            elif 'next' in self.query:
                pyautogui.keyDown('shift')
                pyautogui.press('n')
                pyautogui.keyUp('shift')

            elif 'previous' in self.query:
                pyautogui.keyDown('shift')
                pyautogui.press('p')
                pyautogui.keyUp('shift')

                
            elif  'what is' in self.query :
                #use the same API key that we generated erlier i.e wolframalpha
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(self.query)
                
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No Results")
                    
            elif 'stop listening' in self.query:
                speak("For how many seconds you want me to stop listening to your command?")
                ans = int(self.TakeCommand())
                time.sleep(ans)
                print(ans)
                
            elif 'log out' in self.query:
                os.system("shutdown -1")



            elif 'restart' in self.query:
                speak("Are you sure, you want me to restart your laptop?")
                ans = self.TakeCommand()
                if 'yes' in ans:
                    print(ans)
                    os.system("shutdown /r /t 1")
                if 'no' in ans:
                    speak("Okay not restarting")



            elif 'shutdown' in self.query:
                speak("Are you sure, you want me to shutdown your laptop?")
                ans = self.TakeCommand()
                if 'yes' in ans:
                    print(ans)
                    os.system("shutdown /s /t 1" )
                if 'no' in ans:
                    speak("Okay not shutting down")
            elif  'who is' in self.query:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(self.query)
                
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No Results")

            elif 'tempreature' in self.query:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(self.query)
                
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No Results")
        

            elif "ip address" in self.query:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    speak(f"Your ip address is {ip}")
            elif "where i am" in self.query or "where we are" in self.query:
                    speak("wait sir, let me check")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        print(geo_data)
                        city = geo_data['city']
                        # state = geo_data['state']
                        country = geo_data['country']
                        print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                        speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    except Exception as e:
                        speak("sorry sir, Due to network issue i am not able to find where we are.")
                        pass
            
            elif "open camera" in self.query:
                    speak("Opening Camera...")
                    speak("Sir, Please make sure that you give a good smile ...")
                    speak("orelse I won't click your picture")
                    cap = cv2.VideoCapture(0)
                    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
                    while True:
                        for i in range(1):
                            _, frame = cap.read()
                            original_frame = frame.copy()
                            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            face = face_cascade.detectMultiScale(gray, 1.3, 5)
                            for x, y, w, h in face:
                                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                                face_roi = frame[y:y+h, x:x+w]
                                gray_roi = gray[y:y+h, x:x+w]
                                smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
                                for x1, y1, w1, h1 in smile:
                                    cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                                    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                                    file_name = f'C:\\Users\\Yash\\Desktop\\AI-Assistant\\AI-Selfie\\selfie-{time_stamp}.png'
                                    cv2.imwrite(file_name, original_frame)
                            cv2.imshow('Camera', frame)
                        if cv2.waitKey(10) == ord('q'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()

            elif "instagram profile" in  self.query or "profile on instagram" in self.query:
                    speak("sir please enter the user name correctly.")
                    name = input("Enter username here: ")
                    wb.open(f"www.instagram.com/{name}")
                    speak(f"Sir here is the profile of the user {name}")
                    time.sleep(5)
                    speak("sir would you like to download profile picture of this account.")
                    condition = self.TakeCommand()
                    if "yes" in condition:
                        mod = instaloader.Instaloader() #pip install instadownloader
                        mod.download_profile(name, profile_pic_only=True)
                        speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                    else:
                        pass 

            elif "open notepad" in self.query:
                    speak("Opening notepad")
                    npath = "C:\\Users\\Yash\\Desktop\\Notepad"
                    os.startfile(npath)
            elif "close notepad" in self.query:
                    speak("okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")


            elif "open adobe reader" in self.query:
                speak("Opening adobe reader")
                apath = "C:\\Users\\Public\\Desktop\\Acrobat Reader DC"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                    speak("Opening command prompt")
                    os.system("start cmd")     

            elif 'switch the window' in self.query:
                    speak("Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")      
                
        
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:  
                speak("If you are asking if I'm committed to you , the answer is 'absolutely!'")
    
            elif "how are you" in self.query:
                speak("I'm fine, thank you for asking. This is a challenging time for us. I hope you and your loved ones are staying safe and healthy.")
    
            elif "i love you" in self.query:
                speak("Really? You love me? This is the best day.")





startExecution = MainThread()
# FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./JarvisMain.ui"))
class Main(QMainWindow, QProcess):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Jarvis")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTasks)
        self.ui.pushButton_2.clicked.connect(self.close)
        
        
        
    def startTasks(self):


        self.ui.movie = QtGui.QMovie("./GIF/artificial_intelligence_product_rokid.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        self.ui.movie = QtGui.QMovie("./GIF/body.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        self.ui.movie = QtGui.QMovie("./GIF/MetallicEarth.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        self.ui.movie = QtGui.QMovie("./GIF/game.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        self.ui.movie = QtGui.QMovie("./GIF/T8bahf.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("./GIF/examplee.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("./GIF/taksd.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("./GIF/faceman.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        startExecution.start()
    

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

    def showText(self):
        self.ui.textBrowser_3.setText(self.query)

        



            

    
app = QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())








