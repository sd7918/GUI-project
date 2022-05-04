from tkinter import *
root=Tk()
root.geometry("500x300")
ch=IntVar()
#Label(root, text="Student registration form",font="times 15 bold").grid(row=0,column=3)
regno_user=Label(root,text="Registration no")
regno_user.grid(row=1,column=2)
name_user=Label(root,text="Student Name")
name_user.grid(row=2,column=2)
dept_user=Label(root,text="Depertment")
dept_user.grid(row=3,column=2)
gender_user=Label(root,text="Gender")
gender_user.grid(row=4,column=2)
age_user=Label(root,text="Age")
age_user.grid(row=5,column=2)
regno_value=StringVar
name_value=StringVar
dept_value = StringVar  
age_value= IntVar

regno_box = Entry(root,textvariable=regno_value)
regno_box.grid(row=1,column=3)
name_box = Entry(root,textvariable=name_value)
name_box.grid(row=2 ,column=3)
dept_box = Entry(root,textvariable=dept_value)
dept_box.grid(row=3 ,column=3)
age_spin=Spinbox(root, from_=0, to=19)
age_spin.grid(row=5,column=3)
#age_box= Entry(root,textvariable=age_value)
#age_box.grid(row=5,column=3)

#gender_box = Entry(root,textvariable=gender_value)
#gender_box.grid(row=4 ,column=3)

def choise():
    print(ch.get())

rb1_box = Radiobutton(root,text="Male",variable=ch,value=1,command=choise)
rb1_box.grid(row=4,column=3)
rb2_box = Radiobutton(root,text="Female",variable=ch,value=2,command=choise)
rb2_box.grid(row=4,column=4)
#Scrollbar_box=Scrollbar(text="fnvj",Variable=age_value)
#Scrollbar_box.grid(row=5,column=2)
#check_box = Checkbutton(text="Reminder me",variable=check_value)
#check_box.grid(row=5,column=3)

Button(text="Submit",command=root.destroy).grid(row=6,column=3)
Button(text="insert",command=root.destroy).grid(row=6,column=2)
Button(text="Delete",command=root.destroy).grid(row=7,column=2)
Button(text="Select",command=root.destroy).grid(row=7,column=3)
root.mainloop() 