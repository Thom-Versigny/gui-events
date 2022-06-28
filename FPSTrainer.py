import tkinter
import random
from tkinter.messagebox import askretrycancel
actie = 5
score = 0
timer = 20
window = tkinter.Tk()
bindings = ['<space>', 's', 'd', 'a', 'w', '<Button-1>', '<Double-Button-1>', '<Triple-Button-1>']
tekstbutton = ['Press: space', 'Press: s','Press: d', 'Press: a', 'Press: w', 'click', 'double click', 'triple click']

window.geometry('520x420')
window.configure(bg='black')
window.title('FPS')

def start(event):
    global actie, score, timer
    score = 0
    timer = 21
    labelactie.unbind(bindings[5])
    labelboven.config(text='score: '+str(score))
    timermin()
    actie = random.randint(0, 7)
    if actie <= 4:
        window.bind(bindings[actie], randombutton)
    else:
        labelactie.bind(bindings[actie], randombutton)
    labelactie.place(x=random.randint(30, 490), y=random.randint(30, 380))
    labelactie.config(text=tekstbutton[actie])

def randombutton(event):
    global score, actie
    if actie <= 4:
        score = score + 1
    else:
        score = score + 2
    labelactie.unbind(bindings[actie])
    window.unbind(bindings[actie])
    actie = random.randint(0, 7)
    if actie <= 4:
        window.bind(bindings[actie], randombutton)
    else:
        labelactie.bind(bindings[actie], randombutton)

    labelboven.config(text='score: '+str(score))
    labelactie.place(x=random.randint(30, 490), y=random.randint(30, 380))
    labelactie.config(text=tekstbutton[actie])

def timermin():
    global timer
    timer = timer - 1
    labeltimer.config(text='tijd over: '+str(timer))
    if timer == 0 :
        answer = askretrycancel('Tijd voorbij!', (f'U heeft {score} punten gescored. Wilt u het nog eens proberen'))
        if answer == True:
            labelactie.unbind(bindings[actie])
            opnieuw()
            return
        elif answer == False:
            window.destroy()
    window.after(1000, timermin)



def opnieuw():
    labelactie.pack(ipadx=5, ipady=10, expand=True)
    labelactie.config(text='klik om te beginnen')
    labelactie.bind(bindings[5], start)
    window.update()
    return labelactie

labelboven = tkinter.Label(window, text='score: '+str(score), bg = 'black', fg= 'white')
labeltimer = tkinter.Label(window, text='tijd over: '+str(timer), bg='black', fg='white')
labelactie = tkinter.Label(window, text='klik om te beginnen',)


labelboven.pack(ipadx=10, ipady=10, side=tkinter.RIGHT, anchor='nw')
labeltimer.pack(ipadx=10, ipady=10, side=tkinter.LEFT, anchor='ne',)

labelactie = opnieuw()
window.mainloop()