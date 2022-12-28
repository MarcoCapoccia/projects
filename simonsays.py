from tkinter import *
from tkinter.ttk import *
import time
import random
import numpy as np 

def reset():
    global score
    global highscore
    if (score > highscore):
        highscore = score
        canvas.itemconfig(highscoreLabel,text="Highscore: "+str(highscore))
    
    score = 0
    canvas.itemconfig(groen,fill="green",tags="niks")
    canvas.itemconfig(rood,fill="#BC0606",tags="niks")
    canvas.itemconfig(geel,fill="#C4BC16",tags="niks")
    canvas.itemconfig(blauw,fill="blue",tags="niks")
    canvas.itemconfig(scoreLabel,text="Score: "+str(score))
    canvas.itemconfig(startKnop,fill="dark green",tags="start")
    canvas.itemconfig(startText,text="Start",tags="start")
    
def start():
    global correctSequence
    correctSequence = np.array([])
    i = 0
    while(i<100):
        correctSequence = np.append(correctSequence,random.randint(0, 3) and random.randint(1, 100)<25)
        if (correctSequence[i] == correctSequence[i-1]):
            correctSequence[i] = random.randint(0, 3)
        i = i+1
    print(correctSequence)
    global index
    index = 0
    global indexCurrent
    indexCurrent = 0
    global sequence
    sequence = np.array([])
    
    canvas.itemconfig(groen,fill="green",tags="groen")
    canvas.itemconfig(rood,fill="#BC0606",tags="rood")
    canvas.itemconfig(geel,fill="#C4BC16",tags="geel")
    canvas.itemconfig(blauw,fill="blue",tags="blauw")
    canvas.itemconfig(startKnop,fill="dark red",tags="stop")
    canvas.itemconfig(startText,text="Stop",tags="stop")
    
    showSequence()

def showSequence():
    global index
    canvas.itemconfig(groen,tags="niks")
    canvas.itemconfig(rood,tags="niks")
    canvas.itemconfig(geel,tags="niks")
    canvas.itemconfig(blauw,tags="niks")
    canvas.itemconfig(startKnop,tags="niks")
    canvas.itemconfig(startText,tags="niks")
    i = 0
    canvas.update()
    showSequence2(5)
    while(i<=index):
        if(correctSequence[i]==0):
            canvas.itemconfig(groen,fill="#49B234")
            canvas.update()
            showSequence2(0)
        elif(correctSequence[i]==1):
            canvas.itemconfig(rood,fill="red")
            canvas.update()
            showSequence2(1)
        elif(correctSequence[i]==2):
            canvas.itemconfig(geel,fill="#FAF13C")
            canvas.update()
            showSequence2(2)
        elif(correctSequence[i]==3):
            canvas.itemconfig(blauw,fill="#5049FA")
            canvas.update()
            showSequence2(3)
        i = i+1

    canvas.itemconfig(groen,tags="groen")
    canvas.itemconfig(rood,tags="rood")
    canvas.itemconfig(geel,tags="geel")
    canvas.itemconfig(blauw,tags="blauw")
    canvas.itemconfig(startKnop,tags="stop")
    canvas.itemconfig(startText,tags="stop")

def showSequence2(x):
    time.sleep(0.4)
    if(x==0):
        canvas.itemconfig(groen,fill="green")     
    elif(x==1):
        canvas.itemconfig(rood,fill="#BC0606")        
    elif(x==2):
        canvas.itemconfig(geel,fill="#C4BC16")     
    elif(x==3):
        canvas.itemconfig(blauw,fill="blue")
    canvas.update()
            
def check():
    global sequence
    global indexCurrent
    global index
    global score
    if(sequence[indexCurrent]==correctSequence[indexCurrent]):
        
        indexCurrent = indexCurrent + 1
    else:
        reset()
        return
    if(indexCurrent-1 == index):
        score = score + 1
        canvas.itemconfig(scoreLabel,text="Score: "+ str(score))
        index = index + 1
        if(index == 100):
            reset()
            canvas.itemconfig(scoreLabel,text="You've won!")
            return
        indexCurrent = 0
        sequence = np.array([])
        showSequence()

