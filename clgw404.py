from tkinter import *
root=Tk()
root.geometry("700x300")
def choise1():
    if(source_value==1):
        root.configure()
    elif(source_value==2):
        root.configure()

def choise2():
    if(dest_value==1):
        root.configure()
    elif(dest_value==2):
        root.configure()

book_user=Label(root, text="Bookingid").grid(row=1, column=2)
name_user=Label(root, text="Passenger Name :").grid(row=2, column=2)
flight_user=Label(root, text="Flight").grid(row=3, column=2)
source_user=Label(root, text="Source").grid(row=4, column=2)
dest_user=Label(root, text="Destination").grid(row=4, column=5)
duration_user=Label(root, text="Duration").grid(row=5, column=2)

book_value=StringVar()
name_value=StringVar()
flight_value=StringVar()
source_value=IntVar()
dest_value=IntVar()
duration_value=IntVar()

book_box=Entry(root, textvariable=book_value).grid(row=1,column=3)
name_box=Entry(root, textvariable=name_value).grid(row=2,column=3)
flight_box=Entry(root, textvariable=flight_value).grid(row=3,column=3)
rb1_box=Radiobutton(root,text="Delhi",variable=source_value,value=1,command=choise1).grid(row=4,column=3)
rb2_box=Radiobutton(root,text="Mumbai",variable=source_value,value=2,command=choise1).grid(row=4,column=4)
rb3_box=Radiobutton(root,text="Chennai",variable=dest_value,value=1,command=choise2).grid(row=4,column=6)
rb4_box=Radiobutton(root,text="Kolkata",variable=dest_value,value=2,command=choise2).grid(row=4,column=7)
duration_spin=Spinbox(root,from_=1,to=20).grid(row=5,column=3)

Button(text="Insert",command=root.destroy).grid(row=6,column=2)
Button(text="Update",command=root.destroy).grid(row=6,column=3)
Button(text="Delete",command=root.destroy).grid(row=7,column=2)
Button(text="Select",command=root.destroy).grid(row=7,column=3)
root.mainloop()