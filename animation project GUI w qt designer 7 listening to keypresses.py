# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testQt5App2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


            #Done by Zoltan Toma Middlesex Univesity M00670384

from PyQt5 import QtCore, QtGui, QtWidgets          #GUI library
from time import sleep                              #need sleep function from time library to control time between LED changes
import opc          
import numpy
import colorsys
import random
import webbrowser
import sys, string, os
import threading                                    #this library helps running the animation on a separate thread because the GUI is a loop and otherwise it would crash
from pynput.keyboard import Listener,Key,Controller

#os.system("readopcForStrands.exe")                 #run Simultor.exe, which has to be in same folder
client = opc.Client('localhost:7890')               #rgb led address to send the Send pixels forever at 30 frames per second
run_once=0                                          #need this to start the keypresslistener just once and afte chango to 1
stop=0                                              #animations will keep checking on this variable and keep running until it is 0

class Ui_MainWindow(object):                        #GUI created with using QT5 Designer
    def setupUi(self, MainWindow):        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonBouncyBall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBouncyBall.setGeometry(QtCore.QRect(60, 70, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBouncyBall.setFont(font)
        self.pushButtonBouncyBall.setObjectName("pushButtonBouncyBall")
        self.pushButtonFlashingStar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFlashingStar.setGeometry(QtCore.QRect(60, 120, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFlashingStar.setFont(font)
        self.pushButtonFlashingStar.setObjectName("pushButtonFlashingStar")
        self.pushButtonRainbow1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRainbow1.setGeometry(QtCore.QRect(60, 170, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRainbow1.setFont(font)
        self.pushButtonRainbow1.setObjectName("pushButtonRainbow1")
        self.pushButtonArrow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonArrow.setGeometry(QtCore.QRect(60, 270, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonArrow.setFont(font)
        self.pushButtonArrow.setObjectName("pushButtonArrow")
        self.Hellolabel = QtWidgets.QLabel(self.centralwidget)
        self.Hellolabel.setGeometry(QtCore.QRect(10, -20, 591, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Hellolabel.setFont(font)
        self.Hellolabel.setScaledContents(True)
        self.Hellolabel.setObjectName("Hellolabel")
        self.pushButtonRainbow2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRainbow2.setGeometry(QtCore.QRect(60, 220, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRainbow2.setFont(font)
        self.pushButtonRainbow2.setObjectName("pushButtonRainbow2")
        self.pushButtonSnake = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSnake.setGeometry(QtCore.QRect(60, 330, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSnake.setFont(font)
        self.pushButtonSnake.setObjectName("pushButtonSnake")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(189, 70, 61, 281))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(250, 120, 331, 161))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("MDX-logo-dark.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 171, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 60, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun_Simulator = QtWidgets.QMenu(self.menubar)
        self.menuRun_Simulator.setObjectName("menuRun_Simulator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit_App = QtWidgets.QAction(MainWindow)
        self.actionExit_App.setObjectName("actionExit_App")
        self.actionGo = QtWidgets.QAction(MainWindow)
        self.actionGo.setObjectName("actionGo")
        self.menuFile.addAction(self.actionExit_App)
        self.menuRun_Simulator.addAction(self.actionGo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun_Simulator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonFlashingStar.clicked.connect(lambda:self.startTheThread(self.star))  #here I say what happens at button presses
        self.pushButtonRainbow1.clicked.connect(lambda:self.startTheThread(self.rainbow_1)) #I call function with argument to call function
        self.pushButtonRainbow2.clicked.connect(lambda:self.startTheThread(self.rainbow_2))
        self.pushButtonBouncyBall.clicked.connect(lambda:self.startTheThread(self.bouncy_ball))
        self.pushButtonArrow.clicked.connect(lambda:self.startTheThread(self.arrow))
        self.actionGo.triggered.connect(lambda:self.startTheThread(self.runSimulator))
        self.actionExit_App.triggered.connect(lambda:self.startTheThread(self.exitApp))
        self.pushButton.clicked.connect(lambda:self.startTheThread(self.stopIt))        
        self.pushButton_2.clicked.connect(lambda:self.startTheThread(self.link))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animations"))
        self.pushButtonBouncyBall.setText(_translate("MainWindow", "Bouncy Ball"))
        self.pushButtonFlashingStar.setText(_translate("MainWindow", "Flashing Star"))
        self.pushButtonRainbow1.setText(_translate("MainWindow", "Rainbow1"))
        self.pushButtonArrow.setText(_translate("MainWindow", "Arrow"))
        self.Hellolabel.setText(_translate("MainWindow", "Hello, thank you for using my LED Animation App"))
        self.pushButtonRainbow2.setText(_translate("MainWindow", "Rainbow2"))
        self.pushButtonSnake.setText(_translate("MainWindow", "Snake"))
        self.pushButton.setText(_translate("MainWindow", "STOP ANIMATION"))
        self.pushButton_2.setText(_translate("MainWindow", "Instagram "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRun_Simulator.setTitle(_translate("MainWindow", "Run Simulator"))
        self.actionExit_App.setText(_translate("MainWindow", "Exit App"))
        self.actionGo.setText(_translate("MainWindow", "Go"))

    def runSimulator(self):
        os.system("readopcForStrands.exe")              #run Simultor.exe, which has to be in same folder

    def startTheThread(self, function):                 #runs the chosen function from the argument on a separate thread
        global stop                                     #if i call this function than it is likely I started an animation so I set stop back to 0
        stop = 0
        self.t = threading.Thread(target = function)    #make t a thread and run it with the start command
        self.t.start()                                  #to wait for thread to be finished: t.join()

    def exitApp(self):                                  #exit works but the pop up window is displayed behind main window, not sure ghow to fix it yet
        print("exit triggered")
        exit(self)

    def stopIt(self):                                   #stops animation
        print("stop is True")
        global stop
        stop = 1
    
    def link(self):
        webbrowser.open('https://www.instagram.com/vakondzoli/?igshid=10wvgrmcr1nwk')#this function opens weblinks

    def star(self):                                     #animation of a star poping up randomly    
        while True:                                     #endless loop unless stop=1
            if stop==1:                                 #break while loop
                break
            sleep(1)                                    #every 1 seca star disappears and a new one appears somewhere elese
            nr = random.randint(0,359)                  #generate random number to determine star position
            star_list=[nr, nr+1, nr-1, nr+60, nr-60]    #the list that contains the 5 LEDs taht make the star
            led_colour=[(0,255,255)]*360                #all LED  color
            client.put_pixels(led_colour)               #turn them to taht color now
            for i in star_list:                         #this for loop to make sure the star is not outside the screen
                if i <0:
                    i=i+360
                if i>359:
                    i=i-360
                led_colour[i]=(255,0,0)           
                client.put_pixels(led_colour)           #send list of rgb colors to client (simulator)        

    def bouncy_ball(self):
        arrow_list=[2,3,61,62,63,64,120,121,124,125,180,181,184,185,241,242,243,244,302,303]    #the led numbers in round shape representing a ball
        t=0.001                                 #start time between loops
        t_change=0.00008                          #slowing per loop (adds to the time between loops)
        direction=1                             #moving beck and forth by 1 led positoion
        counter=0
        green = 245, 235, 24                   #rgb code for gree stored in variable named green (https://www.w3schools.com/colors/colors_picker.asp)
        red = 148, 54, 201                      #rgb code for red stored in variable called red
        led_colour=[(green)]*360                #turn all LEDs to chosen color tostart
        while True:
            if stop==1:
                break
            counter+=1                          #counting the number of loops to determine when the last column of LEDs reachd
            sleep(t)                       #wait for time t
            led_colour=[(green)]*360            #instead of turning specific LEDs back to original color, turning all back to original and right after turning the new ones on
            client.put_pixels(led_colour)       #command to display the Pixels
            if counter==55:                     #if statement to change direction when the ball reaches the last column
                direction=-direction            #multiplying by -1
                t=0.03                          #changing time between loops to slow down the ball
                counter=0                       #reset counter         
            for i in arrow_list:                #the LEDS simbolising an arrow will change color
                    led_colour[i]=(red)         #takes the items in the list one by one and changes they rgb value
            for i in range(len(arrow_list)):    #in the runs for loops as many times as many items in the list currently
                arrow_list[i]=arrow_list[i]+direction#i is equal to the numer of loops this way taking the items one by one and shifting them left or right depending if direction variable is + or -1 atm
                t=t+t_change                    #when all done we change the sleep time for the next loop 
            client.put_pixels(led_colour)       #Display pixels

    def arrow(self):                                                    #arrow function
        arrow_list=[0,1,61,62,122,123,182,183,241,242,300,301]          #list containing pixel positions that need to be turned different colr to create arrow like shape
        t=0.05                                                          #delay to slow down the chenge of pixel colrs 
        counter=0
        led_colour=[(255,255,0)]*360
        while True:
            if stop==1:
                break
            counter+=1                                                  #count the loops
            sleep(t)
            led_colour=[(0,255,255)]*360                                #clear screen
            client.put_pixels(led_colour)
            if (counter/58).is_integer():                               #reset arrow to beginning when got to the end
                arrow_list=[0,1,61,62,122,123,182,183,241,242,300,301]         
            for i in arrow_list:                                        #turn them different color
                led_colour[i]=(255,0,0)
            for i in range(len(arrow_list)):                            #move pixe position to the right by one pixel
                arrow_list[i]=arrow_list[i]+1        
            client.put_pixels(led_colour)                               #display them

    def rainbow_1(self):                                                
        s=1.0
        v=1.0
        pixels_rainbow_1=[]             
        for hue in range(360):                                  #using numpy functions create colors that are in degrees                               
            if stop==1: 
                break
            rgb_fraction = colorsys.hsv_to_rgb(hue/360.0,s,v)   #convert ot RGB and gives the 3 flost numbers instead of degrees
            r=rgb_fraction[0]*255                               #we get floats, still need to multiply by 255 to get the rgb values
            g=rgb_fraction[1]*255
            b=rgb_fraction[2]*255
            rgb = (r,g,b)            
            pixels_rainbow_1.append(rgb)                        #add to list
            client.put_pixels(pixels_rainbow_1)                 #we have 360 colors now we display them one by one as they are created
            sleep(0.01)        
        while True:                                             #after we have the rainbow colors we use them for this endless cycle changing slowly the colors 
            if stop==1:
                break
            for i in pixels_rainbow_1:                
                led_colours=[(i)]*360
                client.put_pixels(led_colours)
                sleep(0.02)

    def rainbow_2(self):                                        #same as before but shifting the colors from left to right
        s=1.0
        v=1.0
        pixels_rainbow_2=[]
        for hue in range(360):
            if stop==1:
                break
            rgb_fraction = colorsys.hsv_to_rgb(hue/360.0,s,v) #convert ot RGB and gives the 3 numbers instead of degrees
            r=rgb_fraction[0]*255
            g=rgb_fraction[1]*255
            b=rgb_fraction[2]*255
            rgb = (r,g,b)
            pixels_rainbow_2.append(rgb)        
            client.put_pixels(pixels_rainbow_2)
            sleep(0.001)
        while True:
            if stop==1:
                break
            pixels_rainbow_2.insert(0, pixels_rainbow_2.pop())
            client.put_pixels(pixels_rainbow_2)
            sleep(0.005)

def on_my_press(key):                           #this function is to stop the animation loop
    global stop                                 #make it global otherwise it only exist in this function and the animation function will not see it
    print("key pressed")                        #this is just feedback
    if key.char == 's':                         #if keyboard character is "s" than change the value of stop from 0 to 1
        stop=1                                  #animations are only running until stop is 0
                
def on_my_release(key):                         #when release keyboard key x the if statement becomes true and will ask you if want to kill the app
    print("key released")
    if key.char == 'x':
        print ("THE END")
        exit()
        
def myListener():                               #the function listening for keypresses, it will be very useful for the snake animation
    with Listener(                              #with listener in pynput library keeps checking if any keypressed and if yes sends the key to press/release function
        on_press=on_my_press,
        on_release=on_my_release) as listener:
        listener.join()                         #waiting for the listening to end or be terminated. I believe if this wasnt a thread it would wait here until finished
        
if run_once==0:                                 #start listening on a separate thread
    print("run=1/listening to keypressed")      #use print as a feedback to know we managed to change the variable 
    run_once=1                                  #change 0 to 1 so the if statement will not be true anymore
    l = threading.Thread(target = myListener)   #run function on seperate thread
    l.start()                                   #start thread

if __name__ == "__main__":                      
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
