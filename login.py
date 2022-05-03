from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox 
from student import Student
import os
import subprocess
class log:
    def __init__(s,root):
        s.root=root
        s.root.geometry("1350x700+0+0")
        s.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")

        lm=Frame(s.root,bd=2,relief=RIDGE,bg="white")
        lm.place(x=300,y=102,width=500,height=400)

        s.user_id=StringVar()
        s.password=StringVar()
        
    ########### ++++++ LABEL ++++++++++++++++
        user_stud=Label(lm,text="User_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        user_stud.place(x=11,y=30,height=40,width=110)
        
        doj_stud=Label(lm,text="Password",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        doj_stud.place(x=11,y=90,height=40,width=110)

    ####### + ENTRY +++++++++
        s.user_stud=Entry(lm,textvariable=s.user_id,font=("times new roman" ,15),bg="white",bd=4)
        s.user_stud.place(x=150,y=30,height=40,width=210)

        s.pwd_stud=Entry(lm,textvariable=s.password,show='*',font=("times new roman",15),bg="white",bd=4)
        s.pwd_stud.place(x=150,y=90,height=40,width=200)

        s.btn_emp=Button(lm,text="LOGIN",command=s.login1,compound=LEFT,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",anchor="w")
        s.btn_emp.place(x=180,y=250,height=40,width=110)

    def login1(self): 
        con=sqlite3.connect(database=r'stud.db')
        cur=con.cursor()
        try:
            if self.user_stud.get() == "" and  self.pwd_stud.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                cur.execute("select name from admin where user_id=? and password=?",(self.user_stud.get(),self.pwd_stud.get()))
                user=cur.fetchone()
                if user==None:    
                    messagebox.showerror('Invalid credentials', 'Try again with the correct credentials!!!!')
                if  user==('admin',):
                    try:
                        
                        subprocess.run(['python3','student.py'])
                        
                        
                    finally:
                       self.root.destroy() 
                    
                else:
                    messagebox.showerror("Error", "Cannot access",parent=self.root)
       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)



if  __name__=="__main__":
     root=Tk()
     obj=log(root)
     root.mainloop()
