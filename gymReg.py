import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from adminwindow import AdminWindow

class GymRegistrationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Registration System")

        # Load your image (replace the path below with the actual image path)
        img_path = r"C:\Users\Lenovo\OneDrive\Desktop\Tk_Project\img\gym.png"
        self.img = Image.open(img_path)
        self.img = self.img.resize((500, 500), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(self.img)

        # Create a label to display the image
        self.lblimg = tk.Label(self.root, image=self.photoimg)
        self.lblimg.pack()

        # Create a frame for login widgets (overlaying the image)
        login_frame = tk.Frame(self.root, bg="white")
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Registration form elements within the frame
        lbl_name = tk.Label(login_frame, text="UserName:")
        lbl_name.grid(row=1, column=0)

        self.entry_name = tk.Entry(login_frame)
        self.entry_name.grid(row=1, column=1)

        lbl_password = tk.Label(login_frame, text="Password:")
        lbl_password.grid(row=2, column=0)

        self.entry_password = tk.Entry(login_frame, show="*")
        self.entry_password.grid(row=2, column=1)

        btn_login = tk.Button(login_frame, text="Log In", command=self.admin_details)
        btn_login.grid(row=3, column=0, columnspan=2, pady=10)

 
    def admin_details(self):
        # Check credentials (this is just an example, adapt to your needs)
        username = self.entry_name.get()
        password = self.entry_password.get()

        if username == "admin" and password == "admin123":  # Example credentials
            self.root.destroy()  # Close the main window
            self.open_admin_window()  # Open the admin window
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_admin_window(self):
        new_window = tk.Tk()  # Create a new Tkinter instance for the admin window
        app = AdminWindow(new_window)
        new_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    obj = GymRegistrationSystem(root)
    root.mainloop()
