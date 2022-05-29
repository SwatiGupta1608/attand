from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from grpc import RpcContext
from matplotlib.pyplot import grid
from panel import Row



class student:
    def __init__ (self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        
  #firstimg
        img=Image.open(r"C:\Users\sgupt\Desktop\attandancebasedweb\images\stu1.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second
        img1=Image.open(r"C:\Users\sgupt\Desktop\attandancebasedweb\images\stu2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=530,height=130)

#third
        img2=Image.open(r"C:\Users\sgupt\Desktop\attandancebasedweb\images\stud3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

    #bg

        img3=Image.open(r"C:\Users\sgupt\Desktop\attandancebasedweb\images\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1500,height=600)
        
        #left  labelfreame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\sgupt\Desktop\attandancebasedweb\images\stud4.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

    #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold",),bg="white")
        dep_label.grid(row=0,column=0,padx=10) 

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select department","Computer Science","IT","Electronics","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Courses",font=("times new roman",12,"bold",),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W) 

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","Btech","BSc","BE","BCom")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
#year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold",),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W) 

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2024","2023","2022","2021")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
#semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold",),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W) 

        sem_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class studentinfo
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="C Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)
        #student id
        studentid_label=Label(class_student_frame,text="StudentId",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=10,sticky=W) 

        studentid_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student Name
        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W) 

        studentname_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
 
        #class division
        classdiv_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) 

        classdiv_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        classdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(class_student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) 

        roll_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gen_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W) 

        gen_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gen_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) 

        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) 

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phn_label=Label(class_student_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        phn_label.grid(row=3,column=2,padx=10,pady=5,sticky=W) 

        phn_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phn_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        add_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W) 

        add_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W) 

        teacher_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        radiobtn1=ttk.Radiobutton(class_student_frame,text="take photo sample",value="yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No photo sample",value="yes")
        radiobtn2.grid(row=6,column=1)

        #buttonframe
        btn_frame=Frame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width=725,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)   

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)   

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)   

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)  

        btn_frame1=Frame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=725,height=35) 

        take_photo_btn=Button(btn_frame1,text="Take  photo sample",width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0) 

        update_photo_btn=Button(btn_frame1,text="Update photo sample",width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)        
        
        #rightt  labelfreame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\sgupt\Desktop\attandancebasedweb\images\stud5.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #seach system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search ",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold"),bg="white",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select ","rollno","phoneNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)   

        showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)  

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=640,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photosample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        


if  __name__== "__main__": 
    root=Tk()
    obj=student(root)
    root.mainloop()       