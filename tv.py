import pyttsx3
from deep_translator import GoogleTranslator
from tkinter import *
from tkinter import ttk

root= Tk()
root.geometry('551x150')
root.resizable(0,0)
root.title('Translate')

fram1=LabelFrame(root,font=('Arial',15,'bold'),bg='yellow',bd=5,fg='white')
fram1.place(x=0,y=2,width=551,height=50)

fram2=LabelFrame(root,font=('Arial',15,'bold'),bg='yellow',bd=5,fg='white')
fram2.place(x=0,y=50,width=551,height=50)

fram3=LabelFrame(root,font=('Arial',15,'bold'),bg='yellow',bd=5,fg='white')
fram3.place(x=0,y=100,width=551,height=50)


# -------------------------------------list--------------------------------------
# list1 = Listbox(fram3, width=66, height=14)
# list1.pack(fill=BOTH)
#
# sb1 = Scrollbar(root)
# sb1.place(x=290, y=80)
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

msg = StringVar()

e1 = Entry(root,width=68, textvariable=msg)
e1.place(x=125,y=15)

# ------------------ترجمه متن فارسی به انگلیسی-------------
l11 = Label(fram3,bg='yellow',font=('Arial',10,'bold'))
def tranen():
    y=e1.get()
    global output
    output=GoogleTranslator(source="fa",target="en").translate(y)
    l11.config(text=output)
    l11.place(x=2, y=6)

# ------------------ترجمه متن انگلیسی به فارسی -------------

def tranfa():
    y=e1.get()
    global output
    output=GoogleTranslator(source="en",target="fa").translate(y)
    l11.config(text=output)
    l11.place(x=2, y=6)

# ---------------------------------------------------------------------------------------------

def speechman():
    engine=pyttsx3.init()
    engine.setProperty('rate',115)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    # 0 man
    engine.say(output)
    engine.runAndWait()

def speechwoman():
    engine=pyttsx3.init()
    engine.setProperty('rate',115)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    # 1 woman
    engine.say(output)
    engine.runAndWait()


def Reset():
    msg.set("")



l1=Label(root,text='Plese Enter The Text : ',bg='yellow')
l1.place(x=6,y=13)





b1 = Button(fram2, text='translate en', width=12, command=tranen,bg='orange')
b1.place(x=3,y=6)

b2 = Button(fram2, text='man voice(en)', width=15, command=speechman,bg='orange')
b2.place(x=103,y=6)

b3 = Button(fram2, text='woman voice(en)', width=15, command=speechwoman,bg='orange')
b3.place(x=223,y=6)

b4 = Button(fram2, text='translate fa', width=12, command=tranfa,bg='orange')
b4.place(x=343,y=6)

b5 = Button(fram2, text='Reset', width=12, command=Reset,bg='orange')
b5.place(x=442,y=6)


root.mainloop()









