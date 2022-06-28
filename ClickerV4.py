import tkinter
window = tkinter.Tk()
nummer = 0

window.geometry('200x200')
window.configure(bg='grey')
window.title('clicker')

def keerdrie(event):
    global nummer
    nummer = nummer*3
    labelmiddle.config(text=nummer)


def deelendrie(event):
    global nummer
    nummer = nummer/3
    labelmiddle.config(text=nummer)

def up(event):
    global nummer
    nummer = nummer + 1
    labelmiddle.config(text=nummer)
    achtergrond(1)
    labelmiddle.bind('<Double-Button-1>', keerdrie)
    window.bind('<space>', keerdrie)
def down(event):
    global nummer
    nummer = nummer - 1
    labelmiddle.config(text=nummer)
    achtergrond(1)
    labelmiddle.bind('<Double-Button-1>', deelendrie)
    window.bind('<space>', deelendrie)

def achtergrond(event):
    if nummer <= -1:
        window.configure(bg='red')
    elif nummer >= 1:
        window.configure(bg='green')
    else:
        window.configure(bg='grey')

def hover(event):
    window.configure(bg='yellow')


buttonup = tkinter.Button(window, text='up', command=lambda: [up(1)])
labelmiddle = tkinter.Label(window, text='0',)
buttondown = tkinter.Button(window, text='down', command=lambda: [down(1)])

buttonup.pack(ipadx=5,ipady=5,expand=True)
labelmiddle.pack(ipadx=5, ipady=5, expand=True)
buttondown.pack(ipadx=5, ipady=5, expand=True)

labelmiddle.bind('<Enter>', hover)
labelmiddle.bind('<Leave>', achtergrond)
window.bind('<Up>', up)
window.bind('+', up)
window.bind('<Down>', down)
window.bind('-', down)


window.mainloop()
