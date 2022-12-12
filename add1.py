from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox as ms
from PIL import ImageTk,Image


class adds:
    def __init__(s,root):
        s.root=root
        s.root.geometry("1530x850+380+172")
        s.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        s.root.config(bg="white")
        s.root.focus_force()

        ####---------- ALL VARIABLES---
         
        s.var_user_id=StringVar()
        s.var_name=StringVar()
        s.var_dob=StringVar()
        s.var_mobileno=StringVar()
        s.var_email=StringVar()
        s.var_company=StringVar()
        s.var_status=StringVar()

        
        title=Label(s.root,text="Student details",font=("goudy old style",25),bg="brown").place(x=40,y=50,width=1300)


        

           ##--------EMP ENTERIES-----------
##-----------   USER_ID--------
        user_emp=Label(s.root,text="User_id",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        user_emp.place(x=61,y=190,height=40,width=110)
        ##-----------   NAME--------
        name_emp=Label(s.root,text="Name",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        name_emp.place(x=611,y=190,height=40,width=110)
        ##-----------   DOB--------
        doj_emp=Label(s.root,text="Dob",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        doj_emp.place(x=61,y=250,height=40,width=110)
        ##-----------   MOBILE_NO--------
        mob_emp=Label(s.root,text="Mobile no",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        mob_emp.place(x=611,y=250,height=40,width=110)
        ##-----------EMAIL--------
        pass_emp=Label(s.root,text="Email",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        pass_emp.place(x=61,y=320,height=40,width=110)
        ##-----------COMPANY--------
        utype_emp=Label(s.root,text="Comapny",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_emp.place(x=611,y=320,height=40,width=110)

        ##-----------STATUS--------
        utype_emp=Label(s.root,text="Status",font=("times new roman" ,15, "bold"),fg="#FFFDD0",bg="#7E481C",bd=3)
        utype_emp.place(x=61,y=390,height=40,width=110)




        ###---------ENTRY -----------
        user_Eemp=Entry(s.root,textvariable=s.var_user_id,font=("times new roman" ,15),bg="white",bd=4)
        user_Eemp.place(x=271,y=190,height=40,width=210)

        ###---------NAME -----------
        nam_Eemp=Entry(s.root,textvariable=s.var_name,font=("times new roman" ,15),bg="white",bd=4)
        nam_Eemp.place(x=771,y=190,height=40,width=210)

        ###---------DOB -----------
        s.doj_Eemp=Entry(s.root,textvariable=s.var_dob,font=("times new roman",15),bg="white",bd=4)
        s.doj_Eemp.place(x=271,y=250,height=40,width=200)
        
            
        
        ###---------MOBILE_NO -----------
        mob_Eemp=Entry(s.root,textvariable=s.var_mobileno,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        mob_Eemp.place(x=771,y=250,height=40,width=210)

        ###---------EMAIL -----------
        pass_Eemp=Entry(s.root,textvariable=s.var_email,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        pass_Eemp.place(x=271,y=320,height=40,width=210)

        ###---------COMPANY -----------
        utype_Eemp=Entry(s.root,textvariable=s.var_company,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        utype_Eemp.place(x=771,y=320,height=40,width=210)

        ###---------STATUS -----------
        utype_Eemp=Entry(s.root,textvariable=s.var_status,font=("times new roman" ,15),fg="black",bg="white",bd=4)
        utype_Eemp.place(x=281,y=390,height=40,width=210)
      #+++++++++++ BUTTON +++++++++++++++++  
        add_emp=Button(s.root,text="ADD",command=s.add,font=("times new roman" ,15),bg="#b33c00",fg="black",bd=4)
        add_emp.place(x=611,y=390,height=40,width=110)

        clear_emp=Button(s.root,text="CLEAR",command=s.clear,font=("times new roman" ,15),bg="#b33c00",fg="black",bd=4)
        clear_emp.place(x=771,y=390,height=40,width=110)


        p_frame=Frame(s.root,bd=0,relief=RIDGE,bg="PINK")
        p_frame.place(x=270,y=500,width=670,height=270)

        s.MenuLogo=Image.open("images/rvclg.jpeg")
        s.MenuLogo=s.MenuLogo.resize((670,270),Image.ANTIALIAS)
        s.MenuLogo=ImageTk.PhotoImage(s.MenuLogo)

        s.LeftMenuLogo=Label(p_frame,image=s.MenuLogo,bg="navy")
        s.LeftMenuLogo.pack(side=TOP,fill=BOTH)



    ### ++++++++ ADD FUNCTION +++++++++++++++

    def add(s):
        con=sqlite3.connect(database=r'stud.db')
        print(11)
        cur=con.cursor()
        try:
            print(1)
            if s.var_user_id.get()=="":
                ms.showerror("Error","User_id must be required ",parent=s.root)
            else:
                cur.execute("Select * from student where user_id=?",(s.var_user_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    ms.showerror("Error","This user_id already there ",parent=s.root)
                else:
                    print(3)
                    cur.execute("Insert into student(user_id,name,dob,mobileno,email,company,status) values(?,?,?,?,?,?,?)",(
                        s.var_user_id.get(),
                        s.var_name.get(),
                        s.var_dob.get(),
                        s.var_mobileno.get(),
                        s.var_email.get(),
                        s.var_company.get(),
                        s.var_status.get()
                    ))
                    con.commit()
                    ms.showinfo("Success","Employee added successfully",parent=s.root)
                    s.image()
                    
                   
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=s.root)

#############--------------CLEAR--------------
    
    def clear(s):
        s.var_user_id.set("")
        s.var_name.set("")
        s.var_dob.set("")
        s.var_mobileno.set("")
        s.var_email.set("")
        s.var_company.set("")
        s.var_status.set("")
        s.MenuLog=Image.open("images/rvclg.jpeg")
        s.MenuLog=s.MenuLog.resize((670,270),Image.ANTIALIAS)
        s.MenuLog=ImageTk.PhotoImage(s.MenuLog)
        s.LeftMenuLogo.config(image=s.MenuLog)

########## IMAGE +++++++++++++++++
    def image(s):
        try:
            if s.var_company.get()=="Infosys":
                s.MenuL=Image.open("images/info.jpg")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)
            elif  s.var_company.get()=="Wipro":
                s.MenuL=Image.open("images/wipro.png")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)
            elif  s.var_company.get()=="Amazon":
                s.MenuL=Image.open("images/az.jpg")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)
            elif  s.var_company.get()=="Flipcart":
                s.MenuL=Image.open("images/fp.jpeg")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)
            elif  s.var_company.get()=="Google":
                s.MenuL=Image.open("images/gg.jpg")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)
            elif  s.var_company.get()=="Phone pay":
                s.MenuL=Image.open("images/pp.jpeg")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)

            elif  s.var_company.get()=="Reliance":
                s.MenuL=Image.open("images/re.png")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)

            elif  s.var_company.get()=="Tcs":
                s.MenuL=Image.open("images/tcs.jpeg")
                s.MenuL=s.MenuL.resize((670,270),Image.ANTIALIAS)
                s.MenuL=ImageTk.PhotoImage(s.MenuL)
                s.LeftMenuLogo.config(image=s.MenuL)

            else:
                s.MenuLog=Image.open("images/rvclg.jpeg")
                s.MenuLog=s.MenuLog.resize((670,270),Image.ANTIALIAS)
                s.MenuLog=ImageTk.PhotoImage(s.MenuLog)
                s.LeftMenuLogo.config(image=s.MenuLog)
                            
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=s.root)
        



        



if  __name__=="__main__":
     root=Tk()
     obj=adds(root)
     root.mainloop()
