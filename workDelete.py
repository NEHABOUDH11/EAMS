import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t = tkinter.Tk()
t.geometry('1200x1200')
t.config(bg='light blue')

def workDelete():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()

    x=a.get() 
        
    s="delete from wplan where Planid='%s'"%(x)
    cur.execute(s)
    db.commit()
    messagebox.showinfo("Data Delete","Deleted..")
    a.delete(0,100)
    db.close()
    
    
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='company')
    cur=db.cursor()
    x=[]
    s="select Planid from wplan" 
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
    s="select Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday from wplan where Planid = '%s' "%(x)
    cur.execute(s)
    data=cur.fetchone()
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e7.delete(0,100)
    e8.delete(0,100)
    
    e2.insert(0,data[0])
    e3.insert(0,data[1])  
    e4.insert(0,data[2])
    e5.insert(0,data[3])
    e6.insert(0,data[4])
    e7.insert(0,data[5])
    e8.insert(0,data[6])
    db.close()


    
l1 = Label(t, text='WORK PLAN DATA', fg='grey', bg='light yellow',
           font=('Arial', 20), width=40, height=1)
l1.place(x=300, y=50)
l2 = Label(t, text='Plan Id :', font=('Times new roman', 20))
l2.place(x=120, y=120)
a=ttk.Combobox(t, width=50)
a.place(x=400,y=120, height=30)
data=filldata()
a['values']=data

l3 = Label(t, text='Sunday :', font=('Times new roman', 20))
l3.place(x=120, y=180)
e2 = Entry(t, width=50)
e2.place(x=400, y=180, height=30)

l4 = Label(t, text='Monday :', font=('Times new roman', 20))
l4.place(x=120, y=240)
e3 = Entry(t, width=50)
e3.place(x=400, y=240, height=30)

l4 = Label(t, text='Tuesday :', font=('Times new roman', 20))
l4.place(x=120, y=300)
e4 = Entry(t, width=50)
e4.place(x=400, y=300, height=30)

l5 = Label(t, text='Wednesday :', font=('Times new roman', 20))
l5.place(x=120, y=360)
e5 = Entry(t, width=50)
e5.place(x=400, y=360, height=30)

l6 = Label(t, text='Thursday :', font=('Times new roman', 20))
l6.place(x=120, y=420)
e6 = Entry(t, width=50)
e6.place(x=400, y=420, height=30)

l7 = Label(t, text='Friday :', font=('Times new roman', 20))
l7.place(x=120, y=490)
e7 = Entry(t, width=50)
e7.place(x=400, y=490, height=30)

l8 = Label(t, text='Saturday :', font=('Times new roman', 20))
l8.place(x=120, y=550)
e8 = Entry(t, width=50)
e8.place(x=400, y=550, height=30)

bt19 = Button(t, text='DELETE', width=40, height=1,font=('Times new roman',15),command=workDelete)
bt19.place(x=500, y=590)
bt20 = Button(t, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
bt20.place(x=500, y=650)
t.mainloop()