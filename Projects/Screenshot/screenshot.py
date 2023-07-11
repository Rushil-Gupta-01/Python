from tkinter import *
import customtkinter
import pyautogui
import tkinter as tk 
from tkinter.filedialog import *


#command function
def Click():
    myScreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myScreenshot.save(save_path + "_screenshot.png")



#Main Window properties
window = Tk()
window.title("Screenshort Taker")
window.geometry("400x375")
window.configure(bg="#262626")

img=PhotoImage(file='C:\\Users\\india\\Desktop\\Python\\Projects\\Screenshot\\Icons\\icon2.png')
window.iconphoto(False, img)

myButton = customtkinter.CTkButton(   #Custom Button
    master= window,
    command= Click,
    text= "Screenshot",
    text_font="none 12 bold",
    text_color="#363636",
    hover= True,
    hover_color= "#f2f2f2",
    height=40,
    width= 120,
    border_width=5,
    corner_radius=20,
    border_color= "#d3d3d3", 
    bg_color="#262626",
    fg_color= "#fafafa")


myButton.place(x= 70, y= 100)

#run the main loop
window.mainloop()