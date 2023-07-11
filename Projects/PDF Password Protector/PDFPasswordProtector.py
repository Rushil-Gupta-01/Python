from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

root = Tk()
root.title("PDF Protector")
root.geometry("600x400+300+100")
root.resizable(False,False)


def browsesourcefile():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select your source file...",filetype=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END, filename)


    
def encrypt():
    mainfile=sourcefile.get()
    protectfile=targetfile.get()
    code=password.get()

    if mainfile=="" and protectfile=="" and code=="":
        messagebox.showerror("Invalid","All enteries are empty!!")
    
    elif mainfile=="":
        messagebox.showerror("Invalid","Please type source PDF filename!")

    elif protectfile=="":
        messagebox.showerror("Invalid","Please type the new name for the file!")

    elif code=="":
        messagebox.showerror("Invalid","Please type the password for the file!")

    else:
        try:
            output=PdfFileWriter()
            file=PdfFileReader(filename)
            num = file.numPages

            for idx in range(num):
                page=file.getPage(idx)
                output.addPage(page)

            output.encrypt(code)
            with open(protectfile, "wb") as f:
                output.write(f)

        except:
            messagebox.showerror("Invalid","Invalid Entry!!")

#Icon
image_icon = PhotoImage(file='C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\icon.png')
root.iconphoto(False,image_icon)

#Main
Top_image = PhotoImage(file="C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\bannerz.png")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10,y=110)

########
sourcefile= StringVar()
Label(frame,text="Source PDF File: ",font="king 12 normal",fg="#4c4542").place(x=30,y = 30)
entry1 = Entry(frame,width=20,textvariable=sourcefile,font="king 17",bd=1)
entry1.place(x=200,y=28)

Button_icon = PhotoImage(file="C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\folder.png")
Button(frame,image=Button_icon,width=35,height=24,bg="#d3cdcd",command=browsesourcefile).place(x=500, y=27)

##########
targetfile = StringVar()
Label(frame,text="Target PDF File: ",font="king 12 normal",fg="#4c4542").place(x=30,y = 80)
entry2 = Entry(frame,width=20,textvariable=targetfile,font="king 17",bd=1)
entry2.place(x=200,y=80)





########
password = StringVar()
Label(frame,text="Set User Password: ",font="king 12 normal",fg="#4c4542").place(x=15,y = 130)
entry3 = Entry(frame,width=20,textvariable=password,font="king 17",bd=1)
entry3.place(x=200,y=130)

#######
button_icon = PhotoImage(file="C:\\Users\\india\\Desktop\\Python\\Projects\\PDF Password Protector\\icon.png")
protect=Button(root,text="Protect PDF File",compound=LEFT,image=button_icon,width=230,height=50,bg="#bfb9b9",font="king 14",command=encrypt)
protect.pack(side=BOTTOM,pady=40)


Label(frame,text="*File would be stored in C:\\Users\\india\\Desktop\\.exe ",font="king 12 normal",fg="#4c4542").place(x=15,y = 250)

root.mainloop()