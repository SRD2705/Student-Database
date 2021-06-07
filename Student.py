import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import os
import qrcode
from PIL import Image,ImageTk,ImageDraw,ImageFont
from resizeimage import resizeimage
import tempfile
from datetime import datetime
class Students:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Management System")
        self.root.geometry("1920x1080+0+0")

        title = Label(self.root, text="Student Management System", bd=20, relief=RIDGE,font=("times new roman", 50, "bold"), bg="midnight blue", fg="Green2")
        title.pack(side=TOP, fill=X)  # fill used for spread as its width

        user_title = Label(self.root,text="Welcome User",bd=0,relief = RIDGE,font=("times new roman", 20, "bold"),bg="midnight blue",fg="red")
        user_title.place(x=40,y=40)

        logout_btn = Button(self.root,text="LOGOUT",width=8,bg='red',command=self.logout)
        logout_btn.place(x=1750,y=42)

        bottom = Label(self.root, text="Managed by SRD2705", bd=10, relief=SOLID, font=("Ariel", 20),bg="dark green", fg="white")
        bottom.pack(side=BOTTOM, fill=X)

        ############################################################## All Variables for database

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.course_var = StringVar()
        self.dept_var = StringVar()
        self.pass_var = StringVar()
        self.cgpa_var = StringVar()

        ################################################################### Variable for search
        self.search_by = StringVar()
        self.search_txt = StringVar()

        ############################################################### Manage Fame
        # Responsible for data operation of the students

        self.Manage_Frame = Frame(self.root, bd=10, relief=RIDGE, bg='Grey24')
        self.Manage_Frame.place(x=0, y=115, width=700, height=850)

        m_title = Label(self.Manage_Frame,text=" Student Data Management Panel",font=("Times New Roman",30,"bold"),bg="Grey24",fg="Orange2")
        # We are using grid because in this case we do not need to take care of x,y location it follows row,column
        m_title.grid(row=0,columnspan=2,pady=10,padx=30)

        # Label and text fields for ROLL
        lbl_roll=Label(self.Manage_Frame,text="Roll No.",font=("Times New Roman",20,"bold"),bg="Grey24",fg="White")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w') # Sticky property used for the left alignment

        txt_roll = Entry(self.Manage_Frame,textvariable=self.Roll_No_var,font=("Times New Roman",15,"bold"),bd=5,relief = GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        # Label and text fields for NAME
        lbl_name = Label(self.Manage_Frame, text="Full Name", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        txt_name = Entry(self.Manage_Frame, textvariable=self.name_var,font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        # Label and text fields for EMAIL
        lbl_email = Label(self.Manage_Frame, text="E-Mail", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        txt_email = Entry(self.Manage_Frame, textvariable=self.email_var,font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        # Label and text fields for GENDER
        lbl_gender = Label(self.Manage_Frame, text="Gender", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        combo_gender = ttk.Combobox(self.Manage_Frame,textvariable=self.gender_var,font=("Times New Roman", 15, "bold"),state="readonly")   # We use combo box because of gender we use drop down list
        combo_gender['values']=("Male","Female","Other")                                                   # using readonly state because we dont want to edit the field after selecting it
        combo_gender.grid(row=4,column=1,pady=10, padx=20,sticky='w')

        # Label and text fields for PHONENUMBER
        lbl_phnum = Label(self.Manage_Frame, text="Contact Number", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_phnum.grid(row=5, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        txt_phnum = Entry(self.Manage_Frame, textvariable=self.contact_var,font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_phnum.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        # Label and text fields for DOB
        lbl_dob = Label(self.Manage_Frame, text="DOB", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        txt_dob = Entry(self.Manage_Frame, textvariable=self.dob_var,font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_course = Label(self.Manage_Frame, text="Course", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_course.grid(row=7, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        combo_course = ttk.Combobox(self.Manage_Frame, textvariable=self.course_var, font=("Times New Roman", 15, "bold"),state="readonly")  # We use combo box because of gender we use drop down list
        combo_course['values'] = ("Diploma", "B.Tech", "BCA", "M.Tech", "MCA","Phd")  # using readonly state because we dont want to edit the field after selecting it
        combo_course.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        lbl_dept = Label(self.Manage_Frame, text="Department", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_dept.grid(row=8, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        combo_dept = ttk.Combobox(self.Manage_Frame, textvariable=self.dept_var, font=("Times New Roman", 15, "bold"),state="readonly")  # We use combo box because of gender we use drop down list
        combo_dept['values'] = ("Information Technology","Computer Science","Civil","Mechanical","Electrical","Electronics")  # using readonly state because we dont want to edit the field after selecting it
        combo_dept.grid(row=8, column=1, pady=10, padx=20, sticky='w')

        lbl_pass = Label(self.Manage_Frame, text="Passing Year", font=("Times New Roman", 20, "bold"), bg="Grey24",fg="White")
        lbl_pass.grid(row=9, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        txt_pass = Entry(self.Manage_Frame, textvariable=self.pass_var, font=("Times New Roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_pass.grid(row=9, column=1, pady=10, padx=20, sticky='w')

        lbl_cgpa = Label(self.Manage_Frame, text="CGPA", font=("Times New Roman", 20, "bold"), bg="Grey24",fg="White")
        lbl_cgpa.grid(row=10, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        txt_cgpa = Entry(self.Manage_Frame, textvariable=self.cgpa_var, font=("Times New Roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_cgpa.grid(row=10, column=1, pady=10, padx=20, sticky='w')

        # Label and text fields for ADDRESS
        lbl_address = Label(self.Manage_Frame, text="Address", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="White")
        lbl_address.grid(row=11, column=0, pady=10, padx=20, sticky='w')  # Sticky property used for the left alignment

        self.txt_address = Text(self.Manage_Frame,width=30,height=4,font=("Times New Roman", 15))
        self.txt_address.grid(row=11, column=1, pady=10, padx=20, sticky='w')

        # Button frame
        # creating button for various operations
        self.btn_Frame = Frame(self.root, bd=10,bg='grey24')
        self.btn_Frame.place(x=70, y=870, width=600, height=80)

        addbtn = Button(self.btn_Frame,text="ADD",width=8,bg='green',command=self.add_students).grid(row=0,column=0,padx=20)
        updatebtn = Button(self.btn_Frame, text="UPDATE", width=8,bg="yellow",command=self.update_data).grid(row=0, column=1, padx=20)
        deletebtn = Button(self.btn_Frame, text="DELETE", width=8,bg="red",command=self.delete_data).grid(row=0, column=2, padx=20)
        clearbtn = Button(self.btn_Frame, text="CLEAR", width=8,command=self.clear).grid(row=0, column=3, padx=20)
        generateidbtn = Button(self.btn_Frame, text="GENERATE ID", width=10,bg="blue",command=self.generate_id).grid(row=1, columnspan=4, padx=20,pady=10)


        #############################################3 Detail Frame
        # Responsible for data viewing and filtering

        Detail_Frame = Frame(self.root, bd=10, relief=RIDGE, bg='Grey24')
        Detail_Frame.place(x=700, y=115, width=1220, height=850)

        lbl_search = Label(Detail_Frame, text="Search Filter", font=("Times New Roman", 20, "bold"), bg="Grey24", fg="Yellow")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("Times New Roman", 15, "bold"),state="readonly")  # We use combo box because of gender we use drop down list
        combo_search['values'] = ("roll_no","name","contact","course","dept","pass_year","cgpa")  # using readonly state because we dont want to edit the field after selecting it
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("Times New Roman", 15, "bold"), bd=5, relief=RIDGE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        searchbtn = Button(Detail_Frame, text="SEARCH", width=8,command=self.search_data).grid(row=0, column=3, padx=20)
        showallbtn = Button(Detail_Frame, text="SHOW ALL", width=8,command=self.fetch_data).grid(row=0, column=4, padx=20)

        ######################################################### Table frame(for grid)
        Table_Frame=Frame(Detail_Frame,bd=4,relief=SOLID,bg='White')
        Table_Frame.place(x=4,y=60,width=1190,height=765)

        # creating scrollbar for data scrolling
        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","course","department","passyear","cgpa","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="ROLL NO.")
        self.Student_table.heading("name", text="NAME")
        self.Student_table.heading("email", text="E-MAIL")
        self.Student_table.heading("gender", text="GENDER")
        self.Student_table.heading("contact", text="CONTACT NO.")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("course", text="COURSE")
        self.Student_table.heading("department",text="DEPARTMENT")
        self.Student_table.heading("passyear", text="PASS YEAR")
        self.Student_table.heading("cgpa", text="CGPA")
        self.Student_table.heading("address", text="ADDRESS")
        self.Student_table['show']='headings'
        self.Student_table.column("roll", width=160)
        self.Student_table.column("name", width=240)
        self.Student_table.column("email", width=260)
        self.Student_table.column("gender", width=110)
        self.Student_table.column("contact", width=180)
        self.Student_table.column("dob", width=170)
        self.Student_table.column("course", width=120)
        self.Student_table.column("department", width=220)
        self.Student_table.column("passyear", width=120)
        self.Student_table.column("cgpa", width=100)
        self.Student_table.column("address", width=400)
        self.Student_table.pack(fill=BOTH,expand=1)     # For adjusting the screen
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        self.root.mainloop()


    ####################################################### Function for data add
    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","! All fields are required !")
        elif len(self.contact_var.get()) != 10:
            messagebox.showerror("Error","! Contact number must be 10 digits !")
        else:
            con = pymysql.connect(host='localhost',user="root",password="Rishi@2705",database="stm")
            cur = con.cursor()
            cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Roll_No_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.course_var.get(),
                self.dept_var.get(),
                self.pass_var.get(),
                self.cgpa_var.get(),
                self.txt_address.get('1.0',END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Data added successfully")

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
        cur = con.cursor()
        cur.execute("select * from Students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.course_var.set(""),
        self.dept_var.set(""),
        self.pass_var.set(""),
        self.cgpa_var.set("")
        self.txt_address.delete('1.0', END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.course_var.set(row[6]),
        self.dept_var.set(row[7]),
        self.pass_var.set(row[8]),
        self.cgpa_var.set(row[9]),
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[10])

    def update_data(self):
        con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
        cur = con.cursor()
        cur.execute("update Students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,course=%s,dept=%s,pass_year=%s,cgpa=%s,address=%s where roll_no=%s", (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.course_var.get(),
            self.dept_var.get(),
            self.pass_var.get(),
            self.cgpa_var.get(),
            self.txt_address.get('1.0', END),
            self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Data updated successfully")

    def delete_data(self):
        con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
        cur = con.cursor()
        cur.execute("delete from Students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
        cur = con.cursor()
        if self.search_by.get() == "roll_no":
            cur.execute("select * from Students where roll_no="+str(self.search_txt.get()))
        else:
            cur.execute("select * from Students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def logout(self):
        self.root.destroy()
        os.system("python3 login.py")
        # import login
        
    def generate_id(self):
        # self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        # self.Manage_Frame.destroy()
        # self.btn_Frame.destroy()
        self.Generate_Frame = Frame(self.root, bd=10, relief=RIDGE, bg='Grey24')
        self.Generate_Frame.place(x=0, y=115, width=700, height=850)
        self.ID_Frame = Frame(self.Generate_Frame,bd=10,relief=SOLID,bg="White")
        self.ID_Frame.place(x=140,y=40,width =400,height=600 )
        self.qr_lbl = Label(self.ID_Frame,bd=10,)
        self.qr_lbl.place(x=108,y=100,width =180,height=180)

        qr_title = Label(self.ID_Frame,text="ID Card",font=("goudy old style",20),bg="blue2",fg="white").pack(side=TOP,fill=X)

        qr_lbl_name = Label(self.ID_Frame, text="Name: ", font=("Times New Roman", 20, "bold"), bg="white",fg="Black")
        qr_lbl_name.place(x=20,y=300)
        qr_txt_name = Label(self.ID_Frame, text=self.name_var.get(), font=("times new roman", 15), bg="white", fg="Black")
        qr_txt_name.place(x=120,y=305)

        qr_lbl_roll = Label(self.ID_Frame, text="Roll: ", font=("Times New Roman", 20, "bold"), bg="white",fg="Black")
        qr_lbl_roll.place(x=20,y=340)
        qr_txt_roll = Label(self.ID_Frame, text=self.Roll_No_var.get(), font=("times new roman", 15), bg="white", fg="Black")
        qr_txt_roll.place(x=120,y=345)

        qr_lbl_dept = Label(self.ID_Frame, text="Dept.: ", font=("Times New Roman", 20, "bold"), bg="white",fg="Black")
        qr_lbl_dept.place(x=20,y=380)
        qr_txt_dept = Label(self.ID_Frame, text=self.dept_var.get(), font=("times new roman", 15), bg="white", fg="Black")
        qr_txt_dept.place(x=120,y=385)

        qr_lbl_course = Label(self.ID_Frame, text="Course: ", font=("Times New Roman", 20, "bold"), bg="white",fg="Black")
        qr_lbl_course.place(x=20,y=420)
        qr_txt_course = Label(self.ID_Frame, text=self.course_var.get()+" ("+self.pass_var.get()+")", font=("times new roman", 15), bg="white", fg="Black")
        qr_txt_course.place(x=120,y=425)

        qr_lbl_gender = Label(self.ID_Frame, text="Gender: ", font=("Times New Roman", 20, "bold"), bg="white",fg="Black")
        qr_lbl_gender.place(x=20,y=460)
        qr_txt_gender = Label(self.ID_Frame, text=self.gender_var.get(), font=("times new roman", 15), bg="white", fg="Black")
        qr_txt_gender.place(x=120,y=465)

        back_btn = Button(self.Generate_Frame, text="BACK", width=10, bg="yellow", command=self.back).place(x=100,y=700)
        generateidbtn = Button(self.Generate_Frame, text="GENERATE ID", width=10, bg="blue",command=self.generate_id).place(x=280, y=700)
        download_btn = Button(self.Generate_Frame, text="DOWNLOAD", width=10, bg="yellow",command=self.download).place(x=460, y=700)


        if self.name_var.get()=="" or self.Roll_No_var.get()=="":
            fail_lbl = Label(self.Generate_Frame,text="No ID generated !!",font=("goudy old style",20),bg="grey24",fg="red").place(x=220,y=750)
            advice_lbl = Label(self.Generate_Frame,text="Please select a student from side table ---> ",font=("goudy old style",20),bg="grey24",fg="red").place(x=60,y=790)
        else:
            ############################################################################ QR code part
            qr_data = (f"Name: {self.name_var.get()}\nRoll: {self.Roll_No_var.get()}\nDepartment: {self.dept_var.get()}\nCourse: {self.course_var.get()} ({self.pass_var.get()})\nGender: {self.gender_var.get()}")
            self.qr_code = qrcode.make(qr_data)
            self.qr_code = resizeimage.resize_cover(self.qr_code,[180,180])
            self.qr_code.save("ID cards/"+self.Roll_No_var.get()+"-QR.png")
            self.qrimage = ImageTk.PhotoImage(self.qr_code)
            self.qr_lbl.config(image=self.qrimage)
            success_lbl = Label(self.Generate_Frame,text="ID generated successfully !",font=("goudy old style",20),bg="grey24",fg="green").place(x=160,y=750)

    def back(self):
        self.Generate_Frame.destroy()

    def download(self):
        tmpdate = datetime.now()
        gen_date= tmpdate.strftime("ID generation date:  %d-%m-%y (%I:%M:%S %p)")
        image=Image.new('RGB',(400,600),(255,255,255))
        draw=ImageDraw.Draw(image)
        font=ImageFont.truetype('timesnewroman.ttf',size=50)
        (x,y)=(105,0)
        shape = [(0,0),(600,55)]
        draw.rectangle(shape,fill="blue")
        shape = [(5,60),(394,564)]
        draw.rectangle(shape,outline="black",width=3)
        shape = [(0,600), (400, 568)]
        draw.rectangle(shape, fill="blue")
        (x, y) = (105, 0)
        draw.text((x, y), "ID CARD", fill="white", font=font,align="center")
        font = ImageFont.truetype('timesnewroman.ttf', size=20)
        draw.text((20, 300), "Name: ", fill="black", font=font)
        draw.text((120, 300), self.name_var.get(), fill="black", font=font)
        draw.text((20, 340), "Roll No.: ", fill="black", font=font)
        draw.text((120, 340), self.Roll_No_var.get(), fill="black", font=font)
        draw.text((20, 380), "Dept.: ", fill="black", font=font)
        draw.text((120, 380), self.dept_var.get(), fill="black", font=font)
        draw.text((20, 420), "Course: ", fill="black", font=font)
        draw.text((120, 420), self.course_var.get()+" ("+self.pass_var.get()+")", fill="black", font=font)
        draw.text((20, 460), "Gender: ", fill="black", font=font)
        draw.text((120, 460), self.gender_var.get(), fill="black", font=font)
        draw.text((40,572), gen_date,fill="white", font=ImageFont.truetype('timesnewroman.ttf', size=18),align="center")
        im = Image.open("ID cards/"+self.Roll_No_var.get()+"-QR.png")
        image.paste(im,(110,90))
        shape = [(110,90),(290,270)]
        draw.rectangle(shape,outline="black",width=3)
        image.save("ID cards/"+self.Roll_No_var.get()+".png")
        im.close()
        os.remove("ID cards/"+self.Roll_No_var.get()+"-QR.png")


# root = Tk()  # For tkinter invoke
# ob = Students(root)  # make an object(ob) of that class and pass the tkinter(root)
# root.mainloop()  # for run tkinter in main loop

# comment this because we dont want to access this panel directly
# this panel can only be access with login page
# NOTE: If want to access this page from here uncomment above thing, pass root as an argument in the class, remove mainloop execution before all def started
# and in class dont initialize tk(), replace tk() with root in the class first line