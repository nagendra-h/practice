from tkinter import *
from add1 import adds
from update import upd
from delete import dels
from view import vw
import time
import os
from PIL import ImageTk,Image

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1750x900+0+0")
        self.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        self.root.config(bg="black")

        title=Label(self.root,text="Placement Management  System",compound=LEFT,font=("times new roman",40,"bold"),bg="black",fg="red").place(x=0,y=0,relwidth=1,height=70)
#############  time
        self.b_title=Label(self.root,text="Welcome   \t\tDate=DD:MM:YYYY\t\tTime=II:MM:SS:P",font=("times new roman",10,"bold"),bg="brown",fg="red")
        self.b_title.place(x=0,y=70,relwidth=1,height=30)
        self.update_time()


        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=300,height=700)

        self.MenuLogo=Image.open("images/rvclg.jpeg")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenuLogo=Label(leftmenu,image=self.MenuLogo)
        LeftMenuLogo.pack(side=TOP,fill=X)

        lab_menu=Label(leftmenu,text="MENU",font=("times new roman",10),bg="#009688").pack(side=TOP,fill=X)

        btn_emp=Button(leftmenu,text="ADD",command=self.addsd,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

        btn_pro=Button(leftmenu,text="UPDATE",command=self.update1,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

        btn_sup=Button(leftmenu,text="DELETE",command=self.del1,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

        btn_bill=Button(leftmenu,text="VIEW",command=self.view1,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)

        btn_exit=Button(leftmenu,text="EXIT",command=self.logout,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w").pack(side=TOP,fill=X)



########## add +++++++++++++++
    def addsd(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=adds(self.new_win)

    #######++++++++ update +++++++++
    def update1(self):
        self.new_win=Toplevel(self.root)
        self.new_o2=upd(self.new_win)
    # ++++++++++++++ delete ++++++++++
    def del1(s):
        s.new_win=Toplevel(s.root)
        s.new_o2=dels(s.new_win)

########### ++++++ view ++++++++
    def view1(s):
        s.new_win=Toplevel(s.root)
        s.new_o2=vw(s.new_win)

############ time ++++++++
    def  update_time(self):        
        tim=time.strftime("%I:%M:%S%p")
        dat=time.strftime("%d:%m:%Y")
        self.b_title.config(text=f"Welcome \t\tDate: {str(dat)}\t\t Time: {str(tim)}")
        self.b_title.after(200,self.update_time)

    # ++++++++ logout ++++++++++

    def logout(self):
        self.root.destroy()
        

        

if  __name__=="__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()
