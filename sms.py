from tkinter import *
import ttkthemes
import time
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas as pd

root=ttkthemes.ThemedTk()
# to apply themes
root.get_themes()
root.set_theme("adapta")



root.geometry('1900x800+0+0')
root.title('main page of sms')

# functionalities

#exit button in main page
def exit_window():
    result=messagebox.askyesno('confirm','do you want to exit')
    if result:
        root.destroy()
    else:
        pass    
        

#export button
def export_data():
    url=filedialog.asksaveasfile(defaultextension='.csv')
    indexing=student_tabel.get_children()
    new_list=[]
    for index in indexing:
        content=student_tabel.item(index)
        data_list=content['values']
        new_list.append(data_list)
        
    table=pd.DataFrame(new_list,columns=['ID','Name','Gender','DOB','mobile_no','Address','Email','Join_date'])   
    table.to_csv(url,index=False)
    messagebox.showinfo('success','data is saved successfuly')     
    

#update window
def update_window():
    def update_student():
        query='update student set name=%s,gender=%s,dob=%s,mobile_no=%s,address=%s,email=%s where id=%s'
        mycursor.execute(query,(update_name_entry.get(),update_gender_entry.get(),update_dob_entry.get(),update_mobile_entry.get(),update_address_entry.get(),update_email_entry.get(),update_entry.get()))
        con.commit()
        messagebox.showinfo('success',f'ID{update_entry.get()} is modifed successfully',parent=update_window)
        update_window.destroy()
        show_student()
        
        
    update_window=Toplevel()
    update_window.grab_set()
    update_window.title("update_student")
    
    update_label=Label(update_window,text='ID',font=('times new roman',20,'bold'))
    update_label.grid(padx=20,pady=15,sticky=W)
    update_entry=Entry(update_window,font=('roman',20,'bold'))
    update_entry.grid(row=0,column=1,padx=20)
    
    update_name=Label(update_window,text='Name',font=('times new roman',20,'bold'))
    update_name.grid(row=1,column=0,pady=15,padx=15,sticky=W)
    update_name_entry=Entry(update_window,font=('roman',20,'bold'))
    update_name_entry.grid(row=1,column=1,pady=15)
    
    
    update_gender=Label(update_window,text='Gender',font=('times new roman',20,'bold'))
    update_gender.grid(row=2,column=0,pady=15,padx=15,sticky=W)
    update_gender_entry=Entry(update_window,font=('roman',20,'bold'))
    update_gender_entry.grid(row=2,column=1,pady=15)
    
    update_dob=Label(update_window,text='DOB',font=('times new roman',20,'bold'))
    update_dob.grid(row=3,column=0,pady=15,padx=15,sticky=W)
    update_dob_entry=Entry(update_window,font=('roman',20,'bold'))
    update_dob_entry.grid(row=3,column=1,pady=15)
    
    update_mobile=Label(update_window,text='Mobile No',font=('times new roman',20,'bold'))
    update_mobile.grid(row=4,column=0,pady=15,padx=15,sticky=W)
    update_mobile_entry=Entry(update_window,font=('roman',20,'bold'))
    update_mobile_entry.grid(row=4,column=1,pady=15)
    
    update_address=Label(update_window,text='address',font=('times new roman',20,'bold'))
    update_address.grid(row=5,column=0,pady=15,padx=15,sticky=W)
    update_address_entry=Entry(update_window,font=('roman',20,'bold'))
    update_address_entry.grid(row=5,column=1,pady=15)
    
    update_email=Label(update_window,text='Email',font=('times new roman',20,'bold'))
    update_email.grid(row=6,column=0,pady=15,padx=15,sticky=W)
    update_email_entry=Entry(update_window,font=('roman',20,'bold'))
    update_email_entry.grid(row=6,column=1,pady=15)
    

    
    update_exit_button=ttk.Button(update_window,text='Exit',command=update_window.destroy)
    update_exit_button.grid(row=7,column=0,pady=15)
    
    update_submite_button=ttk.Button(update_window,text='update',command=update_student)
    update_submite_button.grid(row=7,column=1,pady=15)
    
    indexing=student_tabel.focus()
    content=student_tabel.item(indexing)
    listdata=content['values']
    update_entry.insert(0,listdata[0])
    update_name_entry.insert(0,listdata[1])
    update_gender_entry.insert(0,listdata[2])
    update_dob_entry.insert(0,listdata[3])
    update_mobile_entry.insert(0,listdata[4])
    update_address_entry.insert(0,listdata[5])
    update_email_entry.insert(0,listdata[6])
    
    

