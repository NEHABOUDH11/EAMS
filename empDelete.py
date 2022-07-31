import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t = tkinter.Tk()
t.geometry('1200x1200')
t.config(bg='light blue')
def empDelete():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()
  
    x=a.get()
    
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
        
    s="delete from employee where empid='%s'" %(x)
    cur.execute(s)
    db.commit()
    messagebox.showinfo("Data Delete","Deleted..")
    a.delete(0,100)
    db.close()
    
def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select empid from employee" 
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
    s="select ename,address,Phone,email,deptid from employee where empid= '%s' "%(x)
    cur.execute(s)
    data=cur.fetchone()
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e2.insert(0,data[0])
    e3.insert(0,data[1])
    e4.insert(0,data[2]) 
    e5.insert(0,data[3])
    e6.insert(0,data[4])
    db.close()




l1 = Label(t, text='EMPLOYEE DATA', fg='grey', bg='light yellow',
           font=('Arial', 20), width=40, height=1)
l1.place(x=300, y=50)
l2 = Label(t, text='Employee Id :', font=('Times new roman', 20))
l2.place(x=120, y=120)
a=ttk.Combobox(t, width=50)
a.place(x=350,y=120, height=30)
data=filldata()
a['values']=data
#e1 = Entry(t, width=50)
#e1.place(x=350, y=120, height=30)

l3 = Label(t, text='Employee Name :', font=('Times new roman', 20))
l3.place(x=120, y=180)
e2 = Entry(t, width=50)
e2.place(x=350, y=180, height=30)

l4 = Label(t, text='Address :', font=('Times new roman', 20))
l4.place(x=120, y=240)
e3 = Entry(t, width=50)
e3.place(x=350, y=240, height=30)

l4 = Label(t, text='Phone No. :', font=('Times new roman', 20))
l4.place(x=120, y=300)
e4 = Entry(t, width=50)
e4.place(x=350, y=300, height=30)

l5 = Label(t, text='Email :', font=('Times new roman', 20))
l5.place(x=120, y=360)
e5 = Entry(t, width=50)
e5.place(x=350, y=360, height=30)

l6 = Label(t, text='Department Id :', font=('Times new roman', 20))
l6.place(x=120, y=420)
e6 = Entry(t, width=50)
e6.place(x=350, y=420, height=30)

bt4 = Button(t, text='DELETE', width=40, height=1, font=('Times new roman',15), command = empDelete)
bt4.place(x=500, y=550)
bt5 = Button(t, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
bt5.place(x=500, y=620)

t.mainloop()