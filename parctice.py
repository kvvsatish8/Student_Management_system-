import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Exit Button Example")
window.geometry("300x200")

# Function to exit the window
def close_window():
    window.destroy()  # This will close the window

# Create Exit button
exit_button = tk.Button(window, text="Exit", command=close_window, bg="red", fg="white")
exit_button.pack(pady=50)

# Run the GUI loop
window.mainloop()


    add_date=Label(add_window,text='Join_date',font =('times new roman',20,'bold'))
    add_date.grid(row=7,column=0)
    add_date_entry=Entry(add_window,font=('roman',20,'bold'))
    add_date_entry.grid(row=7,column=1,pady=15)  
     
    add_time=Label(add_window,text='Time',font=('times new roman',20,'bold'))
    add_time.grid(row=8,column=0)
    add_time_entry=Entry(add_window,font=('roman',20,'bold'))
    add_time_entry.grid(row=8,column=1,pady=15)
