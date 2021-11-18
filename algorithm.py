from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import docx2pdf

app = Tk()
app.geometry('250x100')
app.resizable(0,0)
app.title("Docx2pdf")
def targetpathway():
    return filedialog.askopenfilename()

def resultpathway():
    return filedialog.askdirectory()
def converter():
    try:
        targettedfile = targetpathway()
        resultpath = resultpathway()

        docx2pdf.convert(targettedfile,resultpath)
        messagebox.showinfo("DOCX2PDF CONVERTER",f"File saved.\nSaved file path: {resultpath}")
    except Exception as e:
        messagebox.showerror("Error","Unsupported format.\nplease make sure you have choosed .docx file. ")

baslik = Label(app,text="EASY DOCX PDF CONVERTER",font ="arial 13 bold",bg="cyan").pack()

convertbutton = ttk.Button(app,text="CONVERT",command=converter).place(x=87,y=60)






app.mainloop()
