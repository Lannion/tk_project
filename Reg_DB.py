import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient
from test_DB import TestWindow 


class Reg_DB:
    def __init__(self, root):
        # Initialize the main window / set the title
        self.root = root
        self.root.title("Gym Registration System")

        # Locate/resize the image to be displayed
        img_path = r"C:\Users\Lenovo\OneDrive\Desktop\Tk_Project\img\gym.png"
        self.img = Image.open(img_path)
        self.img = self.img.resize((500, 500), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(self.img)

        # label to display the image
        self.lblimg = tk.Label(self.root, image=self.photoimg)
        self.lblimg.pack()

        #login frame centered in the window
        login_frame = tk.Frame(self.root, bg="white")
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #label/entry for the username
        lbl_name = tk.Label(login_frame, text="Username:")
        lbl_name.grid(row=1, column=0)

        self.entry_name = tk.Entry(login_frame)
        self.entry_name.grid(row=1, column=1)

        #label/entry for the password
        lbl_password = tk.Label(login_frame, text="Password:")
        lbl_password.grid(row=2, column=0)

        self.entry_password = tk.Entry(login_frame, show="*")
        self.entry_password.grid(row=2, column=1)

        # login button that triggers the admin_details method
        btn_login = tk.Button(login_frame, text="Log In", command=self.admin_details)
        btn_login.grid(row=3, column=0, columnspan=2, pady=10)

        # Setting up MongoDB connection
        self.setup_mongodb()

    # Method for MongoDB connection
    def setup_mongodb(self):
        uri = "mongodb://localhost:27017/"
        self.client = MongoClient(uri)
        self.db = self.client['Database']

    # Method to handle login details
    def admin_details(self):
        username = self.entry_name.get()
        password = self.entry_password.get()

        # query database for the user
        user = self.db['users'].find_one({"username": username, "password": password})
        if user:
            # If user exists, destroy the current window and open TestWindow
            self.root.destroy() 
            self.open_Test_DB()
        else:
            # If user does not exist, show an error message
            messagebox.showerror("Error", "Invalid username or password")

    # Method to open a new window (TestWindow)
    def open_Test_DB(self):
        new_window = tk.Tk()
        app = TestWindow(new_window)
        new_window.mainloop()

# Main function to start application
if __name__ == "__main__":
    root = tk.Tk()
    obj = Reg_DB(root)
    root.mainloop()
