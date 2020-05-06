from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
mydb = pymysql.connect(host='localhost', user='root', password='root')
cur = mydb.cursor()

def link2():
    details=Toplevel()
    details.geometry('600x600')

    path=r'C:\Users\drishti agarwal\Documents\GitHub\school-database-software\wallpaper-3.jpg'
    background=ImageTk.PhotoImage(Image.open(path))

    #labels
    wallpaper=Label(details,image=background,height=2000,width=2000)
    wallpaper.image=background
    wallpaper.place(x=0,y=0)

    school_name=Label(details,text='THE PURE VISION INTERNATIONAL SCHOOL',relief=SOLID,
      bg='black',bd=10,fg='white',font=('Times new roman',30,'bold')).place(x=300,y=0)

    heading=Label(details,text='REGISTRATION FORM',bg='purple',bd=10,fg='orange',
                  font=('Times new roman',20,'bold')).place(x=550,y=100)

    student_name=Label(details,text="STUDENT'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=200)

    email=Label(details,text="EMAIL-ID:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=300)

    #entry boxes
    stu_name=Entry(details,width=40)
    stu_name.config(font=10,bd=5)
    stu_name.place(x=301,y=205)

    em=Entry(details,width=40)
    em.config(font=10,bd=5)
    em.place(x=270,y=305)
    
    #functions
    def info():
        details_r= Toplevel()
        details_r.geometry('600x600')
        path1=r'C:\Users\drishti agarwal\Documents\GitHub\school-database-software\wallpaper-3.jpg'
        background=ImageTk.PhotoImage(Image.open(path1))
        


        # ------------------Labels---------------------------
        Wallpaper=Label(details_r,image=background,height=2000,width=2000)
        Wallpaper.image=background
        Wallpaper.place(x=0,y=0)
        school_name=Label(details_r,text='PURE VISION INTERNATIONAL SCHOOL',relief=SOLID,
                       bg='black',bd=10,fg='white',font=('Times new roman',30,'bold')).place(x=300,y=0)

        heading=Label(details_r,text='STUDENTS DETAILS',bg='purple',bd=10,fg='orange',
                       font=('Times new roman',20,'bold')).place(x=550,y=100)

        student_name=Label(details_r,text="STUDENT'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=200)

        fathers_name=Label(details_r,text="FATHER'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=300)

        mothers_name=Label(details_r,text="MOTHER'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=400)

        gender=Label(details_r,text="GENDER:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=500)

        age=Label(details_r,text="AGE:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=600)

        Class=Label(details_r,text="CLASS:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=500)

        phonenumber=Label(details_r,text="CONTACT NO.:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=300)

        dob=Label(details_r,text="DATE OF BIRTH:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=400)

        email=Label(details_r,text="EMAIL-ID:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=200)

        bloodgroup=Label(details_r,text="BLOOD GROUP:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=600)


        d_name = stu_name.get()
        d_email= em.get()
        
        

        mydb = pymysql.connect(host='localhost', user='root', password='root')
        cur = mydb.cursor()
        cur.execute('create database if not exists project')
        cur.execute('create table if not exists school.student (name varchar(255), f_name varchar(255), m_name varchar(255), gender varchar(20), phone int(10), mail varchar(255), age int(100), date varchar(100), class int(5), Bp varchar(10))')
        cur.execute("select name from school.student where name=%s and mail=%s ",(d_name, d_email))
        s_name = cur.fetchone()
        cur.execute("select f_name from school.student where name=%s and mail=%s ", (d_name, d_email))
        f_name = cur.fetchone()
        cur.execute('select m_name from school.student where name=%s and mail=%s ',(d_name, d_email))
        m_name = cur.fetchone()
        cur.execute('select gender from school.student where name=%s and mail=%s',(d_name, d_email))
        s_gender = cur.fetchone()
        cur.execute('select phone from school.student where name=%s and mail=%s ',(d_name, d_email))
        s_phone = cur.fetchone()
        cur.execute('select mail from school.student where name=%s and mail=%s',(d_name, d_email))
        s_mail = cur.fetchone()
        cur.execute('select age from school.student where name=%s and mail=%s',(d_name, d_email))
        s_age = cur.fetchone()
        cur.execute('select date from school.student where name=%s and mail=%s',(d_name, d_email))
        s_date = cur.fetchone()
        cur.execute('select class from school.student where name=%s and mail=%s',(d_name, d_email))
        s_class= cur.fetchone()
        cur.execute('select Bp from school.student where name=%s and mail=%s',(d_name, d_email))
        s_bp = cur.fetchone()
        # ------------------Labels---------------------------
        name = Label(details_r, text=s_name,bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        name.place(x=301,y=200)
        fname = Label(details_r, text=f_name, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        fname.place(x=300,y=305)
        mname = Label(details_r, text=m_name, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        mname.place(x=300,y=405)
        phn= Label(details_r, text=s_mail, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        phn.place(x=1070,y=305)
        e_mail= Label(details_r, text=s_phone, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        e_mail.place(x=780, y=250)
        Age = Label(details_r, text=s_age, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        Age.place(x=180,y=605)
        DOB = Label(details_r, text=s_date, bd=10,fg='white',
                       font=('Times new roman',20,'bold'))
        DOB.place(x=1080,y=405)
        Cls= Label(details_r, text=s_class, bd=10,fg='white',
                       font=('Times new roman',20,'bold'))
        Cls.place(x=1000,y=505)
        bldgrp= Label(details_r, text=s_bp, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        bldgrp.place(x=1090,y=603)
        gnd= Label(details_r, text=s_gender, bd=10,fg='black',
                       font=('Times new roman',20,'bold'))
        gnd.place(x=250,y=505)
        
      

        Button(details_r,text="BACK",bg='purple',bd=10,fg='white',
                       font=('Times new roman',20,'bold'),command=details_r.destroy).place(x=600,y=630)

        details_r.mainloop()
       

#buttons
    submit=Button(details,text="SUBMIT",bg='purple',bd=10,fg='white',
                       font=('Times new roman',20,'bold'),command=info).place(x=600,y=530)

    details.mainloop()