## importing necessary libraries
import re
import getpass
import cv2
import time
from tkinter import *
from tkinter import messagebox

## listing emails and password 
em = ["mridul.agrawal@intelegencia.com","anant.bharadwaj@intelegencia.com","ashish.rana@intelegencia.com","vivek.sharma@intelegencia.com","karuna.munjal@intelegencia.com","manish.pathak@intelegencia.com"]
ps = ["Mridul@123","Anant@123","Ashish@123","Vivek@123","Karuna@123","Manish@123"]

## check for valid email
def valid_email(email):
    
    if email.count("@") >  1:
        return False
    if email.count(".") >  2:
        return False
        
    x = re.search(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',email)
    if x:
        return True
    else:
        return False

## check for valid password    
def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    #if val:
    return val

## capture and show image
def capture():
    
    l = []## define list to store frames
    cam = cv2.VideoCapture(0)

    while True:
    
        ret, frame = cam.read()
        l.append(frame)
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Say Cheeze", frame)

        k = cv2.waitKey(1)
        
        if len(l) < 70:
            pass
        else:
            img_name = "image.png"
            cv2.imwrite(img_name, l[68])
            break

    cam.release()

    img = cv2.imread("image.png",1)
    cv2.imshow("pic",img)
    cv2.waitKey(4000)## wait for four seconds

    cv2.destroyAllWindows()

## this function will be executed when login button is clicked  
def log_fun():
    username = e1.get()
    password = e2.get()

    if valid_email(username) and password_check(password):
        
        if username in em:
            
            x = em.index(username)
            if  password == ps[x]:

                messagebox.showinfo("","Login Success")
                if messagebox.askyesno("","Do You Want to open Camera"):
                    #root.destroy()
                    capture()
                    if not messagebox.askyesno("","Do You Want to Exit"):
                        pass
                    else:
                        root.destroy()
            else:
                messagebox.showinfo("","Email and Password does not match with our records")
        
        else:
            messagebox.showinfo("","Email and Password does not match with our records")

    else:
        messagebox.showinfo("","please enter valid email and password")
        
# partly done by ashish rana
# Tkinter Window Cofiguration
root = Tk()  
root.geometry('1080x2150')
root.title("Image Capture App")
root.configure(bg="white")

root.attributes('-fullscreen',True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen",not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

# Adding comapny logo
img=PhotoImage(file="logo.png")
Label(root,image=img,bg="white").place(x=8,y=9)

# Labeling and Entry of Email Id'd and Password
global e1
global e2

Frame(root,bg='white').place(x=60,y=200,height=280,width=430)

Label(root,text="Username",font=("Times",15,"bold"),fg="red",bg="white").place(x=90,y=210)
Label(root,text="Password",font=("Times",15,"bold"),fg="red",bg="white").place(x=90,y=290)

Label(root,text="Welcome, we have clicked many stars \n Sign in to add one more.",font=("Helvetica",25,"bold"),fg="red",bg="white").place(x=300,y=80)

e1 = Entry(root,font=("Helvetica",12),bg="white")
e1.place(x=90,y=240,width=350,height=35)

e2 = Entry(root,text="Enter Password",font=("Helvetica",12),bg="white")
e2.place(x=90,y=320,width=350,height=35)
# e2.config(show="*")
e2['show'] = "*"

# Background image Configuration
sideimg=PhotoImage(file="background.png")
Label(root,image=sideimg,borderwidth=0).place(x=670,y=189)

# Login Button 
login_btn= PhotoImage(file="login button.png")
loginbtn=Button(root,command=log_fun,borderwidth=0,image=login_btn).place(x=90,y=390)

root.mainloop()