#show button fun
def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    student_tabel.delete(*student_tabel.get_children())
    for data in fetched_data:
        student_tabel.insert('',END,values=data) 
#delete button
def delete_student():
    indexing=student_tabel.focus()
    content=student_tabel.item(indexing)
    content_id=content['values'][0] 
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('deleted',f'ID{content_id} deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    student_tabel.delete(*student_tabel.get_children())
    for data in fetched_data:
        student_tabel.insert('',END,values=data)


#search_window
def search_student():
    def search_data():
        query='select * from student where ID=%s or Name=%s or Gender=%s or DOB=%s or Mobile_No=%s or address=%s or Email=%s'
        mycursor.execute(query,(search_entry.get(),search_name_entry.get(),search_gender_entry.get(),search_dob_entry.get(),search_mobile_entry.get(),search_address_entry.get(),search_email_entry.get()))
        student_tabel.delete(*student_tabel.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            student_tabel.insert('',END,values=data)
    
    
    search_window=Toplevel()
    search_window.grab_set()
    search_window.title("search_student")
    
    search_label=Label(search_window,text='ID',font=('times new roman',20,'bold'))
    search_label.grid(padx=20,pady=15,sticky=W)
    search_entry=Entry(search_window,font=('roman',20,'bold'))
    search_entry.grid(row=0,column=1,padx=20)
    
    search_name=Label(search_window,text='Name',font=('times new roman',20,'bold'))
    search_name.grid(row=1,column=0,pady=15,padx=15,sticky=W)
    search_name_entry=Entry(search_window,font=('roman',20,'bold'))
    search_name_entry.grid(row=1,column=1,pady=15)
    
    search_gender=Label(search_window,text='Gender',font=('times new roman',20,'bold'))
    search_gender.grid(row=2,column=0,pady=15,padx=15,sticky=W)
    search_gender_entry=Entry(search_window,font=('roman',20,'bold'))
    search_gender_entry.grid(row=2,column=1,pady=15)
    
    search_dob=Label(search_window,text='DOB',font=('times new roman',20,'bold'))
    search_dob.grid(row=3,column=0,pady=15,padx=15,sticky=W)
    search_dob_entry=Entry(search_window,font=('roman',20,'bold'))
    search_dob_entry.grid(row=3,column=1,pady=15)
    
    search_mobile=Label(search_window,text='Mobile No',font=('times new roman',20,'bold'))
    search_mobile.grid(row=4,column=0,pady=15,padx=15,sticky=W)
    search_mobile_entry=Entry(search_window,font=('roman',20,'bold'))
    search_mobile_entry.grid(row=4,column=1,pady=15)
    
    search_address=Label(search_window,text='address',font=('times new roman',20,'bold'))
    search_address.grid(row=5,column=0,pady=15,padx=15,sticky=W)
    search_address_entry=Entry(search_window,font=('roman',20,'bold'))
    search_address_entry.grid(row=5,column=1,pady=15)
    
    search_email=Label(search_window,text='Email',font=('times new roman',20,'bold'))
    search_email.grid(row=6,column=0,pady=15,padx=15,sticky=W)
    search_email_entry=Entry(search_window,font=('roman',20,'bold'))
    search_email_entry.grid(row=6,column=1,pady=15)
    

    
    search_exit_button=ttk.Button(search_window,text='Exit',command=search_window.destroy)
    search_exit_button.grid(row=7,column=0,pady=15)
    
    search_submite_button=ttk.Button(search_window,text='search',command=search_data)
    search_submite_button.grid(row=7,column=1,pady=15)
    


#add_student
def add_student():
    #submite button funtionality
    def add_data():
        if add_entry.get()==''or add_name_entry.get()=='' or add_gender_entry.get()=='' or add_dob_entry.get()=='' or add_mobile_entry.get()=='' or add_address_entry.get()=='' or add_email_entry.get()=='':
            messagebox.showerror('error','fill all details',parent=add_window )
        else:
            currentdate=time.strftime('%d/%m/%Y')
            try:
                query = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(query,(add_entry.get(),add_name_entry.get(),add_gender_entry.get(),add_dob_entry.get(),add_mobile_entry.get(),add_address_entry.get(),add_email_entry.get(),currentdate))
                con.commit()
                result=messagebox.askyesno('confirm','data added successfully.do you want to clean the form',parent=add_window)
                if result:
                    add_entry.delete(0,END)
                    add_name_entry.delete(0,END)
                    add_gender_entry.delete(0,END)
                    add_dob_entry.delete(0,END)
                    add_mobile_entry.delete(0,END)
                    add_address_entry.delete(0,END)
                    add_email_entry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('error',"ID's must not be same")    
                return
            
            query='select * from student' 
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            print(fetched_data)
            student_tabel.delete(*student_tabel.get_children())
            for data in fetched_data:
                list_data=list(data) 
                student_tabel.insert('',END,values=list_data)

            
            
            
    add_window=Toplevel()
    add_window.grab_set()
    add_window.title("add_student")
    
    add_label=Label(add_window,text='ID',font=('times new roman',20,'bold'))
    add_label.grid(padx=20,pady=15,sticky=W)
    add_entry=Entry(add_window,font=('roman',20,'bold'))
    add_entry.grid(row=0,column=1,padx=20)
    
    add_name=Label(add_window,text='Name',font=('times new roman',20,'bold'))
    add_name.grid(row=1,column=0,pady=15,padx=15,sticky=W)
    add_name_entry=Entry(add_window,font=('roman',20,'bold'))
    add_name_entry.grid(row=1,column=1,pady=15)
    
    add_gender=Label(add_window,text='Gender',font=('times new roman',20,'bold'))
    add_gender.grid(row=2,column=0,pady=15,padx=15,sticky=W)
    add_gender_entry=Entry(add_window,font=('roman',20,'bold'))
    add_gender_entry.grid(row=2,column=1,pady=15)
    
    add_dob=Label(add_window,text='DOB',font=('times new roman',20,'bold'))
    add_dob.grid(row=3,column=0,pady=15,padx=15,sticky=W)
    add_dob_entry=Entry(add_window,font=('roman',20,'bold'))
    add_dob_entry.grid(row=3,column=1,pady=15)
    
    add_mobile=Label(add_window,text='Mobile No',font=('times new roman',20,'bold'))
    add_mobile.grid(row=4,column=0,pady=15,padx=15,sticky=W)
    add_mobile_entry=Entry(add_window,font=('roman',20,'bold'))
    add_mobile_entry.grid(row=4,column=1,pady=15)
    
    add_address=Label(add_window,text='address',font=('times new roman',20,'bold'))
    add_address.grid(row=5,column=0,pady=15,padx=15,sticky=W)
    add_address_entry=Entry(add_window,font=('roman',20,'bold'))
    add_address_entry.grid(row=5,column=1,pady=15)
    
    add_email=Label(add_window,text='Email',font=('times new roman',20,'bold'))
    add_email.grid(row=6,column=0,pady=15,padx=15,sticky=W)
    add_email_entry=Entry(add_window,font=('roman',20,'bold'))
    add_email_entry.grid(row=6,column=1,pady=15)
    

    
    add_exit_button=ttk.Button(add_window,text='Exit',command=add_window.destroy)
    add_exit_button.grid(row=7,column=0,pady=15)
    
    add_submite_button=ttk.Button(add_window,text='Submit',command=add_data)
    add_submite_button.grid(row=7,column=1,pady=15)
    
    

#time fun
def clock():
    global date
    date=time.strftime('%d/%m/%Y')
    current_time=time.strftime('%H:%M:%S')
    data_time_label.config(text=f'  Date:{date} \n Time:{current_time}')
    data_time_label.after(1000,clock)
    
#slider fun  
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    slider_label.config(text=text)
    count+=1
    slider_label.after(300,slider) 
    
#database connection
def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='Hayati143@')
            mycursor=con.cursor()
            
            
        except:
            messagebox.showerror('error','invaild details',parent=connect_window)
            return
        try:    
            query='create database student_management_system'
            mycursor.execute(query)
            
            query='use student_management_system'
            mycursor.execute(query)
    
            query='create table student(id int,name varchar(30) NOT NULL,gender varchar(10),dob varchar(10),mobile_no varchar(10) ,address varchar(30),email varchar (30),join_data varchar(10),Time varchar(10),primary key(id))'    
            mycursor.execute(query)
        except:
            query='use student_management_system' 
            mycursor.execute(query)  
        messagebox.showinfo('success','database connection is successful',parent=connect_window)
        connect_window.destroy() 
        add_student_button.config(state=NORMAL)
        search_button.config(state=NORMAL)
        update_button.config(state=NORMAL)
        delete_button.config(state=NORMAL)
        show_button.config(state=NORMAL)
        export_button.config(state=NORMAL)
              
            
            
    connect_window=Toplevel()   
    connect_window.grab_set()
    connect_window.geometry('500x200+950+200')   
    connect_window.title('database connection')
    connect_window.resizable(0,0)
    #creating database connection gui
    host_label=Label(connect_window,text='Host Name :',font=('arial',20,'bold'))
    host_label.grid(row=0,column=0,padx=5,pady=5)
    #creating entry for host
    host_entry=Entry(connect_window,font=('roman',20,'bold'),bd=5)
    host_entry.grid(row=0,column=1,padx=5,pady=5)
   
    user_label=Label(connect_window,text='User Name :',font=('arial',20,'bold'))
    user_label.grid(row=1,column=0,padx=5,pady=5)
    
    user_entry=Entry(connect_window,font=('roman',20,'bold'),bd=5)
    user_entry.grid(row=1,column=1,padx=5,pady=5)
    
    password_label=Label(connect_window,text='Password :',font=('arial',20,'bold'))
    password_label.grid(row=2,column=0,padx=5,pady=5)
    
    password_entry=Entry(connect_window,font=('roman',20,'bold'),bd=5)
    password_entry.grid(row=2,column=1,padx=5,pady=5)  
    
    # creating exit and connect button
    connectbutton=ttk.Button(connect_window,text='Connect',command=connect)
    connectbutton.grid(row=3,column=1) 
    
    exitbutton=ttk.Button(connect_window,text='exit',command=exit_window)
    exitbutton.grid(row=3,column=0)
    



# gui part

#creating time and data gui
data_time_label=Label(root,font=('times new roman',18,"bold"))
data_time_label.place(x=5,y=5)
clock()
#creating slider
s="STUDENT MANAGEMENT SYSTEM"
slider_label=Label(root,font=("arial",28,'italic bold'),width=30)
slider_label.place(x=300,y=0)
slider()

#creating database connect button
connect_button=ttk.Button(root,text='Connect DataBase',command=connect_database)
connect_button.place(x=1300,y=1)



#creating left frame
left_frame=Frame(root)
left_frame.place(x=50,y=80,width=350,height=650)

#import left frame logo
left_logo=PhotoImage(file='student_resize.png')
left_label=Label(left_frame,image=left_logo)
left_label.grid(row=1,column=0)

#creating student button
add_student_button=ttk.Button(left_frame,text=' Add Student ',width=25,state=DISABLED,command=add_student)
add_student_button.grid(row=2,column=0,pady=20)

search_button=ttk.Button(left_frame,text=' Search Student ',width=25,state=DISABLED,command=search_student)
search_button.grid(row=3,column=0,pady=20)

update_button=ttk.Button(left_frame,text=' Update student ',width=25,state=DISABLED,command=update_window)
update_button.grid(row=4,column=0,pady=20)

delete_button=ttk.Button(left_frame,text=' Delete Student',width=25,state=DISABLED,command=delete_student)
delete_button.grid(row=5,column=0,pady=20)

show_button=ttk.Button(left_frame,text=' show student list ',width=25,state=DISABLED,command=show_student)
show_button.grid(row=6,column=0,pady=20)

export_button=ttk.Button(left_frame,text=' Export Data',width=25,state=DISABLED,command=export_data)
export_button.grid(row=7,column=0,pady=20)

exit_button=ttk.Button(left_frame,text=' Exit ',width=25,command=exit_window)
exit_button.grid(row=8,column=0,pady=20)

#creating right Frame
right_frame=Frame(root)
right_frame.place(x=400,y=90,width=1005,height=650)

#creating scroll bar
Scrollbar_x=Scrollbar(right_frame,orient=HORIZONTAL)
Scrollbar_y=Scrollbar(right_frame,)


#creating tree view class
student_tabel=ttk.Treeview(right_frame
                           ,columns=('ID','NAME','GENDER'
                                     ,'DOB','MOBILE NO','ADDRESS',
                                     'EMAIL','JOIN DATE'),
                           xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)

#configurating scrollbar and palcing
student_tabel.pack(fill=BOTH,expand=1)
Scrollbar_x.pack(fill=X,side=BOTTOM)
Scrollbar_y.pack(fill=Y,side=RIGHT)
Scrollbar_x.config(command=student_tabel.xview)
Scrollbar_y.config(command=student_tabel.yview)

#creating heding in table
student_tabel.heading('ID',text='ID')
student_tabel.heading('NAME',text='NAME')
student_tabel.heading('GENDER',text='GENDER')
student_tabel.heading('DOB',text='D.O.B')
student_tabel.heading('MOBILE NO',text='MOBILE NO')
student_tabel.heading('ADDRESS',text='ADDRESS')
student_tabel.heading('EMAIL',text='EMAIL')
student_tabel.heading('JOIN DATE',text='JOIN DATE')
student_tabel.config(show='headings')


root.mainloop()