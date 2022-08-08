import tkinter as tk 
from time import sleep as s 
import keyboard
import mouse


def keyboardfc():
    def onof():
        enteronof = enter['text']
        if enteronof == 'ENTER ON':
            enter['text'] = 'ENTER OFF'
        else: 
            enter['text']='ENTER ON'

    def go():
        enteronof = enter['text']
        delay = delaystrv.get()
        delay = int(delay)
        
        text = repetstrv.get()

        times = timesstrv.get()
        times = int(times)
        
        delay = delay/1000
        if enteronof == 'ENTER ON':
            s(3)
            while not times==0:
                keyboard.write(text)
                keyboard.press('enter')
                times = times-1
                s(delay)
        else:
            s(10)
            while not times==0:
                keyboard.write(text)
                times = times-1
                s(delay)

        quit()

    

    keyboardw = tk.Toplevel()
    keyboardw.geometry('500x200')
    keyboardw.title('Keyboard Spam')

    intro = tk.Label(keyboardw, text='Spam any text', font=('Arial',20)).pack()
    subtit = tk.Label(keyboardw, text='Please set your spammer', font=('Arial',11)).pack()

    repetstrv = tk.StringVar(keyboardw)
    entradrepet = tk.Entry(keyboardw, textvariable=repetstrv).place(x=180,y=100)

    gobtn = tk.Button(keyboardw, text='GO', command=go).place(x=350, y=100)


    timeslabel = tk.Label(keyboardw, text='Repeat x times').place(x=200, y=140)
    timesstrv = tk.StringVar(keyboardw)
    timesentry = tk.Entry(keyboardw, textvariable=timesstrv).place(x=180, y=170)

    enter = tk.Button(keyboardw, text='PRESS ENTER?', command=onof)
    enter.place(x=80, y=150)

    delaylbl = tk.Label(keyboardw, text='Delay (ms)').place(x=420, y=120)
    delaystrv = tk.StringVar(keyboardw)
    delayentry = tk.Entry(keyboardw, textvariable=delaystrv).place(x=420, y=150)
    
def mousefc():    

    def gocmd():
        delay = delaystrv.get()
        delay = int(delay)
        delay = delay/1000

        clicks = repetstrv.get()
        clicks = int(clicks)

        s(3)

        while clicks>0:
            mouse.click()
            clicks = clicks-1
            s(delay)
    mousew = tk.Toplevel()
    mousew.geometry('500x200')
    mousew.title('Keyboard Spam')

    intro = tk.Label(mousew, text='AutoClicker', font=('Arial',20)).pack()
    subtit = tk.Label(mousew, text='Please, set your spammer', font=('Arial',11)).pack()

    repetstrv = tk.StringVar(mousew)
    entradrepet = tk.Entry(mousew, textvariable=repetstrv).place(x=180,y=100)
    repetstrv.set('Number of clicks')

    delaystrv = tk.StringVar(mousew)
    delayentry = tk.Entry(mousew, textvariable=delaystrv).place(x=180, y=130)
    delaystrv.set('Delay (ms)')

    gobtn = tk.Button(mousew, text='GO', command=gocmd).place(x=360, y=115)


main = tk.Tk()
main.title('All-in-one spammer')
main.geometry('500x200')


intro = tk.Label(main, text='Spammer and AutoClicker', font=('Arial',20)).pack()


keyboardbtn = tk.Button(main, text='Spam', command=keyboardfc).place(x=100, y=100)

mousebtn = tk.Button(main, text='AutoClicker', command=mousefc).place(x=300, y=100)



main.mainloop()