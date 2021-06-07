from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os
import sys
import random
import smtplib
import time
class Login_system:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1920x1080+0+0")

        ################################# All images

        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=PhotoImage(file="images/username.png")
        self.pass_icon=PhotoImage(file="images/pass.png")
        self.logo_icon = PhotoImage(file="images/mainlogo.png")
        self.email_icon = PhotoImage(file="images/mail.png")
        self.otp_icon = PhotoImage(file="images/otp.png")


        ############################################# Variables
        self.user_var=StringVar()
        self.pass_var = StringVar()
        self.forgot_email_var = StringVar()
        self.new_pass_var = StringVar()
        self.userotp_var = StringVar()
        self.originalotp_var = StringVar()
        self.otp_trylimit_var = 3
        self.strt_time_var = 0
        self.end_time_var = 0
        self.time_var = 0

        bg_label = Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login Panel",font=("Times new roman",40,"bold"),bg="grey14",fg="yellow3",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root,bg="forest green")
        Login_Frame.place(x=200,y=150)
        logo_lbl = Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        user_lbl = Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="forest green").grid(row=1,column=0,padx=20,pady=10)
        txt_user = Entry(Login_Frame,bd="5",textvariable=self.user_var,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        pass_lbl = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=2, column=0, padx=20,pady=10)
        txt_pass = Entry(Login_Frame, bd="5", show = "*",textvariable=self.pass_var,relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        btn_login = Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman",15,"bold"),bg="white",fg="Blue").grid(row=3,column=1,pady=10)
        btn_register = Button(Login_Frame, text="Register", width=15, command=self.register,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=3, column=0, pady=10)
        btn_forgot = Button(Login_Frame, text="Forgot Password", width=15, command=self.forgot_pass,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=4, columnspan=2,pady=10)




    def login(self):
        if self.user_var.get()=="" or self.pass_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
            cur = con.cursor()
            cur.execute("SELECT password FROM `admins` WHERE user='" + str(self.user_var.get()) + "'")
            rows=cur.fetchone()
            if rows:
                # print(rows[0])
                # print(self.pass_var.get())
                if rows[0] == self.pass_var.get():
                    self.root.destroy()
                    import Student
                    Student.Students()
                else:
                    messagebox.showerror("Invalid","Username and password did not match")
            else:
                messagebox.showerror("Invalid", "Username and password did not match")
    def register(self):
        self.root.destroy()
        os.system("python3 register.py")

    def forgot_pass(self):
        self.otp_trylimit_var=3
        self.Forgot_Frame = Frame(self.root, bg="forest green")
        self.Forgot_Frame.place(x=800, y=150)

        email_lbl = Label(self.Forgot_Frame, text="Email", image=self.email_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=1, column=0, padx=20,pady=10)
        txt_email = Entry(self.Forgot_Frame, bd="5", textvariable=self.forgot_email_var, relief=GROOVE, font=("", 15)).grid(row=1,column=1, padx=20)

        # new_pass_lbl = Label(self.Forgot_Frame, text="New password", image=self.email_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="forest green").grid(row=2, column=0, padx=20, pady=10)
        # txt_new_pass = Entry(self.Forgot_Frame, bd="5", textvariable=self.new_pass_var, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        btn_sendotp = Button(self.Forgot_Frame, text="Send OTP", width=15, command=self.sendotp,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=3, column=1, pady=10)

    def sendotp(self):
        # self.Forgot_Frame.destroy()
        # self.Forgot_Frame = Frame(self.root, bg="forest green")
        # self.Forgot_Frame.place(x=800, y=150)
        # otp_lbl = Label(self.Forgot_Frame, text="OTP", image=self.otp_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=3, column=0, padx=20,pady=10)
        # txt_otp = Entry(self.Forgot_Frame, bd="5", textvariable=self.userotp_var, relief=GROOVE,font=("", 15)).grid(row=3, column=1, padx=20)
        # btn_submitotp = Button(self.Forgot_Frame, text="Verify", width=15, command=self.verifyotp,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=4,column=1,pady=10)
        # btn_back = Button(self.Forgot_Frame, text="Back", width=10, command=self.back,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=4, column=0, pady=10)
        self.strt_time_var = time.time()
        if self.forgot_email_var.get() == "":
            messagebox.showerror("Error","Please enter a email address")
        else:
            con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
            cur = con.cursor()
            cur.execute("SELECT mail FROM `admins`")
            rows = cur.fetchall()
            st = False
            for i in rows:
                if i[0] == self.forgot_email_var.get():
                    st = True
                    break
            if st == False:
                messagebox.showerror("Error","Entered email address is not linked to any account")
                self.forgot_email_var.set("")
            else:
                self.Forgot_Frame = Frame(self.root, bg="forest green")
                self.Forgot_Frame.place(x=800, y=150)
                otp_lbl = Label(self.Forgot_Frame, text="OTP", image=self.otp_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=3, column=0, padx=20,pady=10)
                txt_otp = Entry(self.Forgot_Frame, bd="5", textvariable=self.userotp_var, relief=GROOVE,font=("", 15)).grid(row=3, column=1, padx=20)
                btn_submitotp = Button(self.Forgot_Frame, text="Verify", width=15, command=self.verifyotp,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=4,column=1,pady=10)
                btn_back = Button(self.Forgot_Frame, text="Back", width=10, command=self.back,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=4, column=0, pady=10)

                vals = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwwxyz"
                self.originalotp_var = ""
                for i in range(6):
                    self.originalotp_var += (random.choice(vals))
                subject = 'Reset password OTP'
                part1 = 'Hello user,'
                part2 = 'This is your otp for reset your password:'
                part3 = 'NOTE: This OTP is valid for 5 minute and you can attempt 3 times.'
                msg = f'Subject: {subject}\n\n{part1}\n{part2}\n{self.originalotp_var}\n{part3}'
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("contactus.indian@gmail.com", "Rishi@2705")
                s.sendmail("contactus.indian@gmail.com", self.forgot_email_var.get(), msg)

                # self.Forgot_Frame.destroy()
                # self.Forgot_Frame = Frame(self.root, bg="forest green")
                # self.Forgot_Frame.place(x=800, y=150)



    def verifyotp(self):
        self.end_time_var = time.time()
        self.time_var = self.end_time_var - self.strt_time_var
        if self.time_var > 60:
            messagebox.showerror("Timeout","Your OTP is expired, Try again")
            self.Forgot_Frame.destroy()
            self.forgot_pass()
        elif self.userotp_var.get()=="":
            messagebox.showerror("Error","Please enter a OTP")
        else:
            if str(self.userotp_var.get())==str(self.originalotp_var):
                self.Forgot_Frame.destroy()
                self.Forgot_Frame = Frame(self.root, bg="forest green")
                self.Forgot_Frame.place(x=800, y=150)
                new_pass_lbl = Label(self.Forgot_Frame, text="New password", image=self.email_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="forest green").grid(row=4, column=0, padx=20, pady=10)
                txt_new_pass = Entry(self.Forgot_Frame, bd="5", textvariable=self.new_pass_var, relief=GROOVE,font=("", 15)).grid(row=4, column=1, padx=20)

                btn_update = Button(self.Forgot_Frame, text="Update", width=15, command=self.update_pass,font=("times new roman", 15, "bold"), bg="white", fg="Blue").grid(row=5,column=1,pady=10)


            else:
                messagebox.showerror("Error","OTP does not match")
                self.otp_trylimit_var -= 1
                if self.otp_trylimit_var != 0:
                    self.sendotp()
                else:
                    messagebox.showerror("Locked","Your account is locked,Please contact administrator")
                    self.Forgot_Frame.destroy()
                    self.forgot_email_var.set("")
                    self.login()

    def update_pass(self):
        if self.new_pass_var.get()=="":
            messagebox.showerror("Error","Enter a password")
        else:
            con = pymysql.connect(host='localhost', user="root", password="Rishi@2705", database="stm")
            cur = con.cursor()
            cur.execute("UPDATE `admins` SET password='"+str(self.new_pass_var.get())+"' WHERE mail='"+str(self.forgot_email_var.get())+"'")
            con.commit()
            con.close()
            self.Forgot_Frame.destroy()
            messagebox.showinfo("Success","Password updated successfully")
            self.Forgot_Frame.destroy()
    def back(self):
        self.Forgot_Frame.destroy()
        self.forgot_pass()


root = Tk()
obj = Login_system(root)
root.mainloop()
