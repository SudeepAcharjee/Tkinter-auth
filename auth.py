from tkinter import * # type: ignore
from tkinter import messagebox
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentication System")
        self.root.geometry("1350x1100+0+0")

        # -------Images--------
        self.bg_icon=ImageTk.PhotoImage(file="./images/bg.jpg")
        self.user_icon=PhotoImage(file="./images/man-user.png").subsample(5)  # Adjust the subsample value for icon size
        self.pass_icon=PhotoImage(file="./images/password.png").subsample(8)  # Adjust the subsample value for icon size
        self.logo_icon=PhotoImage(file="./images/icon.png").subsample(3)

        bg_lbl = Label(self.root, image=self.bg_icon)# type: ignore
        bg_lbl.pack()

        title = Label(self.root, text="Login Page", font=("times new roman", 40, "bold"), bg="grey", fg="black", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="blue", bd=5)
        Login_Frame.place(x=400, y=150)

        logolbl = Label(Login_Frame, image=self.logo_icon) # type: ignore
        logolbl.grid(row=0, column=0, pady=10, columnspan=2)

        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT, font=("times new roman", 10, "bold"), bg="black", fg="white")
        lbluser.grid(row=1, column=0, pady=10)
        self.txtuser = Entry(Login_Frame, bd=5, relief=GROOVE, font=("", 15))
        self.txtuser.grid(row=1, column=1, padx=20)

        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT, font=("times new roman", 10, "bold"), bg="black", fg="white")
        lblpass.grid(row=2, column=0, pady=10)
        self.txtpass = Entry(Login_Frame, bd=5, relief=GROOVE, font=("", 15), show="*")
        self.txtpass.grid(row=2, column=1, padx=20)

        btn_login = Button(Login_Frame, text="Login", width=15, font=("times new roman", 14, "bold"), bg="yellow", fg="black", command=self.login)
        btn_login.grid(row=3, columnspan=2, pady=20)

    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "Sudeep" and password == "123456":
            messagebox.showinfo("Login Successful", "Successfully logged in!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password!")

root = Tk()
obj = Login_System(root)
root.mainloop()
