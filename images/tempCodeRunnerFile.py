
        #buttonframe
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=700,height=50)
        
        #rightt  labelfreame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=660,height=580)



if  __name__== "__main__": 
    root=Tk()
    obj=student(root)
    root.mainloop()       