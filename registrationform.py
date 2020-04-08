
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
mydb = pymysql.connect(host='localhost', user='root', password='root')
cur = mydb.cursor()
def link():
    register=Toplevel()
    register.geometry('600x600')

    path=r'D:\drishti\finalproject(schooldatabase)\wallpaper-3.jpg'
    background=ImageTk.PhotoImage(Image.open(path))

    ###################################labels###################################################

    wallpaper=Label(register,image=background,height=2000,width=2000)
    wallpaper.image=background
    wallpaper.place(x=0,y=0)
    school_name=Label(register,text='PURE VISION INTERNATIONAL SCHOOL',relief=SOLID,
      bg='black',bd=10,fg='white',font=('Times new roman',30,'bold')).place(x=300,y=0)

    heading=Label(register,text='REGISTRATION FORM',bg='purple',bd=10,fg='orange',
                  font=('Times new roman',20,'bold')).place(x=550,y=100)

    student_name=Label(register,text="STUDENT'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=200)

    fathers_name=Label(register,text="FATHER'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=300)

    mothers_name=Label(register,text="MOTHER'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=400)

    gender=Label(register,text="GENDER:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=500)

    age=Label(register,text="AGE:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=600)

    Class=Label(register,text="CLASS:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=500)

    phonenumber=Label(register,text="CONTACT NO.:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=300)

    dob=Label(register,text="DATE OF BIRTH:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=400)

    email=Label(register,text="EMAIL-ID:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=200)

    bloodgroup=Label(register,text="BLOOD GROUP:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=900,y=600)

    ###########################entry boxes########################################

    stu_name=Entry(register,width=40)
    stu_name.config(font=10,bd=5)
    stu_name.place(x=301,y=205)

    dad_name=Entry(register,width=40)
    dad_name.config(font=10,bd=5)
    dad_name.place(x=300,y=305)

    mom_name=Entry(register,width=40)
    mom_name.config(font=10,bd=5)
    mom_name.place(x=300,y=405)

    phone_no=Entry(register,width=20)
    phone_no.config(font=10,bd=5)
    phone_no.place(x=1070,y=305)

    emailid=Entry(register,width=30)
    emailid.config(font=10,bd=5)
    emailid.place(x=1020,y=203)


    age_box=Entry(register,width=30)
    age_box.config(font=10,bd=5)
    age_box.place(x=180,y=605)


    date_=Entry(register,width=20)
    date_.config(font=10,bd=5)
    date_.place(x=1080,y=405)

    ################################### drop down menu  ###############################################

    standard=IntVar()
    choices={1,2,3,4,5,6,7,8,9,10,11,12}
    standard.set('please select')
    Cls=OptionMenu(register,standard,*choices)
    Cls.config(fg='white',bg='purple',relief=SOLID,font=('arial',13,'bold'))
    Cls.place(x=1000,y=505)

    blood_grp=StringVar()
    choice={'A-','A+','B-','B+','AB-','AB+','O-','O+'}
    blood_grp.set('please select')
    bld_grp=OptionMenu(register,blood_grp,*choice)
    bld_grp.config(fg='white',bg='purple',relief=SOLID,font=('arial',13,'bold'))
    bld_grp.place(x=1090,y=603)

    ####################################### radiobuttons ####################################################
    v=IntVar()
    female=Radiobutton(register,text='FEMALE',variable=v,relief=SUNKEN,font=('arial',15,'bold'),value=1).place(x=250,y=505)

    male=Radiobutton(register,text='MALE',variable=v,relief=SUNKEN,font=('arial',15,'bold'),value=2).place(x=400,y=505)

     ###################################### retrieve data ####################################################
    def Database():
        name=stu_name.get()
        f_name=dad_name.get()
        m_name=mom_name.get()
        gender=v.get()
        phone=phone_no.get()
        mail=emailid.get()
        age=age_box.get()
        date=date_.get()
        Class=standard.get()
        Bp=blood_grp.get()

        mydb = pymysql.connect(host='localhost', user='root', password='root')
        cur = mydb.cursor()
        cur.execute('create database if not exists school')
        cur.execute('create table if not exists school.student (name varchar(255), f_name varchar(255), m_name varchar(255), gender varchar(20), phone int(10), mail varchar(255), age int(100), date varchar(100), class int(5), Bp varchar(10))')
        cur.execute('insert into school.student (name, f_name, m_name, gender,  phone, mail, age, date, class, Bp) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(name, f_name, m_name, gender, phone, mail, age, date, Class, Bp))
        mydb.commit()      
        messagebox.showinfo(title='thank you', message='DETAILS RECIEVED')
        register.destroy()

        
    ######################################## buttons ##########################################################

    submit=Button(register,text="SUBMIT",bg='purple',bd=10,fg='white',
                       font=('Times new roman',20,'bold'),command=Database).place(x=600,y=630)

   


    register.mainloop()