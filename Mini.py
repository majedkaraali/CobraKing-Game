#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import subprocess
import sys
import time
########################################################################################## Libaries

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def harf_yazma(a):
    b=""
    for i in a:
        b+=i
        print(b,end="\r")
        time.sleep(0.1)
#harf_yazma("-Code By Majed")
print("-Code By Majed")



time.sleep(1)
print("Welcome to the game / Oyuna hoş geldiniz")
time.sleep(1)
print("Checking required libraries / Gerekli kütüphaneler kontrol ediliyor")
time.sleep(1)
print("Required libraries are [tkinter,Pillow] / gerekli kütüphaneler [tkinter,Pillow,playsound]")
time.sleep(1)

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
##########################################################################
from tkinter import *
from PIL import Image,ImageTk

import random
import time
import threading
root=Tk()
root.title("CobraKing")
root.iconbitmap("imgs/1c.ico")
#root.geometry("800x600")


ggame=0
win=0
score=0
score2=0
liste=[] 
sayac=0
take=[]
player=1
#root.attributes('-fullscreen', True)
gimg=ImageTk.PhotoImage(Image.open("imgs/bg7.jpg"))



def lounch():
    
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
    info=Button(div22,text="Info",command=infoo,font=("Times" ,14),fg="white",bg="#202529",borderwidth=0,activebackground="#78d6ff")
    info.place(x=690,y=10)


def slp():
    global box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,sayac,div2,div1,boxes
    global take,remove,win,score,player,score2,box17,box18,box19,box20,box21,box22,box23,box24,info
    box1.config(command="None")
    box2.config(command="None")
    box3.config(command="None")
    box4.config(command="None")
    box5.config(command="None")
    box6.config(command="None")
    box7.config(command="None")
    box8.config(command="None")
    box9.config(command="None")
    box10.config(command="None")
    box11.config(command="None")
    box12.config(command="None")
    box13.config(command="None")
    box14.config(command="None")
    box15.config(command="None")
    box16.config(command="None")
    box17.config(command="None")
    box18.config(command="None")
    box19.config(command="None")
    box20.config(command="None")
    box21.config(command="None")
    box22.config(command="None")
    box23.config(command="None")
    box24.config(command="None")
    time.sleep(0.5)

    if liste[0]==liste[1]:
        score=int(score)
        score2=int(score2)
        if player==1:
            player=1
            score+=10
        elif player==2:
            score2+=10
            player==2
            
        win=1
       
        for i in take:
            boxes.remove(i)
        
        wr=Label(div2,text="Correct!  ",fg="green",font=("BLOD",18),bg="#282828")
        wr.place(x=580,y=15)
        time.sleep(1)
        wr.destroy()

        
        
    else:
        if player==1:
            player=2
        elif player==2:
            player=1
      
        wr=Label(div2,text="Wrong!  ",fg="red",font=("BLOD",18),bg="#282828")
        wr.place(x=580,y=15)
        time.sleep(1)
        wr.destroy()
        for i in take:
            if i ==1:
                box1=Button(div1,command=lambda :play(1),bg="#1c2127",image=logo2)
                box1.place(x=10,y=10)
            elif i==2:
                box2=Button(div1,command=lambda :play(2),bg="#1c2127",image=logo2)
                box2.place(x=168,y=10)
            elif i==3:
                box3=Button(div1,command=lambda :play(3),bg="#1c2127",image=logo2)
                box3.place(x=326,y=10)
            elif i==4:
                box4=Button(div1,command=lambda :play(4),bg="#1c2127",image=logo2)
                box4.place(x=484,y=10)
            elif i==5:
                box5=Button(div1,command=lambda :play(5),bg="#1c2127",image=logo2)
                box5.place(x=642,y=10)
            elif i==6:
                box6=Button(div1,command=lambda :play(6),bg="#1c2127",image=logo2)
                box6.place(x=800,y=10)
            elif i==7:
                box7=Button(div1,command=lambda :play(7),bg="#1c2127",image=logo2)
                box7.place(x=958,y=10)
            elif i==8:
                box8=Button(div1,command=lambda :play(8),bg="#1c2127",image=logo2)
                box8.place(x=1116,y=10)
            elif i==9:
                box9=Button(div1,command=lambda :play(9),bg="#1c2127",image=logo2)
                box9.place(x=10,y=176)
            elif i==10:
                box10=Button(div1,command=lambda :play(10),bg="#1c2127",image=logo2)
                box10.place(x=168,y=176)
            elif i==11:
                box11=Button(div1,command=lambda :play(11),bg="#1c2127",image=logo2)
                box11.place(x=326,y=176)
            elif i==12:
                box12=Button(div1,command=lambda :play(12),bg="#1c2127",image=logo2)
                box12.place(x=484,y=176)
            elif i==13:
                box13=Button(div1,command=lambda :play(13),bg="#1c2127",image=logo2)
                box13.place(x=642,y=176)
            elif i==14:
                box14=Button(div1,command=lambda :play(14),bg="#1c2127",image=logo2)
                box14.place(x=800,y=176)
            elif i==15:
                box15=Button(div1,command=lambda :play(15),bg="#1c2127",image=logo2)
                box15.place(x=958,y=176)
            elif i==16:
                box16=Button(div1,command=lambda :play(16),bg="#1c2127",image=logo2)
                box16.place(x=1116,y=176)
            elif i==17:
                box17=Button(div1,command=lambda :play(17),bg="#1c2127",image=logo2)
                box17.place(x=10,y=342)
            elif i==18:
                box18=Button(div1,command=lambda :play(18),bg="#1c2127",image=logo2)
                box18.place(x=168,y=342)
            elif i==19:
                box19=Button(div1,command=lambda :play(19),bg="#1c2127",image=logo2)
                box19.place(x=326,y=342)
            elif i==20:
                box20=Button(div1,command=lambda :play(20),bg="#1c2127",image=logo2)
                box20.place(x=484,y=342)
            elif i==21:
                box21=Button(div1,command=lambda :play(21),bg="#1c2127",image=logo2)
                box21.place(x=642,y=342)
            elif i==22:
                box22=Button(div1,command=lambda :play(22),bg="#1c2127",image=logo2)
                box22.place(x=800,y=342)
            elif i==23:
                box23=Button(div1,command=lambda :play(23),bg="#1c2127",image=logo2)
                box23.place(x=958,y=342)
            elif i==24:
                box24=Button(div1,command=lambda :play(24),bg="#1c2127",image=logo2)
                box24.place(x=1116,y=342)
    
    if len(liste)>1:
        for i in range(len(liste)):
            liste.pop(0)
        for i in range(len(take)):
            take.pop(0)

    
    
    scoree()
    



    
        

    
    

