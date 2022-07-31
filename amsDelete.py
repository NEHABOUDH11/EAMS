import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t = tkinter.Tk()
t.geometry('1200x1200')
t.config(bg='light blue')
def amsDelete():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()
   
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    
    x=a.get()
        
    s="delete from ams  where empid='%s'"%(x)
    cur.execute(s)
    db.commit()
    messagebox.showinfo("Data Delete","Deleted..")
    a.delete(0,100)
    db.close()
    
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()
    x=[]
    s="select empid from ams" 
    cur.execute(s)
    data=cur.fetchall()
    for res in data:
        x.append(res[0])
    return x
    
def finddata():
    db = pymysql.connect(host='localhost', user='root',
                         password='root', database='company')
    cur=db.cursor()
    x=a.get()
    s="select  ename, date , status from ams where empid = '%s' "%(x)
    cur.execute(s)
    data=cur.fetchone()
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e2.insert(0,data[0])
    e3.insert(0,data[1])  
    e4.insert(0,data[2])
    db.close()


    
l1 = Label(t, text='ATTENDANCE MASTER DATA', fg='grey', bg='light yellow',
           font=('Arial', 20), width=40, height=1)
l1.place(x=300, y=50)
l2 = Label(t, text='Employee Id :', font=('Times new roman', 20))
l2.place(x=120, y=120)
a=ttk.Combobox(t, width=50)
a.place(x=400,y=120, height=30)
data=filldata()
a['values']=data
#e1 = Entry(t, width=50)
#e1.place(x=400, y=120, height=35)

l3 = Label(t, text='Employee Name :', font=('Times new roman', 20))
l3.place(x=120, y=180)
e2 = Entry(t, width=50)
e2.place(x=400, y=180, height=35)

l4 = Label(t, text='Date Of Mark :', font=('Times new roman', 20))
l4.place(x=120, y=240)
e3 = Entry(t, width=50)
e3.place(x=400, y=240, height=35)

l4 = Label(t, text='Status :', font=('Times new roman', 20))
l4.place(x=120, y=300)
e4=Spinbox(t,from_=0,to=1,width=50)
e4.place(x=400,y=300,height=35)

bt22 = Button(t, text='DELETE', width=40, height=1,font=('Times new roman',15),command=amsDelete)
bt22.place(x=400, y=450)
bt23 = Button(t, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
bt23.place(x=400, y=550)

t.mainloop()