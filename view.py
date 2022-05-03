from tkinter import *
from tkinter import ttk
from tkcalendar import  Calendar,DateEntry
import sqlite3
from tkinter import messagebox as ms


class vw:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x530+290+170")
        self.root.title("PLACEMENT MANAGEMENT SYSTEM | MCA STUDENTS")
        self.root.config(bg="white")
        self.root.focus_force()

        ####---------- ALL VARIABLES---
        self.search=StringVar()  
        self.var_user_id=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_mobileno=StringVar()
        self.var_email=StringVar()
        self.var_company=StringVar()
        self.var_status=StringVar()




        st=ttk.Style()
        st.theme_use("clam")
        


       
        
        view_emp=Frame(self.root,bd=3,relief=RIDGE)
        view_emp.place(x=0,y=0,relwidth=1,height=400)

        scrolly=Scrollbar(view_emp,orient=VERTICAL)
        scrollx=Scrollbar(view_emp,orient=HORIZONTAL)


        self.studentTable=ttk.Treeview(view_emp,columns=("useri_id","name","dob","mobileno","email","company","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)
        
        
        
        self.studentTable.heading("useri_id",text="USER_ID")
        self.studentTable.heading("name",text="NAME")
        self.studentTable.heading("dob",text="DOB")
        self.studentTable.heading("mobileno",text="MOBILE NO")
        self.studentTable.heading("email",text="EMAIL")
        self.studentTable.heading("company",text="COMPANY")
        self.studentTable.heading("status",text="STATUS")



        self.studentTable["show"]="headings"


        self.studentTable.column("useri_id",width=90)
        self.studentTable.column("name",width=100)
        self.studentTable.column("dob",width=100)
        self.studentTable.column("mobileno",width=100)
        self.studentTable.column("email",width=100)
        self.studentTable.column("company",width=100)
        self.studentTable.column("status",width=100)

        self.studentTable.pack(fill=BOTH,expand=1)
       # self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        st.configure("Treeview",
                  background="grey",
                  foregroung="#FF2800",
                  rowheight=25,
                  fieldbackground="#997950"
                  )
        st.map("Treeview",background=[("selected","navy")])
        
        

    def show(self):
        con=sqlite3.connect(database=r'stud.db')
        cur=con.cursor()
        try:
                
          global c
          c=0
          self.studentTable.tag_configure('oddrow',background="#7C4700")
          self.studentTable.tag_configure('evrow',background="#808588")
          cur.execute("select * from student")
          rows=cur.fetchall()
          self.studentTable.delete(*self.studentTable.get_children())
          for row in rows:
              if c % 2 == 0:
                      self.studentTable.insert('',END,values=row,tags=('oddrow',))
              else:
                      self.studentTable.insert('',END,values=row,tags=('evrow',))
              c +=1
          
        except Exception as ex:
            ms.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)











if  __name__=="__main__":
     root=Tk()
     obj=vw(root)
     root.mainloop()