def kleurSwitch(groen,rood,geel,blauw,x):
    global sequence
    if(x == 0):
        canvas.itemconfig(groen,fill="#49B234",tags="niks")
        canvas.itemconfig(rood,tags="niks")
        canvas.itemconfig(geel,tags="niks")
        canvas.itemconfig(blauw,tags="niks")
        canvas.update()
        sequence = np.append(sequence,x)
        kleurSwitch2(groen,rood,geel,blauw,x)
    elif(x == 1):
        canvas.itemconfig(rood,fill="red",tags="niks")
        canvas.itemconfig(groen,tags="niks")
        canvas.itemconfig(geel,tags="niks")
        canvas.itemconfig(blauw,tags="niks")
        canvas.update()
        sequence = np.append(sequence,x)
        kleurSwitch2(groen,rood,geel,blauw,x)
    elif(x == 2):
        canvas.itemconfig(geel,fill="#FAF13C",tags="niks")
        canvas.itemconfig(groen,tags="niks")
        canvas.itemconfig(rood,tags="niks")
        canvas.itemconfig(blauw,tags="niks")
        canvas.update()
        sequence = np.append(sequence,x)
        kleurSwitch2(groen,rood,geel,blauw,x)
    elif(x == 3):
        canvas.itemconfig(blauw,fill="#5049FA",tags="niks")
        canvas.itemconfig(groen,tags="niks")
        canvas.itemconfig(geel,tags="niks")
        canvas.itemconfig(rood,tags="niks")
        canvas.update()
        sequence = np.append(sequence,x)
        kleurSwitch2(groen,rood,geel,blauw,x)
    check()  
        
def kleurSwitch2(groen,rood,geel,blauw,x):
    time.sleep(0.4)
    if(x==0):
        canvas.itemconfig(groen,fill="green",tags="groen")
        canvas.itemconfig(rood,tags="rood")
        canvas.itemconfig(geel,tags="geel")
        canvas.itemconfig(blauw,tags="blauw")
    elif(x==1):
        canvas.itemconfig(rood,fill="#BC0606",tags="rood")
        canvas.itemconfig(groen,tags="groen")
        canvas.itemconfig(geel,tags="geel")
        canvas.itemconfig(blauw,tags="blauw")
    elif(x==2):
        canvas.itemconfig(geel,fill="#C4BC16",tags="geel")
        canvas.itemconfig(rood,tags="rood")
        canvas.itemconfig(groen,tags="groen")
        canvas.itemconfig(blauw,tags="blauw")
    elif(x==3):
        canvas.itemconfig(blauw,fill="blue",tags="blauw")
        canvas.itemconfig(rood,tags="rood")
        canvas.itemconfig(geel,tags="geel")
        canvas.itemconfig(groen,tags="groen")
      
def clicked (groen,rood,geel,blauw,x) :
    kleurSwitch(groen,rood,geel,blauw,x)
    
score = 0
highscore = 0
spel = Tk()
spel.title("Simon Says")
spel.geometry("200x300")
canvas = Canvas(spel, width= 200,height=300,bg="white")

groen = canvas.create_rectangle(0, 0, 100, 100, fill = "green",tags='niks')
canvas.tag_bind ('groen',"<Button-1>", lambda event: clicked(groen,rood,geel,blauw,0))
rood = canvas.create_rectangle(100, 0, 200, 100, fill = "#BC0606",tags='niks')
canvas.tag_bind ('rood',"<Button-1>", lambda event: clicked(groen,rood,geel,blauw,1))
geel = canvas.create_rectangle(0, 100, 100, 200, fill = "#C4BC16",tags='niks')
canvas.tag_bind ('geel',"<Button-1>", lambda event: clicked(groen,rood,geel,blauw,2))
blauw = canvas.create_rectangle(100, 100, 200, 200, fill = "blue",tags='niks')
canvas.tag_bind ('blauw',"<Button-1>", lambda event: clicked(groen,rood,geel,blauw,3))

scoreLabel = canvas.create_text(50, 238, text="Score: "+str(score),fill="black")
highscoreLabel = canvas.create_text(50, 262, text="Highscore: "+str(highscore),fill="black")

startKnop = canvas.create_rectangle(125, 225, 175, 275,outline = "black", fill = "dark green",tags='start')
startText = canvas.create_text(150,250,text="Start",tags="start")
canvas.tag_bind('start',"<Button-1>", lambda event: start())
canvas.tag_bind('stop',"<Button-1>", lambda event: reset())

canvas.pack()

mainloop()