def scoree():
    global div1,boxes,ggame,remove,score,score2,box17,box18,box19,box20,box21,box22,box23,box24,div1,div2,boxes,ggame,remove,div3,info
    global box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,sayac,div2,remove,take
    for i in boxes:
        if i==1:
            box1.config(command=lambda :play(1))
        elif i==2:
            box2.config(command=lambda :play(2))
        elif i==3:
            box3.config(command=lambda :play(3))
        elif i==4:
            box4.config(command=lambda :play(4))
        elif i==5:
            box5.config(command=lambda :play(5))
        elif i==6:
            box6.config(command=lambda :play(6))
        elif i==7:
            box7.config(command=lambda :play(7))
        elif i==8:
            box8.config(command=lambda :play(8))
        elif i==9:
            box9.config(command=lambda :play(9))
        elif i==10:
            box10.config(command=lambda :play(10))
        elif i==11:
            box11.config(command=lambda :play(11))
        elif i==12:
            box12.config(command=lambda :play(12))
        elif i==13:
            box13.config(command=lambda :play(13))
        elif i==14:
            box14.config(command=lambda :play(14))
        elif i==15:
            box15.config(command=lambda :play(15))
        elif i==16:
            box16.config(command=lambda :play(16))
        elif i==17:
            box17.config(command=lambda :play(17))
        elif i==18:
            box18.config(command=lambda :play(18))
        elif i==19:
            box19.config(command=lambda :play(19))
        elif i==20:
            box20.config(command=lambda :play(20))
        elif i==21:
            box21.config(command=lambda :play(21))
        elif i==22:
            box22.config(command=lambda :play(22))
        elif i==23:
            box23.config(command=lambda :play(23))
        elif i==24:
            box24.config(command=lambda :play(24))

    
    
    score=str(score)
    score2=str(score2)
    
    lab=Label(div2,text="Player1 Score :"+score,fg="white",bg="#282828",font=("Times",14))
    lab.place(x=10,y=5)
    lab2=Label(div2,text="Player2 Score :"+score2,fg="white",bg="#282828",font=("Times",14))
    lab2.place(x=10,y=34)
    
    if player==1:
        pl=Label(div2,text="Player 1",font=("Times" ,20),fg="white",bg="#282828")
    elif player==2:
        pl=Label(div2,text="Player 2",font=("Times" ,20),fg="white",bg="#282828")
    pl.place(x=580,y=15)


    
    


    
    
