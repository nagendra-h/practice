from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox as ms


class adds:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x530+290+170")
        self.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        self.root.config(bg="white")
        self.root.focus_force()

        ####---------- ALL VARIABLES---
         
        self.var_user_id=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_mobileno=StringVar()
        self.var_email=StringVar()
        self.var_company=StringVar()
        self.var_status=StringVar()

        

        

        ##--------EMP ENTERIES-----------
##-----------   USER_ID--------
        user_emp=Label(self.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        user_emp.place(x=11,y=10,height=40,width=110)
        ##-----------   NAME--------
        name_emp=Label(self.root,text="Name",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        name_emp.place(x=611,y=10,height=40,width=110)
        ##-----------   DOB--------
        doj_emp=Label(self.root,text="Doj",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        doj_emp.place(x=11,y=80,height=40,width=110)
        ##-----------   MOBILE_NO--------
        mob_emp=Label(self.root,text="Mobile no",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        mob_emp.place(x=611,y=80,height=40,width=110)
        ##-----------EMAIL--------
        pass_emp=Label(self.root,text="Email",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        pass_emp.place(x=11,y=150,height=40,width=110)
        ##-----------COMPANY--------
        utype_emp=Label(self.root,text="Comapny",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_emp.place(x=611,y=150,height=40,width=110)

        ##-----------STATUS--------
        utype_emp=Label(self.root,text="Status",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_emp.place(x=11,y=210,height=40,width=110)




        ###---------ENTRY -----------
        user_Eemp=Entry(self.root,textvariable=self.var_user_id,font=("times new roman" ,15),bg="white",bd=4)
        user_Eemp.place(x=150,y=10,height=40,width=210)

        ###---------NAME -----------
        nam_Eemp=Entry(self.root,textvariable=self.var_name,font=("times new roman" ,15),bg="white",bd=4)
        nam_Eemp.place(x=771,y=10,height=40,width=210)

        ###---------DOB -----------
        self.doj_Eemp=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="white",bd=4)
        self.doj_Eemp.place(x=150,y=80,height=40,width=200)
        
            
        
        ###---------MOBILE_NO -----------
        mob_Eemp=Entry(self.root,textvariable=self.var_mobileno,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        mob_Eemp.place(x=771,y=80,height=40,width=210)

        ###---------EMAIL -----------
        pass_Eemp=Entry(self.root,textvariable=self.var_email,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        pass_Eemp.place(x=150,y=150,height=40,width=210)

        ###---------COMPANY -----------
        utype_Eemp=Entry(self.root,textvariable=self.var_company,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        utype_Eemp.place(x=771,y=150,height=40,width=210)

        ###---------STATUS -----------
        utype_Eemp=Entry(self.root,textvariable=self.var_status,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        utype_Eemp.place(x=150,y=210,height=40,width=210)
      #+++++++++++ BUTTON +++++++++++++++++  
        add_emp=Button(self.root,text="ADD",command=self.add,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
        add_emp.place(x=380,y=250,height=40,width=110)

        add_emp=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman" ,15),bg="#4caf50",fg="grey",bd=4)
        add_emp.place(x=580,y=250,height=40,width=110)




    ### ++++++++ ADD FUNCTION +++++++++++++++

    def add(self):
        con=sqlite3.connect(database=r'stud.db')
        print(11)
        cur=con.cursor()
        try:
            print(1)
            if self.var_user_id.get()=="":
                ms.showerror("Error","User_id must be required ",parent=self.root)
            else:
                cur.execute("Select * from student where user_id=?",(self.var_user_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    ms.showerror("Error","This user_id already there ",parent=self.root)
                else:
                    print(3)
                    cur.execute("Insert into student(user_id,name,dob,mobileno,email,company,status) values(?,?,?,?,?,?,?)",(
                        self.var_user_id.get(),
                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_mobileno.get(),
                        self.var_email.get(),
                        self.var_company.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    ms.showinfo("Success","Employee added successfully",parent=self.root)
                    print("done")
                    
                   
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)

#############--------------CLEAR--------------
    
    def clear(self):
        self.var_user_id.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_mobileno.set("")
        self.var_email.set("")
        self.var_company.set("")
        self.var_status.set("")
        



        



if  __name__=="__main__":
     root=Tk()
     obj=adds(root)
     root.mainloop()
