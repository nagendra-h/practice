from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox as ms


class dels:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x530+290+170")
        self.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        self.root.config(bg="white")
        self.root.focus_force()

        ####---------- ALL VARIABLES---
        self.search=StringVar()  
        self.var_user_id=StringVar()


        #++++++++++++ search frame ++++++++++
        searc=LabelFrame(self.root,text="Search Product",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
        searc.place(x=310,y=0,width=600,height=100)

        # ++++++++ options +++++++
        cmb_cat=ttk.Combobox(searc,textvariable=self.search,values=("Select","Student number","Student name","Company"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
        cmb_cat.place(x=0,y=0)
        cmb_cat.current(0)
        txtsearch=Entry(searc,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=230,y=10,width=180)

        btsearch=Button(searc,text="search",font=("goudy old style",15,"bold"),bg="lightyellow",cursor="hand2").place(x=440,y=10,height=30,width=120)

        title=Label(self.root,text="Student details",font=("goudy old style",15,"bold"),bg="brown").place(x=20,y=140,width=1000)


        ##--------EMP ENTERIES-----------
##-----------   USER_ID--------
        user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        user_emp.place(x=11,y=180,height=40,width=110)

        ###---------ENTRY -----------
        user_Eemp=Entry(self.root,textvariable=self.var_user_id,font=("times new roman" ,15),bg="white",bd=4)
        user_Eemp.place(x=271,y=180,height=40,width=210)


        #+++++++++++ BUTTON +++++++++++++++++  
        add_emp=Button(self.root,text="DELETE",command=self.del11,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
        add_emp.place(x=330,y=450,height=40,width=110)

    def del11(self):
        con=sqlite3.connect(database=r'stud.db')
        cur=con.cursor()
        try:
                if self.var_user_id.get()=="":
                    ms.showerror("Error","User_id must be required ",parent=self.root)
                else:
                    cur.execute("Select * from student where user_id=?",(self.var_user_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        ms.showerror("Error","INVALID  user_id  ",parent=self.root)
                    else:
                        op=ms.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                        cur.execute("delete from student where user_id=?",(self.var_user_id.get(),))
                        if op==True:
                            con.commit()
                            ms.showinfo("Success","student deleted successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)                    




if  __name__=="__main__":
     root=Tk()
     obj=dels(root)
     root.mainloop()