def new_game():
    global boxes,liste,img17,img18,img19,img20,img21,img22,img23,img24,info, div1,div2,boxes,ggame,remove,div3,info
    global logo2,img1,img2,img3,img4,img5,img6,img7,img8,gimg,bac,img9,img10,img11,img12,img13,img14,img15,img16,div22
    div22.destroy()
    boxes=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    if len(liste)>0:
            for i in range(len(liste)):
                liste.pop(0)
    i1=ImageTk.PhotoImage(Image.open("imgs/1.jpg"))
    i2=ImageTk.PhotoImage(Image.open("imgs/2.jpg"))
    i3=ImageTk.PhotoImage(Image.open("imgs/3.jpg"))
    i4=ImageTk.PhotoImage(Image.open("imgs/4.jpg"))
    i5=ImageTk.PhotoImage(Image.open("imgs/5.jpg"))
    i6=ImageTk.PhotoImage(Image.open("imgs/6.jpg"))
    i7=ImageTk.PhotoImage(Image.open("imgs/7.jpg"))
    i8=ImageTk.PhotoImage(Image.open("imgs/8.jpg"))
    i9=ImageTk.PhotoImage(Image.open("imgs/9.jpg"))
    i10=ImageTk.PhotoImage(Image.open("imgs/10.jpg"))
    i11=ImageTk.PhotoImage(Image.open("imgs/11.jpg"))
    i12=ImageTk.PhotoImage(Image.open("imgs/12.jpg"))
    

    
    logo2=ImageTk.PhotoImage(Image.open("imgs/logo2.jpg"),width=145,heigh=155)

    liste.append(i1)
    liste.append(i1)
    liste.append(i2)
    liste.append(i2)
    liste.append(i3)
    liste.append(i3)
    liste.append(i4)
    liste.append(i4)
    liste.append(i5)
    liste.append(i5)
    liste.append(i6)
    liste.append(i6)
    liste.append(i7)
    liste.append(i7)
    liste.append(i8)
    liste.append(i8)
    liste.append(i9)
    liste.append(i9)
    liste.append(i10)
    liste.append(i10)
    liste.append(i11)
    liste.append(i11)
    liste.append(i12)
    liste.append(i12)

    img1=random.choice(liste)
    liste.remove(img1)
    img2=random.choice(liste)
    liste.remove(img2)
    img3=random.choice(liste)
    liste.remove(img3)
    img4=random.choice(liste)
    liste.remove(img4)
    img5=random.choice(liste)
    liste.remove(img5)
    img6=random.choice(liste)
    liste.remove(img6)
    img7=random.choice(liste)
    liste.remove(img7)
    img8=random.choice(liste)
    liste.remove(img8)
    img9=random.choice(liste)
    liste.remove(img9)
    img10=random.choice(liste)
    liste.remove(img10)
    img11=random.choice(liste)
    liste.remove(img11)
    img12=random.choice(liste)
    liste.remove(img12)
    img13=random.choice(liste)
    liste.remove(img13)
    img14=random.choice(liste)
    liste.remove(img14)
    img15=random.choice(liste)
    liste.remove(img15)
    img16=random.choice(liste)
    liste.remove(img16)
    img17=random.choice(liste)
    liste.remove(img17)   
    img18=random.choice(liste)
    liste.remove(img18)
    img19=random.choice(liste)
    liste.remove(img19)
    img20=random.choice(liste)
    liste.remove(img20)
    img21=random.choice(liste)
    liste.remove(img21)
    img22=random.choice(liste)
    liste.remove(img22)
    img23=random.choice(liste)
    liste.remove(img23)
    img24=random.choice(liste)
    liste.remove(img24)
    
    frames()






    




