import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t = tkinter.Tk()
t.geometry('1200x1200')
t.config(bg='light blue')

def holiDelete():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()
    e2.delete(0,100)
    e3.delete(0,100)
        
    x=a.get()
        
    s="delete from HMaster where Hid='%s'"%(x)
    cur.execute(s)
    db.commit()
    messagebox.showinfo("Data Delete","Deleted..")
    a.delete(0,100)
    db.close()
    
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()
    x=[]
    s="select Hid from HMaster" 
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
    s="select Hname,Date from HMaster where Hid = '%s' "%(x)
    cur.execute(s)
    data=cur.fetchone()
    e2.delete(0,100)
    e3.delete(0,100)
    e2.insert(0,data[0])
    e3.insert(0,data[1])  
    db.close() 


    
l1 = Label(t, text='HOLIDAY MASTER DATA', fg='grey', bg='light yellow',
           font=('Arial', 20), width=40, height=1)
l1.place(x=300, y=50)
l2 = Label(t, text='Holiday Id :', font=('Times new roman', 20))
l2.place(x=120, y=120)
a=ttk.Combobox(t, width=50)
a.place(x=400,y=120, height=30)
data=filldata()
a['values']=data

l3 = Label(t, text='Holiday Name :', font=('Times new roman', 20))
l3.place(x=120, y=180)
e2 = Entry(t, width=50)
e2.place(x=400, y=180, height=35)

l4 = Label(t, text='Date Of Holiday :', font=('Times new roman', 20))
l4.place(x=120, y=240)
e3 = Entry(t, width=50)
e3.place(x=400, y=240, height=35)

bt15 = Button(t, text='DELETE', width=40, height=1, font=('Times new roman',15), command = holiDelete)
bt15.place(x=400, y=450)
bt16 = Button(t, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
bt16.place(x=400, y=500)

t.mainloop()
    