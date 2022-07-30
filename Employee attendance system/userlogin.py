import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
import datetime

def fronttwo():

    t = tkinter.Tk()
    t.geometry('1550x900')
    t.config(bg='light blue')


    
    def Ok():
        
        uname=e1.get()
        password=e2.get() 
        
        if(uname=="" and password==""):
            messagebox.showinfo("","Blank Not Allowed")
            
        elif(uname=="Test" and password=="abcd"): 
            
            messagebox.showinfo("","Login Success")
              
        else:
           db = pymysql.connect(host='localhost', user='root',
                                password='root', database='company')
           cur = db.cursor()
           
           a = e1.get()
           b = e2.get()
           c= e3.get()
           s = "insert into ams values('%s','%s','%s')"%(a,b,c)
           cur.execute(s)
           db.commit()
           messagebox.showinfo("login success", "Your Attendance has been marked")
           e1.delete(0, 100)
           e2.delete(0, 100)
           
           db.close()
      
            
        
        
    def clear():
        t.destroy()
    
    
         
    '''
    def forg():
        t = tkinter.Tk()
        t.geometry('700x700')
        t.config(bg='light blue')
        t.title('Forgot Password Screen')
    
        l4 = Label(t, text='New Password :', font=('Lucida Handwriting', 20))
        l4.place(x=350, y=220)
        e3 = Entry(t, width=50)
        e3.place(x=760, y=220,height=35)
        
        l5 = Label(t, text='Confirm Password :', font=('Lucida Handwriting', 20))
        l5.place(x=350, y=330)
        e4 = Entry(t, width=50)
        e4.place(x=760, y=330,height=35)
        
        bt4=Button(t,text='SAVE',font=('Lucida Handwriting',20),command=Insert)
        bt4.place(x=580,y=440)
    '''    
        
    
    

    
    
    l1 = Label(t, text='USER LOGIN PAGE', font=('Times new Roman', 20),
               fg='grey', bg='light yellow', width=50, height=1)
    l1.place(x=350, y=50)
    l2 = Label(t, text='Username :', font=('Times new roman', 20))
    l2.place(x=450, y=220)
    e1 = Entry(t, width=50)
    e1.place(x=650, y=220, height=35)
    l3 = Label(t, text='Password :', font=('Times New Roman', 20))
    l3.place(x=450, y=330)
    e2 = Entry(t, width=50, show='*')
    e2.place(x=650, y=330, height=35)
    
    d = datetime.datetime.now()

    
    e3 = Entry(t, width=50,font=('Times new roman',20))
    e3.place(x=1, y=1, height=35)
    e3.insert(END, d.strftime('%Y-%m-%d  %A %H:%M:%S'))
    
    
    bt1 = Button(t, text='OK', font=('Times New Roman', 15),command=Ok)
    bt1.place(x=580, y=440)
    bt2 = Button(t, text='CANCEL', font=('Times New Roman', 15),command=clear) 
    bt2.place(x=690, y=440) 
    '''bt4 = Button(t, text='FORGOT PASSWORD', font=('Times New Roman', 15),command=forg) 
    bt4.place(x=750, y=540) '''
    t.mainloop()
