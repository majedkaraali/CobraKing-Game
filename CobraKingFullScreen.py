import subprocess
import sys
import time
########################################################################################## Libaries

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    print("[GAME] Trying to import tkinter ")
    from tkinter import *
except:
    print("[EXCEPTION] tkinter not installed")
    try:
        print("[GAME] Trying to install tkinter via pip")
        import pip
        install("tk")
        print("[GAME] tkinter has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")

try:
    print("[GAME] Trying to import Pillow")
    import PIL
except:
    print("[EXCEPTION] Pillow not installed")
    try:
        print("[GAME] Trying to install Pillow via pip")
        import pip
        install("Pillow")
        print("[GAME] Pillow has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")

##########################################################################################


from tkinter import *
from PIL import Image,ImageTk
import random
import time
import threading


root=Tk()
root.title("CobraKing")
root.iconbitmap("imgs/1c.ico")
#root.geometry("800x600")

boxes_=[]
images_=[]


ggame=0
win=0
sayac=0
score=0
score2=0
player=1

liste=[] 
take=[]
collected=[]
games=[]

#root.attributes('-fullscreen', True)
gimg=ImageTk.PhotoImage(Image.open("imgs/bg7.jpg"))

def chek_effect(true:bool):
    pass

def louncher():
    
    global gimg,div22,info,div
    div=Label(root,image=gimg,width=730,heigh=400,bg="#202529")
    div.grid(row=0,column=0)
    cbk=Label(div,text="COBRAKING",font=("Times" ,28),bg="#202529",fg="#FFD700")
    cbk.place(x=248,y=55)
    div22=LabelFrame(root,width=734,heigh=40,bg="#202529",borderwidth=0)
    div22.grid(row=1,column=0)
    start=Button(div,text="PLAY",command=new_game,font=("Times" ,18),fg="white",bg="#202529",borderwidth=0,activebackground="#78d6ff")
    start.place(x=330,y=265)
    ex=Button(div22,text="Exit",command=exit ,font=("Times" ,14),fg="white",bg="#202529",borderwidth=0,activebackground="#78d6ff")
    ex.place(x=0,y=10)
    info=Button(div22,text="Info",command=infoo ,font=("Times" ,14),fg="white",bg="#202529",borderwidth=0,activebackground="#78d6ff")
    info.place(x=690,y=10)



    

def check():
    global sayac,div2,div1,boxes,boxes_
    global take,win,score,player,score2,info
    score=int(score)
    score2=int(score2)
    # THIS LOCKS OTHER BOXES 
    
 
    for box in boxes_:
        box.config(command="None")


    time.sleep(0.5)


    if liste[0]==liste[1]:
        

        for i in take:
            collected.append(i)

        if player==1:
            player=1
            score+=10
        elif player==2:
            score2+=10
            player==2

        trac_game("match_rol",match=True)
            
        
        
    else:
        
        if player==1:
            player=2
        elif player==2:
            player=1
        trac_game("false_rol",match=False)
       


    for i in range(1, 25):
        if i not in collected:
            boxes_[i - 1].config(command=lambda i=i: play(i), bg="#1c2127", image=logo2)


    take.clear()
    liste.clear()
    
    
    
    



    
def trac_game(info,match:bool):
    global games,win,score,score2

    if match:
        win=1
        crr=Label(div2,text="Correct!  ",fg="green",font=("BLOD",18),bg="#282828")
        crr.place(x=580,y=15)
        time.sleep(1)
        crr.destroy()


    else:
        wr=Label(div2,text="Wrong!  ",fg="red",font=("BLOD",18),bg="#282828")
        wr.place(x=580,y=15)
        time.sleep(1)
        wr.destroy()

    scoree()

    games.append(info)

    if games.count('match_rol')==12:
        result()



def result():
    global div112
    time.sleep(2)
    div.destroy()
    div1.destroy()
    div112=Frame(root,bg="#2E8B57")
    div112.grid(row=1,column=0,ipadx=900,ipady=340)
    print(score,score2)
    if score>score2:
        winlab=Label(div112,text="Winner is Player1  ",fg="white",bg="#282828",font=("Times",42))
        
    elif  score<score2:
        winlab=Label(div112,text="Winner is Player2  ",fg="white",bg="#282828",font=("Times",42))
    else:
        winlab=Label(div112,text="No Winner   ,   TIE  ",fg="white",bg="#282828",font=("Times",42))
    
    winlab.place(x=380,y=302)
    
    
  

 

