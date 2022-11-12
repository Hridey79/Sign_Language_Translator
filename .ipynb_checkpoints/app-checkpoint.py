# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2

root = Tk()
root.geometry("700x350")
# label =Label(root)
# label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

root.title('Sign-Language-To-Text')

def show_frames():
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)

show_frames()
root.mainloop()