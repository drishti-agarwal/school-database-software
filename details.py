from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

def link2():
    details=Toplevel()
    details.geometry('600x600')

    path=r'F:\wallpaper-3.jpg'
    background=ImageTk.PhotoImage(Image.open(path))

    #labels
    wallpaper=Label(details,image=background,height=2000,width=2000)
    wallpaper.image=background
    wallpaper.place(x=0,y=0)

    school_name=Label(details,text='PURE VISION INTERNATIONAL SCHOOL',relief=SOLID,
      bg='black',bd=10,fg='white',font=('Times new roman',30,'bold')).place(x=300,y=0)

    heading=Label(details,text='REGISTRATION FORM',bg='purple',bd=10,fg='orange',
                  font=('Times new roman',20,'bold')).place(x=550,y=100)

    student_name=Label(details,text="STUDENT'S NAME:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=200)

    student_id=Label(details,text="STUDENT'S ID:",bg='orange',bd=10,fg='white',
                       font=('Times new roman',15,'bold')).place(x=100,y=300)

    #entry boxes
    stu_name=Entry(details,width=40)
    stu_name.config(font=10,bd=5)
    stu_name.place(x=301,y=205)

    stu_id=Entry(details,width=40)
    stu_id.config(font=10,bd=5)
    stu_id.place(x=270,y=305)
    #functions
    def check():
            temp = int(stu_id.get())
            if temp>=10000:
                messagebox.showinfo(title='ALERT!!!', message='INVALID STUDENT ID')
            else:
                messagebox.showinfo(title='thank you', message='WELCOME')


#buttons
    submit=Button(details,text="SUBMIT",bg='purple',bd=10,fg='white',
                       font=('Times new roman',20,'bold'),command=check).place(x=600,y=530)

    details.mainloop()