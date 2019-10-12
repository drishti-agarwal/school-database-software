from tkinter import*
from PIL import ImageTk,Image
import registrationform
import details
mainwindow=Tk()
mainwindow.geometry('600x600')

path=r'F:\wallpaper-3.jpg'
background=ImageTk.PhotoImage(Image.open(path))

#labels
wallpaper=Label(mainwindow,image=background,height=2000,width=2000)
wallpaper.image=background
wallpaper.place(x=0,y=0)
school_name=Label(mainwindow,text='PURE VISION INTERNATIONAL SCHOOL',relief=SOLID,
         bg='black',bd=10,fg='white',font=('Times new roman',30,'bold')).place(x=300,y=0)
intro_heading=Label(mainwindow,text='ABOUT THE SCHOOL',
         bg='purple',bd=10,fg='orange',font=('Times new roman',20,'bold')).place(x=0,y=100)
introduction=Label(mainwindow,text='The Pure vision is committed to fostering excellence '
                                   'in education.We firmly believe that teaching is'
                                   ' not about knowledge downloads, but opening '
                                   'the minds\nof young learners.'
                                   'We guide them towards learning, comprehensively '
                                   'focussing on the overall development of '
                                   'each student.Some people follow a path\n'
                                   'they choose on their own.They discover '
                                   'their true calling. They chase '
                                   'their dreams with passion, '
                                   'and excel in their chosen discipline. '
                                   'But, best of all,\nthey become what they want to be.'
                                   'Pure vision is the school for such people.'
 ,bg='brown',bd=10,fg='white',justify=LEFT,font=('ariel',15)).place(x=0,y=150)






#buttons
register=Button(mainwindow,text='Register Here',fg='white',
                font=('times new roman',20,'bold'),
                bd=10,bg='black',relief=SOLID,command=registrationform.link).place(x=400,y=300)
details=Button(mainwindow,text='Student Detail',fg='white',
               font=('times new roman',20,'bold'),
               bd=10,bg='black',relief=SOLID,command=details.link2).place(x=800,y=300)

mainwindow.mainloop()











