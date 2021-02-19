from tkinter import*
import random

root=Tk()
root.title('Spearton')

canvas=Canvas(root,width=400,height=400,bg='#d1d4f2')
canvas.pack()

heading=Label(root,text='Welcome To Rock Paper Scissor',bg='#d1d4f2',font=('Courier',15,'bold'))
canvas.create_window(200,25,window=heading)

label=Label(root,text='Make your play ',bg='#d1d4f2',font=('Courier',13,'bold'))
canvas.create_window(200,70,window=label)

def clear_all():
    display.delete(0,END)

def clear1_all():
    display1.delete(0,END)

def combination(x):
    user_pick=x
    if user_pick=='stone':
        result='Rock'
        clear_all()
        display.insert(0,result)

    elif user_pick=='paper':
        result='Paper'
        clear_all()
        display.insert(0,result)

    elif user_pick=='scissor':
        result='Scissor'
        clear_all()
        display.insert(0,result)



display=Entry(root,bd=0,fg='#f5a548',bg='#d1d4f2',justify='center',font=('Courier,11'))
canvas.create_window(200,195,window=display)
Stone=Button(root,text='\u270a',bd=0,fg='#f5a548',bg='#d1d4f2',activebackground='#d1d4f2',font=('Courier',30),command=lambda:combination('stone'))
canvas.create_window(100,120,window=Stone)
paper=Button(root,text='\u270b',bd=0,fg='#f5a548',bg='#d1d4f2',activebackground='#d1d4f2',font=('Courier',30),command=lambda:combination('paper'))
canvas.create_window(300,120,window=paper)
Scissor=Button(root,text='\u270c',bd=0,fg='#f5a548',bg='#d1d4f2',activebackground='#d1d4f2',font=('Courier',30),command=lambda:combination('scissor'))
canvas.create_window(200,145,window=Scissor)

display1=Entry(root,bd=0,fg='#757575',bg='#d1d4f2',justify='center',font=('Courier,11'))
canvas.create_window(200,220,window=display1)
Stone1=Button(root,text='\u270a',bd=0,fg='#d1d4f2',bg='#d1d4f2',font=('Courier',30))
canvas.create_window(100,275,window=Stone1)
paper1=Button(root,text='\u270b',bd=0,fg='#d1d4f2',bg='#d1d4f2',font=('Courier',30))
canvas.create_window(200,275,window=paper1)
Scissor1=Button(root,text='\u270c',bd=0,fg='#d1d4f2',bg='#d1d4f2',font=('Courier',30))
canvas.create_window(300,275,window=Scissor1)

def ston():
    Stone1['fg']='#757575'
def pape():
    paper1['fg']='#757575'
def scisso():
    Scissor1['fg']='#757575'

def rd():
    display2['fg']='red'
def gr():
    display2['fg']='green'
def br():
    display2['fg']='#318ce7'



def play():
    comp_pick=random.randint(1,3)
    if comp_pick==1:
        comp_pick='Rock'
        display1.insert(0,comp_pick)
        ston()
    elif comp_pick==2:
        comp_pick='Paper'
        display1.insert(0,comp_pick)
        pape()

    elif comp_pick==3:
        comp_pick='Scissor'
        display1.insert(0,comp_pick)
        scisso()

    user_choice=display.get()
    if user_choice==comp_pick:
        Result='it is a tie'
        display2.insert(0,Result)
        br()
    elif user_choice=='Rock' and comp_pick=='Paper':
        Result='Computer wins ,Better luck next time'
        display2.insert(0,Result)
        rd()
    elif user_choice=='Rock' and comp_pick=='Scissor':
        Result='You win'
        display2.insert(0,Result)
        gr()
    elif user_choice=='Paper' and comp_pick=='Rock':
        Result='You win'
        display2.insert(0,Result)
        gr()
    elif user_choice=='Paper' and comp_pick=='Scissor':
        Result='Computer wins ,Better luck next time'
        display2.insert(0,Result)
        rd()
    elif user_choice=='Scissor' and comp_pick=='Paper':
        Result='You win'
        display2.insert(0,Result)
        gr()
    elif user_choice=='Scissor' and comp_pick=='Rock':
        Result='Computer wins ,Better luck next time'
        display2.insert(0,Result)
        rd()

def Reset():
    display2.delete(0,END)
    clear_all()
    clear1_all()
    Stone1['bg']='#d1d4f2'
    Stone1['fg']='#d1d4f2'
    paper1['bg']='#d1d4f2'
    paper1['fg']='#d1d4f2'
    Scissor1['bg']='#d1d4f2'
    Scissor1['fg']='#d1d4f2'

def Exit():
    root.destroy()

display2=Entry(root,bd=0,bg='#d1d4f2',justify='center',font=('Courier',12,'bold'))
canvas.create_window(200,320,width=390,window=display2)
play=Button(root,text='Play',bd=0,bg='#d1d4f2',activebackground='#d1d4f2',font=('Courier',12),command=play)
canvas.create_window(80,360,window=play)
reset=Button(root,text='Reset',bd=0,bg='#d1d4f2',activebackground='#d1d4f2',font=('Courier',12),command=Reset)
canvas.create_window(200,360,window=reset)
exit=Button(root,text='Exit',bd=0,bg='#d1d4f2',activebackground='#d1d4f2',font=('Courier',12),command=Exit)
canvas.create_window(320,360,window=exit)


root.mainloop()
