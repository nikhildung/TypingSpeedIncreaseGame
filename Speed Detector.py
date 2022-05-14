words = ['grapes','mango','apple','gun','fan','door','tv','mobile','laptop']

def labelSlider():
    global count,sliderWords\

    # Are Kuch nhi hai Bhai String Modify Kar rha hu Buss Or Agar  count len(text) se
    # Increase Wo gaya Tha Count = 0 kar rha hu buss
    text = 'Welcome to typing Speed Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    # After labelslider waale function ko Wapas Call kar hai gha Afer 1.5 seconds 
    fontLabel.after(150,labelSlider)

def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        timeLableCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timeLableCount.configure(text=timeleft)
        timeLableCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','For Play Again Hit Retry Button')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timeLableCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLableCount.configure(text=score)

# Here argumnet has to be Given
def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')

    #  Bhai Agar Entry mai Jho tune Likha hai and Jho Display hua hai Label Mai Se Agar Same Hai Toh Score ko Inrease Karde
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLableCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox
############################    Root Method    ########################################
root = Tk()
root.geometry('800x600+250+30')
root.configure(bg='powder blue')
root.title('Typing Speed Increser Game')
# TO Set The Window ICon
root.iconbitmap('E:/Nikhil/Python/Projects/Python/typingspeed.ico')


#############################   Variables       ######################################### 
score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0
############################    Label Method    #########################################
# welcome Tag
fontLabel = Label(root,text='',font=('airal',25,'italic bold'),
                  bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordLabel.place(x=350,y=200)

scoreLable = Label(root,text='Your Score : ',font=('airal',25,'italic bold'),bg='powder blue')
scoreLable.place(x=10,y=100)

scoreLableCount = Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLableCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left :',font=('airal',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timeLableCount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLableCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold'),
                            bg='powder blue',fg='dark grey')
gamePlayDetailLabel.place(x=120,y=450)


############################   Entry Method      ##########################################  

# Justify means u w'll start writing from center
wordEntry = Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
# This means When u run the code then anythong u write will start from here
wordEntry.focus_set()



#  This Functions Means When u press the Enter Button startGame function Will Be Called 
root.bind('<Return>',startGame)
root.mainloop()