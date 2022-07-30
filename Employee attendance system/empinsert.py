import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql

def Empone():
    

    def empInsert():
        if len(e1.get())==0:
            
            e1.config(bg='Red')
            e2.config(bg='Red')
            e3.config(bg='Red')
            e4.config(bg='Red')
            e5.config(bg='Red')
            e6.config(bg='Red')
            messagebox.showwarning("Warning","please fill it all")

        elif len(e2.get())==0:
               e2.config(bg='Red')
               e3.config(bg='Red')
               e4.config(bg='Red')
               e5.config(bg='Red')
               e6.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e3.get())==0:
               
               e3.config(bg='Red')
               e4.config(bg='Red')
               e5.config(bg='Red')
               e6.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e4.get())==0:
               e4.config(bg='Red')
               e5.config(bg='Red')
               e6.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e5.get())==0:
               e5.config(bg='Red')
               e6.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e6.get())==0:
               e6.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        else:
            
                    db = pymysql.connect(host='localhost', user='root',
                                         password='root', database='company')
                    cur = db.cursor()
                    a = e1.get()
                    b = e2.get()
                    c = e3.get()
                    d = e4.get()
                    e = e5.get()
                    f = e6.get()
                    s = "insert into employee values('%s','%s','%s','%s','%s','%s')" % (
                        a, b, c, d, e, f)
                    cur.execute(s)
                    db.commit()
                    messagebox.showinfo("Data saved", "Saved")
                    e1.delete(0, 100)
                    e2.delete(0, 100)
                    e3.delete(0, 100)
                    e4.delete(0, 100)
                    e5.delete(0, 100)
                    e6.delete(0, 100)
                    db.close()
    def correct(inp):
          if inp.isdigit():
              return True
             
          elif inp == "":
              return True
          else:
              return False  
              
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select Deptid from department" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
            
    
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
    
    l1 = Label(c,text='EMPLOYEE DATA', fg='grey', bg='light yellow',
               font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Employee Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    e1 = Entry(c, width=50)
    e1.place(x=350, y=120, height=30)
    
    l3 = Label(c, text='Employee Name :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=350, y=180, height=30)
    
    l4 = Label(c, text='Address :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    e3 = Entry(c, width=50)
    e3.place(x=350, y=240, height=30)
    
    l4 = Label(c, text='Phone No. :', font=('Times new roman', 20))
    l4.place(x=120, y=300)
    e4 = Entry(c, width=50)
    e4.place(x=350, y=300, height=30)
    reg = c.register(correct)
    e4.config(validate="key",validatecommand=(reg,'%P'))
    
    
    l5 = Label(c, text='Email :', font=('Times new roman', 20))
    l5.place(x=120, y=360)
    e5 = Entry(c, width=50)
    e5.place(x=350, y=360, height=30)
    
    l6 = Label(c, text='Department Id :', font=('Times new roman', 20))
    l6.place(x=120, y=420)
    e6=ttk.Combobox(c, width=50)
    e6.place(x=400,y=420, height=30)
    data=filldata()
    e6['values']=data
    
    bt = Button(c, text='SAVE', width=40, height=1,font=('Times new roman',15),command=empInsert)
    bt.place(x=500, y=550)
    