def frames():
    global div1,div2,boxes,ggame,remove,div3,info
    div1=Frame(root,bg="#2E8B57")
    div1.grid(row=0,column=0,ipadx=638,ipady=340)
    div3=Frame(root,bg="#CDAD00")
    div3.grid(row=1,column=0,ipadx=638,ipady=1)
    div2=Frame(root,bg="#282828")
    div2.grid(row=2,column=0,ipadx=638,ipady=34)

    res=Button(div2,text="Restart",command=restart,width=6,heigh=2,bg="#FFB90F")
    res.place(x=1140,y=15)
    mmm=Button(div2,text="Menu",command=menuu,width=6,heigh=2,bg="#FFB90F")
    mmm.place(x=1200,y=15)
    game()
    
    
def game():
    global div1,boxes,ggame,remove,score,score2,box17,box18,box19,box20,box21,box22,box23,box24,div1,div2,boxes,ggame,remove,div3,info
    global box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,sayac,div2,remove,take
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
    
    global div1,div2,boxes,ggame,remove,div3,info,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,sayac,div2,div1,remove,take,ggame,info
    ggame+=1
    
    if a==1:
        box1['command'] = 0
        box1.config(image=img1,width=145,heigh=155,bg="white")

        sayac+=1
        liste.append(img1)
        take.append(a)
    elif a==2:
        box2['command'] = 0
        box2.config(image=img2,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img2)
        take.append(a)
    elif a==3:

        box3.config(image=img3,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img3)
        take.append(a)
    elif a==4:
        box4['command'] = 0
        box4.config(image=img4,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img4)
        take.append(a)

    elif a==5:
        box5['command'] = 0
        box5.config(image=img5,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img5)
        take.append(a)
        box5['command'] = 0
    elif a==6:
        box6['command'] = 0
        box6.config(image=img6,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img6)
        take.append(a)
          
    elif a==7:
        box7['command'] = 0
        box7.config(image=img7,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img7)
        take.append(a)
        
    elif a==8:
        box8['command'] = 0
        box8.config(image=img8,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img8)
        take.append(a)
    elif a==9:
        box9['command'] = 0
        box9.config(image=img9,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img9)
        take.append(a)
        

    elif a==10:
        box10['command'] = 0
        box10.config(image=img10,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img10)
        take.append(a)
        
    elif a==11:
        box11['command'] = 0
        box11.config(image=img11,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img11)
        take.append(a)
        
    elif a==12:
        box12['command'] = 0
        box12.config(image=img12,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img12)
        take.append(a)
        
        
    elif a==13:
        box13['command'] = 0
        box13.config(image=img13,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img13)
        take.append(a)
        
        
    elif a==14:
        box14['command'] = 0
        box14.config(image=img14,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img14)
        take.append(a)
        
        
    elif a==15:
        box15['command'] = 0
        box15.config(image=img15,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img15)
        take.append(a)
            
    elif a==16:
        box16['command'] = 0
        box16.config(image=img16,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img16)
        take.append(a)
    elif a==17:
        box17['command'] = 0
        box17.config(image=img17,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img17)
        take.append(a)
    elif a==18:
        box18['command'] = 0
        box18.config(image=img18,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img18)
        take.append(a)
    elif a==19:
        box19['command'] = 0
        box19.config(image=img19,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img19)
        take.append(a)
    elif a==20:
        box20['command'] = 0
        box20.config(image=img20,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img20)
        take.append(a)
    elif a==21:
        box21['command'] = 0
        box21.config(image=img21,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img21)
        take.append(a)
    elif a==22:
        box22['command'] = 0
        box22.config(image=img22,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img22)
        take.append(a)
    elif a==23:
        box23['command'] = 0
        box23.config(image=img23,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img23)
        take.append(a)
    elif a==24:
        box24['command'] = 0
        box24.config(image=img24,width=145,heigh=155,bg="white")
        sayac+=1
        liste.append(img24)
        take.append(a)
    
               
        
    if sayac==2:
        sayac=0
        threading.Thread(target=slp).start()
        
 
             
        

    
    

def restart():
    global score,score2,div,sup,info,div22,info,div3,div2,div1,div22
    div1.destroy()
    div2.destroy()
    div3.destroy()
    for i in range(len(liste)):
        liste.pop(0)
    for i in range(len(take)):
        take.pop(0)
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
    global score,score2,div1,div2,div3,info
    div1.destroy()
    div2.destroy()
    div3.destroy()

    for i in range(len(liste)):
        liste.pop(0)
    for i in range(len(take)):
        take.pop(0)
    score=0
    score2=0
    lounch()
    

    
    
    
lounch()

root.mainloop()