def scoree():
    global div1,boxes,ggame,remove,score,score2,div1,div2,boxes,ggame,remove,div3
    global boxes_,sayac,div2,remove,take
 
    
    print('RUNssssssssssss')
    print(score,score2)
    
    score=str(score)
    score2=str(score2)
    
    lab=Label(div2,text="Player1 Score :"+score,fg="white",bg="#282828",font=("Times",14))
    lab.place(x=10,y=5)
    lab2=Label(div2,text="Player2 Score :"+score2,fg="white",bg="#282828",font=("Times",14))
    lab2.place(x=10,y=34)
    
    score=int(score)
    score2=int(score2)

    if player==1:
        pl=Label(div2,text="Player 1",font=("Times" ,20),fg="white",bg="#282828")
    elif player==2:
        pl=Label(div2,text="Player 2",font=("Times" ,20),fg="white",bg="#282828")
    pl.place(x=580,y=15)


    
    


    
    


    
def new_game():
    print('FULL ')
#root.attributes('-fullscreen', True)
    global boxes,liste,div2,boxes,ggame,div3,info
    global images_,logo2,div22
    div22.destroy()

    boxes=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    
    liste.clear()
    logo2=ImageTk.PhotoImage(Image.open("imgs/logo2.jpg"),width=145,heigh=155)

    for image in range(1,13):
        print(image)
        IMAGE=ImageTk.PhotoImage(Image.open(f"imgs/{image}.jpg"))
       
    
        liste.append(IMAGE)
        liste.append(IMAGE)
       
    for i in range(1,25):
        image=random.choice(liste)
        liste.remove(image)
        images_.append(image)


    frames()
    






    




def frames():
   
    global div1,div2,boxes,ggame,remove,div3,info
    div1=Frame(root,bg="#2E8B57")
    div1.grid(row=0,column=0,ipadx=900,ipady=340)
    div3=Frame(root,bg="#CDAD00")
    div3.grid(row=1,column=0,ipadx=900,ipady=1)
    div2=Frame(root,bg="#282828")
    div2.grid(row=2,column=0,ipadx=900,ipady=110)

    res=Button(div2,text="Restart",command=restart,width=6,heigh=2,bg="#FFB90F")
    res.place(x=1140,y=15)
    mmm=Button(div2,text="Menu",command=menuu,width=6,heigh=2,bg="#FFB90F")
    mmm.place(x=1200,y=15)
    x=Button(div2,text="Exit",command=exit,width=6,heigh=2,bg="#FFB90F")
    x.place(x=1260,y=15)
    game()
    
    
