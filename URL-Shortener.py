from tkinter import *
import pyshorteners

#~~~~~~~~~~~~~~GUI interface~~~~~~~~~~~~~~~
#creating the application main window. 
win = Tk()
win.title("~~~URL Shortener~~~")
win.geometry("550x300")
win.resizable(False,False)

#~~~~~~~~~~~~~~~ Shorten URL~~~~~~~~~~~~~~~
def generate_url():
#input long URL
    long = str(long_url.get())

#initialize the pyshortener library’s class object to start shortening our URL.
    type_tiny = pyshorteners.Shortener()

#now we shorten our URL
    shortURL = type_tiny.tinyurl.short(long)
    result.set(shortURL)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Frame
line = Frame(win, width=550, height=5, bg="#162252")
line.grid(row=0, column=0)

body = Frame(win, width=550, height=300, bg="#D3D3D3")
body.grid(row=1, column=0)

#widget
name = Label(win, text= "URL Shortener", font=("Arial",18,"bold","italic","underline"),bg= "silver",fg = "#162252", relief=RAISED)
name.place(x = 200, y = 20)

#to take input from user
url = Label(win, text="Long URL",font= ("Times New Roman", 12, "bold"),bg="white",fg= "#162252", relief= GROOVE ).place(x = 30, y = 100)
long_url = StringVar()
Entry(win, textvariable=long_url,font= ("Times New Roman", 12, "bold"), width= 40, relief=GROOVE).place(x = 130, y = 100)

#button to call fun and generate url
Button(win, text="Generate Short one", font= ("Arial", 15, "bold"),bg= "silver",fg = "#162252", relief=RAISED, command=generate_url).place(x = 200, y = 150)

#output the short one
Label(win,text = "New URL / Copy it", font= ("Times New Roman", 12, "bold"),bg="white",fg= "#162252",relief= GROOVE).place(x = 30, y = 220)
result = StringVar()
Entry(win,textvariable=result, font= ("Times New Roman", 12, "bold"),width = 40, relief=GROOVE).place(x = 200, y = 220)


#Entering the event main loop  
win.mainloop()
  