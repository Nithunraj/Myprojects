from tkinter import *
from PIL import Image,ImageTk
from random import *

#main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background = "medium sea green")

#picture
rock_img = ImageTk.PhotoImage(Image.open("User_rock.jpg"))
paper_img = ImageTk.PhotoImage(Image.open("User_paper.jpg"))
scissor_img = ImageTk.PhotoImage(Image.open("User_scissors.jpg"))
rock_comp_img = ImageTk.PhotoImage(Image.open("Comp_rock.jpg"))
paper_comp_img = ImageTk.PhotoImage(Image.open("Computer_paper.jpg"))
scissor_comp_img = ImageTk.PhotoImage(Image.open("Comp_scissors.jpg"))

#insert image
User_label = Label(root,image=rock_img,bg="medium sea green")
User_label.grid(row=1,column=4)
Comp_label = Label(root,image=rock_comp_img,bg="medium sea green")
Comp_label.grid(row=1,column=0)

#player scores
playerScore = Label(root,text=0,font=100,bg="medium sea green")
playerScore.grid(row=1,column=3)
compScore = Label(root,text=0,font=100,bg="medium sea green")
compScore.grid(row=1,column=1)

#button
rock_bt = Button(root,width=20,height=2,text="Rock",command = lambda:updateChoice('rock'),bg='dodger blue',fg='black')
Paper_bt = Button(root,width=20,height=2,text="Paper",command = lambda:updateChoice('paper'),bg='gold',fg='black')
scissor_bt = Button(root,width=20,height=2,text="Scissor",command = lambda:updateChoice('scissor'),bg='indian red',fg='black')
rock_bt.grid(row=2,column=1)
Paper_bt.grid(row=2,column=2)
scissor_bt.grid(row=2,column=3)

#Headers
computer_header = Label(root,text="Computer",font=50,bg="medium sea green",fg='white')
computer_header.grid(row=0,column=1)
User_header = Label(root,text="User",font=50,bg="medium sea green",fg='white')
User_header.grid(row=0,column=3)

#messages
msg = Label(root,font=50,bg="medium sea green",fg='white')
msg.grid(row=3,column=2)

#update picture
choice = ['rock','paper','scissor']
def updateChoice(x):
#computer choice
    computerchoice = choice[randint(0,2)]
    if computerchoice == 'rock':
        Comp_label.configure(image=rock_comp_img)
    elif computerchoice == 'paper':
        Comp_label.configure(image=paper_comp_img)
    elif computerchoice == 'scissor':
        Comp_label.configure(image=scissor_comp_img)
    else:
        pass


#user choice
    if x == 'rock':
        User_label.configure(image=rock_img)
    elif x == 'paper':
        User_label.configure(image=paper_img)
    else:
        User_label.configure(image=scissor_img)

    WinnerAnnounce(x,computerchoice)

def updatemessage(x):
    msg['text'] = x

def Userscore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)


def Computerscore():
    score = int(compScore['text'])
    score += 1
    compScore['text'] = str(score)


def WinnerAnnounce(player,computer):
    if player == computer:
        updatemessage("its a tie")
    elif player == 'rock':
        if computer == 'paper':
            updatemessage("computer won!,You lose")
            Computerscore()
        else:
            updatemessage('you won')
            Userscore()

    elif player == 'paper':
        if computer == 'scissor':
            updatemessage("computer won!,You lose")
            Computerscore()
        else:
            updatemessage('you won')
            Userscore()

    elif player == 'scissor':
        if computer == 'rock':
            updatemessage("computer won!,You lose")
            Computerscore()
        else:
            updatemessage('you won')
            Userscore()

    else:
        pass



root.mainloop()