def game():
    global div1,boxes,ggame,score,score2,box17,box18,box19,box20,box21,box22,box23,box24,div1,div2,boxes,ggame,remove,div3,info
    global boxes_,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,sayac,div2,remove,take
    
    box1=Button(div1,command=lambda :play(1),bg="#1c2127",image=logo2)
    box2=Button(div1,command=lambda :play(2),bg="#1c2127",image=logo2)
    box3=Button(div1,command=lambda :play(3),bg="#1c2127",image=logo2)
    box4=Button(div1,command=lambda :play(4),bg="#1c2127",image=logo2)
    box5=Button(div1,command=lambda :play(5),bg="#1c2127",image=logo2)
    box6=Button(div1,command=lambda :play(6),bg="#1c2127",image=logo2)
    box7=Button(div1,command=lambda :play(7),bg="#1c2127",image=logo2)
    box8=Button(div1,command=lambda :play(8),bg="#1c2127",image=logo2)
    box9=Button(div1,command=lambda :play(9),bg="#1c2127",image=logo2)
    box10=Button(div1,command=lambda :play(10),bg="#1c2127",image=logo2)
    box11=Button(div1,command=lambda :play(11),bg="#1c2127",image=logo2)
    box12=Button(div1,command=lambda :play(12),bg="#1c2127",image=logo2)
    box13=Button(div1,command=lambda :play(13),bg="#1c2127",image=logo2)
    box14=Button(div1,command=lambda :play(14),bg="#1c2127",image=logo2)
    box15=Button(div1,command=lambda :play(15),bg="#1c2127",image=logo2)
    box16=Button(div1,command=lambda :play(16),bg="#1c2127",image=logo2)
    box17=Button(div1,command=lambda :play(17),bg="#1c2127",image=logo2)
    box18=Button(div1,command=lambda :play(18),bg="#1c2127",image=logo2)
    box19=Button(div1,command=lambda :play(19),bg="#1c2127",image=logo2)
    box20=Button(div1,command=lambda :play(20),bg="#1c2127",image=logo2)
    box21=Button(div1,command=lambda :play(21),bg="#1c2127",image=logo2)
    box22=Button(div1,command=lambda :play(22),bg="#1c2127",image=logo2)
    box23=Button(div1,command=lambda :play(23),bg="#1c2127",image=logo2)
    box24=Button(div1,command=lambda :play(24),bg="#1c2127",image=logo2)

   
   
    box1.place(x=10,y=10)
    box2.place(x=168,y=10)
    box3.place(x=326,y=10)
    box4.place(x=484,y=10)
    box5.place(x=642,y=10)
    box6.place(x=800,y=10)
    box7.place(x=958,y=10)
    box8.place(x=1116,y=10)
    box9.place(x=10,y=176)
    box10.place(x=168,y=176)
    box11.place(x=326,y=176)
    box12.place(x=484,y=176)
    box13.place(x=642,y=176)
    box14.place(x=800,y=176)
    box15.place(x=958,y=176)
    box16.place(x=1116,y=176)
    box17.place(x=10,y=342)
    box18.place(x=168,y=342)
    box19.place(x=326,y=342)
    box20.place(x=484,y=342)
    box21.place(x=642,y=342)
    box22.place(x=800,y=342)
    box23.place(x=958,y=342)
    box24.place(x=1116,y=342)


    boxes_.extend([box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,box17,box18,box19,box20,box21,box22,box23,box24])



    score=str(score)
    score2=str(score2)
    
    lab=Label(div2,text="Player1 Score :"+score,fg="white",bg="#282828",font=("Times",14))
    lab.place(x=10,y=5)
    lab2=Label(div2,text="Player2 Score :"+score2,fg="white",bg="#282828",font=("Times",14))
    lab2.place(x=10,y=34)
    
    if player==1:
        pl=Label(div2,text="Player1",font=("Times" ,20),fg="white",bg="#282828")
    elif player==2:
        pl=Label(div2,text="Player2",font=("Times" ,20),fg="white",bg="#282828")
    pl.place(x=580,y=15)
            
            


    
    

     
    
def play(a):
    
    global boxes_ ,div1,div2,boxes,ggame,remove,div3,info,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,sayac,div2,div1,remove,take,ggame,info
    ggame+=1

    

    boxes_[a-1].config(command = 0)
    boxes_[a-1].config(image=images_[a-1],bg="white")
    liste.append(images_[a-1])
    take.append(a)
    sayac+=1   
        
    if sayac==2:
        sayac=0
        threading.Thread(target=check).start()
        
             
        

    
    

def restart():
    global score,score2,div,sup,info,div22,info,div3,div2,div1,div22
    div1.destroy()
    div2.destroy()
    div3.destroy()



    boxes_.clear()
    liste.clear()
    take.clear()

    score=0
    score2=0
    new_game()
    
    
def exit():
    root.destroy()
    
    
def x():
    global div,sup,info
    sup.destroy()
    
    
def infoo():
    global div,sup
    sup=Frame(div,width=350,heigh=250,bg="#8E8E8E")
    sup.place(x=175,y=50)
    tt=Label(sup,text="CobraKing Game By Majed",bg="#8E8E8E",fg="#EEE8AA",font=("Times" ,14))
    tt.place(x=75,y=50)
    tt=Label(sup,text="Discord",bg="#8E8E8E",fg="#EEE8AA",font=("Times" ,14))
    tt.place(x=145,y=90)
    tt=Label(sup,text="majed#5222",bg="#8E8E8E",fg="#EEE8AA",font=("Times" ,14))
    tt.place(x=135,y=120)
    cls=Button(sup,text="close",command=x,bg="#8DB6CD")
    cls.place(x=163,y=200)
    
    

def menuu():
    pass
    global score,score2,div1,div2,div3,info,div112
    div1.destroy()
    div2.destroy()
    div3.destroy()
    div112.destroy()
    root.attributes('-fullscreen', False)
    for i in range(len(liste)):
        liste.pop(0)
    for i in range(len(take)):
        take.pop(0)
    score=0
    score2=0
    louncher()
    

    
    
    
louncher()

root.mainloop()

