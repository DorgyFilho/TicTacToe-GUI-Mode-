from tkinter import *

Win = Tk()
Win.title('Tic-Tac-Toe --- Concept By Dorgival Filho')
Win.geometry('320x480')

InfoText = StringVar()
InfoText.set('Info\nPlayer 1: X\nPlayer 2: O')
InfoLabel = Label(Win, textvariable=InfoText)
InfoLabel.grid(row=5, column=2)

LabText = StringVar()
LabText.set('Result: ')
TextLab = Label(Win, textvariable=LabText)
TextLab.grid(row=7, column=2)


enter = True
def TTT(but):
    global enter
    if but['text'] == ' ' and enter == True:
        but['text'] = 'X'
        enter = False
    elif but['text'] == ' ' and enter == False:
        but['text'] = 'O'
        enter = True
    checking()

def checking():
    if (but1['text'] == 'X' and but2['text'] == 'X' and but3['text'] == 'X' or
    but4['text'] == 'X' and but5['text'] == 'X' and but6['text'] == 'X' or
    but7['text'] == 'X' and but8['text'] == 'X' and but9['text'] == 'X' or
    but2['text'] == 'X' and but5['text'] == 'X' and but8['text'] == 'X' or
    but3['text'] == 'X' and but6['text'] == 'X' and but9['text'] == 'X' or
    but1['text'] == 'X' and but4['text'] == 'X' and but7['text'] == 'X' or
    but1['text'] == 'X' and but5['text'] == 'X' and but9['text'] == 'X' or
    but3['text'] == 'X' and but5['text'] == 'X' and but7['text'] == 'X'):
        LabText.set('Player 1 Wins!!!')

    elif (but1['text'] == 'O' and but2['text'] == 'O' and but3['text'] == 'O' or
    but4['text'] == 'O' and but5['text'] == 'O' and but6['text'] == 'O' or
    but7['text'] == 'O' and but8['text'] == 'O' and but9['text'] == 'O' or
    but2['text'] == 'O' and but5['text'] == 'O' and but8['text'] == 'O' or
    but3['text'] == 'O' and but6['text'] == 'O' and but9['text'] == 'O' or
    but1['text'] == 'O' and but4['text'] == 'O' and but7['text'] == 'O' or
    but1['text'] == 'O' and but5['text'] == 'O' and but9['text'] == 'O' or
    but3['text'] == 'O' and but5['text'] == 'O' and but7['text'] == 'O'):
        LabText.set('Player 2 Wins!!!')

but = StringVar()

but1 = Button(Win, text=' ', fg='black', height=3, width=6,  font=('Kalimati', '12'), command=lambda:TTT(but1))
but1.grid(row=1, column=1, sticky=S+N+E+W) 
but2 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but2))
but2.grid(row=1, column=2, sticky=S+N+E+W)
but3 = Button(Win, text=' ', fg='black',height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but3))
but3.grid(row=1, column=3, sticky=S+N+E+W) 
but4 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but4))
but4.grid(row=2, column=1, sticky=S+N+E+W) 
but5 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but5))
but5.grid(row=2, column=2, sticky=S+N+E+W) 
but6 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but6))
but6.grid(row=2, column=3, sticky=S+N+E+W) 
but7 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but7))
but7.grid(row=3, column=1, sticky=S+N+E+W) 
but8 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but8))
but8.grid(row=3, column=2, sticky=S+N+E+W) 
but9 = Button(Win, text=' ', fg='black', height=3, width=6, font=('Kalimati', '12'), command=lambda:TTT(but9))
but9.grid(row=3, column=3, sticky=S+N+E+W) 

resText = StringVar()
resText.set('Result: ')

Win.mainloop()