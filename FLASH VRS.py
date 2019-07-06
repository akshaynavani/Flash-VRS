from tkinter import *
import sqlite3
import tkinter.messagebox

conn=sqlite3.connect("project.db")
print("CONNECTED!!!")

avail_car = {'CAR':6,'7-SEATER':5,'SUV':4,'9-SEATER':3,'MINI BUS':2,'BUS':2}

def create_table():
    register_query=str("CREATE TABLE IF NOT EXISTS register(register_username VARCHAR,"+
                     "register_password VARCHAR,"+
                     "register_rpassword VARCHAR,"+
                     "register_email VARCHAR PRIMARY KEY,"+
                     "register_mobile INTEGER)")
                     
    conn.execute(register_query)
    print("created client table")


class project:

    def insertdetails(self):
            username=self.e_rusername.get()
            email=self.e_email.get()
            mobile=self.e_mobile.get()
            password=self.e_rpassword.get()
            rpassword=self.e_rpass.get()
            if(username=='' or email==''or mobile==''or password==''or rpassword==''):
                tkinter.messagebox.showinfo("Error", "Please Enter all the details")
            else:
                
                    try:
                        query=str("INSERT INTO register(register_username, register_password, register_rpassword, register_email, register_mobile) VALUES(?,?,?,?,?)")
                        conn.execute(query,(username,password,rpassword,email,mobile,))
                        conn.commit()
                    except sqlite3.IntegrityError:
                        tkinter.messagebox.showinfo("Error", "The entered EMAIL ID is already present")
                    else:
                        if(rpassword==password):
                            print("registered")
                            tkinter.messagebox.showinfo("SUCCESSFUL", "REGISTRATION DONE SUCCESSFULLY")
                            self.login()
                        else:
                            tkinter.messagebox.showinfo("Error", "The re-entered password doesnt match previous password")


    def checkLogin(self):
        un=self.e_username.get()
        pw=self.e_password.get()
        if(self.e_username.get()=="" or self.e_password.get()==""):
                tkinter.messagebox.showinfo("Error", "PLEASE FILL ALL THE CREDENTIALS")
        r=conn.execute("SELECT * FROM register WHERE register_email=? AND register_password=?",(self.e_username.get(),self.e_password.get(),)) 
        for i in r:
            if(self.e_username.get()==i[3] and self.e_password.get()==i[1]):
                self.booking_page()
            if((un==i[3] and pw==i[1])==False):
                tkinter.messagebox.showinfo("Wrong Credentials!", "INVALID EMAIL OR PASSWORD")
		
		    
    def book_car(self):
        if(self.e_cust_name.get()=='' or self.e_contact.get()=='' or self.e_source.get()=='' or self.e_destination.get()=='' or self.e_days.get()==''):
                tkinter.messagebox.showinfo("Error","PLEASE FILL ALL DETAILS BEFORE BOOKING")
        if(self.tkvar.get()==''):
                tkinter.messagebox.showinfo("Error","SELECT A VEHICLE BEFORE BOOKING")
        else:
            print(str(self.tkvar.get()))
            if(avail_car[self.tkvar.get()]!=0):
                self.RentalCost()
                avail_car[self.tkvar.get()]=int(avail_car[self.tkvar.get()])-1
                print(avail_car[self.tkvar.get()])
                tkinter.messagebox.showinfo("SUCCESSFUL", "BO0KING DONE")
            else:
                tkinter.messagebox.showinfo("VEHICLE NOT AVAILABLE", "TRY BOOKING LATER")
            
            
    def qexit(self):
        qexit=tkinter.messagebox.askyesno("LOGOUT","Do you want to log out?")
        if qexit>0:
            self.login()
            

    def RentalCost(self):
        noOfDays=int(self.e_days.get())

        if(self.tkvar.get()=="CAR"):
           rent=noOfDays*500
        elif(self.tkvar.get()=="7-SEATER"):
           rent=noOfDays*650
        elif(self.tkvar.get()=="SUV"):
           rent=noOfDays*700
        elif(self.tkvar.get()=="9-SEATER"):
           rent=noOfDays*800
        elif(self.tkvar.get()=="MINI BUS"):
           rent=noOfDays*1000
        else:
            rent=noOfDays*1500

        self.t.delete(0,tkinter.END)
        self.t.insert(0,rent)
        return
    
    def login(self):
            self.frame.destroy()
            self.frame = Frame(root, height=500, width=700,bd=8,relief="raise",bg="grey74")
            self.frame.pack()
            #labels
            lbl = Label(self.frame,font=('arial',16,'bold'),text="Enter your EMAIL ",bd=16,bg="grey74",anchor='w')
            lbl.grid(row=0, column=0, padx=5, pady=5)
            lb2 = Label(self.frame,font=('arial',16,'bold'),text="Enter password",bd=16,bg="grey74",anchor='w')
            lb2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
            #entry fields
            self.e_username = Entry(self.frame,font=('arial',16),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_username.grid(row=0, column=1, padx=5, pady=5)
            self.e_password = Entry(self.frame,font=('arial',16),show="*",fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_password.grid(row=1, column=1, padx=5, pady=5)
            #button
            b = Button(self.frame,font=('arial',16,'bold'),text="LOGIN",bg="grey",command=self.checkLogin)
            b.grid(row=2, column=0, columnspan=2)
            self.frame.grid_propagate(0)

    def register(self):
            self.frame.destroy()
            self.frame = Frame(root, height=500, width=700,bd=8,relief="raise",bg="grey74")
            self.frame.pack()
            #labels
            lbl = Label(self.frame,font=('arial',16,'bold'),text="Enter username",bd=16,bg="grey74",anchor='w')
            lbl.grid(row=0, column=0, padx=5, pady=5)
            lb2 = Label(self.frame,font=('arial',16,'bold'),text="Enter password",bd=16,bg="grey74",anchor='w')
            lb2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
            lb3 = Label(self.frame,font=('arial',16,'bold'), text="Re-Enter password",bd=16,bg="grey74",anchor='w')
            lb3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
            lbl4= Label(self.frame,font=('arial',16,'bold'),text='Email',bd=16,bg="grey74",anchor='w')
            lbl4.grid(row=3,column=0)
            lbl5= Label(self.frame,font=('arial',16,'bold'),text='Mobile',bd=16,bg="grey74",anchor='w')
            lbl5.grid(row=4,column=0)
            #entry fields
            self.e_rusername= Entry(self.frame,font=('arial',16),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_rusername.grid(row=0, column=1, padx=5, pady=5)
            self.e_rpassword = Entry(self.frame,font=('arial',16),show="*",fg="black",bd=5,insertwidth=10,bg="white",justify='left')        
            self.e_rpassword.grid(row=1, column=1, padx=5, pady=5)
            self.e_rpass= Entry(self.frame,font=('arial',16),show="*",fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_rpass.grid(row=2, column=1, padx=5, pady=5)
            self.e_email=Entry(self.frame,font=('arial',16),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_email.grid(row=3,column=1)
            self.e_mobile=Entry(self.frame,font=('arial',16),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_mobile.grid(row=4,column=1)
            #register button
            b = Button(self.frame,font=('arial',16,'bold'),text="REGISTER",bg="grey",command=self.insertdetails)
            b.grid(row=5,column=0,columnspan=2)
            self.frame.grid_propagate(0)

    def booking_page(self):
            self.frame.destroy()
            self.frame = Frame(root, height=500, width=750,bd=8,relief="raise",bg="grey74")
            self.frame.pack()
            #labels
            lbl = Label(self.frame,font=('arial',10,'bold'),text="CUSTOMER NAME",bd=16,bg="grey74",anchor='w')
            lbl.grid(row=0, column=1, padx=5, pady=5)
            lb2 = Label(self.frame,font=('arial',10,'bold'),text="CONTACT NO: ",bd=16,bg="grey74",anchor='w')
            lb2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            lb3 = Label(self.frame,font=('arial',10,'bold'), text="SELECT VEHICLE",bd=16,bg="grey74",anchor='w')
            lb3.grid(row=2, column=1, padx=5, pady=5, sticky=W)
            lbl4= Label(self.frame,font=('arial',10,'bold'),text='SOURCE',bd=16,bg="grey74",anchor='w')
            lbl4.grid(row=3,column=0)
            lbl5= Label(self.frame,font=('arial',10,'bold'),text='DESTINATION',bg="grey74",bd=16,anchor='w')
            lbl5.grid(row=4,column=0)
            lbl6= Label(self.frame,font=('arial',10,'bold'),text='NO. OF DAYS RENTED',bg="grey74",bd=16,anchor='w')
            lbl6.grid(row=3,column=2)
            lbl7= Label(self.frame,font=('arial',10,'bold'),text='TOTAL',bd=16,bg="grey74",anchor='w')
            lbl7.grid(row=4,column=2)
            self.frame.grid_propagate(0)
            #entry fields
            self.e_cust_name = Entry(self.frame,font=('arial',12),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_cust_name.grid(row=0, column=2, padx=5, pady=5)
            self.e_contact = Entry(self.frame,font=('arial',12),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_contact.grid(row=1, column=2, padx=5, pady=5)
            self.e_source=Entry(self.frame,font=('arial',12),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_source.grid(row=3,column=1)
            self.e_destination=Entry(self.frame,font=('arial',12),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_destination.grid(row=4,column=1)
            self.e_days=Entry(self.frame,font=('arial',12),fg="black",bd=5,insertwidth=10,bg="white",justify='left')
            self.e_days.grid(row=3,column=3)
            self.t=Entry(self.frame,font=('arial',10),fg="black",bd=5,insertwidth=5,bg="white",justify='left')
            self.t.grid(row=4,column=3)
            #buttons
            b2 = Button(self.frame,font=('arial',16,'bold'),text="BOOK",bg="grey",command=self.book_car)
            b2.grid(row=6,column=1,rowspan=2)
            b3 = Button(self.frame,font=('arial',16,'bold'),text="LOG OUT",bg="grey",command=self.qexit)
            b3.grid(row=6,column=3,rowspan=2)
            #dropdown list
            self.tkvar = StringVar(self.frame)
            choices = ['CAR','7-SEATER','SUV','9-SEATER','MINI BUS','BUS']            
            popupMenu = OptionMenu(self.frame, self.tkvar, *choices)
            popupMenu.grid(row=2, column=2, padx=5, pady=5) 
            # on change dropdown value
            #def change_dropdown(*args):
            #    print( tkvar.get() ) 
            # link function to change dropdown
            #tkvar.trace('w', change_dropdown)

    def __init__(self,root):
        self.frame=Frame(root,height=500,width=700,bg="grey74")
        self.frame.pack()
        #labels
        self.title=Label(self.frame,font=('arial',20,'bold'),text="FLASH VEHICLE RENTAL SERVICE",bg="grey74",fg="black")
        self.title.pack(side=TOP)
        self.title2=Label(self.frame,font=('arial',10,'bold','italic'),text="FLEXIBLE.ACCESSIBLE.AFFORDABLE",bg="grey74",fg="maroon")
        self.title2.pack(side=TOP)
        #buttons
        self.login_button=Button(self.frame,font=('arial',16,'bold'),text="LOGIN",fg="black",bg="grey",command=self.login)
        self.login_button.pack(side=BOTTOM,fill=X,padx=10,pady=10)
        self.reg_button=Button(self.frame,font=('arial',16,'bold'),text="REGISTER",fg="black",bg="grey",command=self.register)
        self.reg_button.pack(side=BOTTOM,fill=X,padx=10,pady=10)
        self.frame.pack_propagate(0)

        
#main
create_table()

result = conn.execute("select * from register")
for i in result:
    print("id = {}  pass= {}".format(i[3],i[1]))

root=Tk()
c=project(root)
root.mainloop()
