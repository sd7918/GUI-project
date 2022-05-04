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

book_user=Label(root, text="Movie Booking id").grid(row=1, column=2)
name_user=Label(root, text="Person Name :").grid(row=2, column=2)
movieNm_user=Label(root, text="Movie Name").grid(row=3, column=2)
class_user=Label(root, text="Class").grid(row=4, column=2)
time_user=Label(root, text="Time of Show").grid(row=4, column=5)
ticket_user=Label(root, text="No of Tickets").grid(row=5, column=2)

book_value=StringVar()
name_value=StringVar()
movieNm_value=StringVar()
class_value=IntVar()
time_value=IntVar()
ticket_value=IntVar()

book_box=Entry(root, textvariable=book_value).grid(row=1,column=3)
name_box=Entry(root, textvariable=name_value).grid(row=2,column=3)
movieNm_box=Entry(root, textvariable=movieNm_value).grid(row=3,column=3)
rb1_box=Radiobutton(root,text="A",variable=class_value,value=1,command=choise1).grid(row=4,column=3)
rb2_box=Radiobutton(root,text="B",variable=class_value,value=2,command=choise1).grid(row=4,column=4)
rb3_box=Radiobutton(root,text="7.15pm",variable=time_value,value=1,command=choise2).grid(row=4,column=6)
rb4_box=Radiobutton(root,text="9am",variable=time_value,value=2,command=choise2).grid(row=4,column=7)
scale_box=Scale(root,variable=ticket_value,from_=1,to=50,orient=HORIZONTAL).grid(row=5,column=3)

Button(text="Insert",command=root.destroy).grid(row=6,column=2)
Button(text="Update",command=root.destroy).grid(row=6,column=3)
Button(text="Delete",command=root.destroy).grid(row=7,column=2)
Button(text="Select",command=root.destroy).grid(row=7,column=3)
root.mainloop()