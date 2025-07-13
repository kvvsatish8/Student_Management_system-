from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

#creating funationalities

#creating login function
def login():
    if user_name_entry.get()=='' or password_entry.get()=='':
       messagebox.showerror('error','fields must not be empty')
    elif user_name_entry.get()=="satish" and password_entry.get()=='1234':
        messagebox.showinfo('success','welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror("error",'enter correct details')   
        
#creating exit function
def close_window():
    window.destroy()                               


#createing gui part

window=Tk()
window.geometry('1900x800+0+0')
window.title('login page for student managment system')

bg=ImageTk.PhotoImage(file='sm_background.jpg')
bg_label=Label(window,image=bg)
bg_label.place(x=0,y=0)

#creating frame on window
login_frame=Frame(window,bg='white')
login_frame.place(x=520,y=200)

#adding logo to the frame
logo_image=PhotoImage(file='logo.png')
logolabel=Label(login_frame,image=logo_image)
logolabel.grid(row=0,column=0,pady=10)

#creating username with icon
user_name_icon=ImageTk.PhotoImage(file='usericon.png')
user_name_label=Label(login_frame,image=user_name_icon,text='USER NAME :',font=('times new roman',20,'bold'),bg='white',compound=LEFT)
user_name_label.grid(row=1,column=0,pady=10,padx=20)

#creating entry class
user_name_entry=Entry(login_frame,font=('times new roman',20,'bold'),bd=5,fg='royal blue')
user_name_entry.grid(row=1,column=1,padx=20)


#creatng password with icon
password_icon=ImageTk.PhotoImage(file='passwordicon.png')  
password_label=Label(login_frame,image=password_icon,text='PASSWORD :',font=('times new roman',20,'bold'),
                     bg='white',compound=LEFT)
password_label.grid(row=2,column=0,padx=10,pady=10)

#creating password entry
password_entry=Entry(login_frame,font=('times new roman',20,'bold'),bd=5,fg='royal blue')
password_entry.grid(row=2,column=1,padx=20)

#creating login button,exit button
exit_button=Button(login_frame,text='exit',font=('times new roman',15,'bold'),width=15,fg='white',
                   bg='black',cursor='hand2',command=close_window)
exit_button.grid(row=3,column=0,padx=10,pady=10)
login_button=Button(login_frame,text='login',font=('times new roman',15,'bold'),width=15,fg='white'
                    ,bg='cornflower blue',cursor='hand2',command=login)
login_button.grid(row=3,column=1,padx=10,pady=10)
    

window.mainloop()