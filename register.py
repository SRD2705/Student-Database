import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import pymysql
class Login_system:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1920x1080+0+0")

        ################################# All images

        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=PhotoImage(file="images/username.png")
        self.mail_icon=PhotoImage(file="images/mail.png")
        self.gender_icon=PhotoImage(file="images/gender.png")
        self.contact_icon=PhotoImage(file="images/contact.png")
        self.id_icon=PhotoImage(file="images/id.png")
        self.pass_icon=PhotoImage(file="images/pass.png")
        self.logo_icon = PhotoImage(file="images/register.png")


        ############################################# Variables
        self.name_var = StringVar()
        self.mail_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var=StringVar()
        self.idtype_var = StringVar()
        self.idnum_var = StringVar()
        self.user_var=StringVar()
        self.pass_var = StringVar()


        bg_label = Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Registration Panel",font=("Times new roman",40,"bold"),bg="grey14",fg="yellow3",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root,bg="forest green")
        Login_Frame.place(x=420,y=120)
        logo_lbl = Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=6,pady=20)

        name_lbl = Label(Login_Frame,text="Full name", image=self.user_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=1, column=0, padx=0,pady=0)
        txt_name = Entry(Login_Frame, bd="5", textvariable=self.name_var, relief=GROOVE, font=("", 15)).grid(row=1,column=1,padx=20)

        mail_lbl = Label(Login_Frame, text="Email", image=self.mail_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=1, column=3, padx=0,pady=0)
        txt_mail = Entry(Login_Frame, bd="5", textvariable=self.mail_var, relief=GROOVE, font=("", 15)).grid(row=1, column=4,padx=20)

        lbl_gender = Label(Login_Frame, text="Gender",image=self.gender_icon,compound=LEFT, font=("Times New Roman", 20, "bold"), bg="forest green")
        lbl_gender.grid(row=3, column=0, pady=0, padx=0, sticky='w')  # Sticky property used for the left alignment

        combo_gender = ttk.Combobox(Login_Frame, textvariable=self.gender_var, font=("Times New Roman", 20, "bold"),state="readonly")  # We use combo box because of gender we use drop down list
        combo_gender['values'] = ("Male", "Female", "Other")  # using readonly state because we dont want to edit the field after selecting it
        combo_gender.grid(row=3, column=1, padx=0, sticky='w')

        contact_lbl = Label(Login_Frame, text="Contact Number", image=self.contact_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=3, column=3, padx=0,pady=0)
        txt_contact = Entry(Login_Frame, bd="5", textvariable=self.contact_var, relief=GROOVE, font=("", 15)).grid(row=3,column=4,padx=0)


        lbl_idtype = Label(Login_Frame, text="ID Type",image=self.id_icon,compound=LEFT, font=("Times New Roman", 20, "bold"), bg="forest green")
        lbl_idtype.grid(row=4, column=0, padx=0, sticky='w')  # Sticky property used for the left alignment

        combo_idtype = ttk.Combobox(Login_Frame, textvariable=self.idtype_var, font=("Times New Roman", 20, "bold"),state="readonly")  # We use combo box because of gender we use drop down list
        combo_idtype['values'] = ("Aadhaar Card", "Passport", "Pancard","Voter ID")  # using readonly state because we dont want to edit the field after selecting it
        combo_idtype.grid(row=4, column=1, padx=0, sticky='w')



        idnum_lbl = Label(Login_Frame, text="ID Number", image=self.id_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=4, column=3, padx=20,pady=10)
        txt_idnum = Entry(Login_Frame, bd="5", textvariable=self.idnum_var, relief=GROOVE, font=("", 15)).grid(row=4,column=4,padx=0)




        user_lbl = Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="forest green").grid(row=6,column=0,padx=0,pady=0)
        txt_user = Entry(Login_Frame,bd="5",textvariable=self.user_var,relief=GROOVE,font=("",15)).grid(row=6,column=1,padx=0)

        pass_lbl = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=6, column=3, padx=0,pady=0)
        txt_pass = Entry(Login_Frame, bd="5", show = "*",textvariable=self.pass_var,relief=GROOVE, font=("", 15)).grid(row=6, column=4, padx=0)

        btn_register = Button(Login_Frame,text="Register",command=self.register,width=15,font=("times new roman",15,"bold"),bg="white",fg="Blue").grid(row=8,columnspan=8,pady=10)


    def register(self):
        if self.name_var.get() == "" or self.mail_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.idtype_var.get()=="" or self.idnum_var.get()=="" or self.user_var.get()=="" or self.pass_var.get()=="":
            messagebox.showerror("Error","! All fields are required !")
        elif len(self.contact_var.get()) != 10:
            messagebox.showerror("Error","! Contact number must be 10 digits !")
        else:
            con = pymysql.connect(host='localhost',user="root",password="Rishi@2705",database="stm")
            cur = con.cursor()
            cur.execute("insert into admins values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.name_var.get(),
                self.mail_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.idtype_var.get(),
                self.idnum_var.get(),
                self.user_var.get(),
                self.pass_var.get()
            ))
            con.commit()
            self.clear()
            con.close()
            messagebox.showinfo("Success","User registered successfully")
            self.root.destroy()
            os.system("python3 login.py")

    def clear(self):
        self.name_var.set(""),
        self.mail_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.idtype_var.set(""),
        self.idnum_var.set(""),
        self.user_var.set(""),
        self.pass_var.set("")


root = Tk()
obj = Login_system(root)
root.mainloop()
