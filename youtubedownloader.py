from pytube import YouTube
from tkinter import ttk
from tkinter import *

def downloadvedio():
    url = entervariable.get()
    my_vedio = YouTube(url)
    download = my_vedio.streams.first()
    return download

root = Tk()
root.geometry('350x400')
root.title('youtube downloader')
root.columnconfigure(0,weight=1)

pasteurl = Label(root,text='Paste URL',font=('josh',15))
pasteurl.grid()

entervariable = StringVar()
entrybox = ttk.Entry(root,width=50,textvariable=entervariable)
entrybox.grid()

entrybutton = Button(root,text='Download',fg='red',bg='white',command=downloadvedio)
entrybutton.grid()

root.mainloop()
