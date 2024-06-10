from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

data_list = []

class AdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration System")
        self.root.geometry("1200x650")
        self.root.configure(background='cornsilk2')

        self.dash_frame = tk.Frame(root, bg='grey')
        self.dash_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.dash_frame.propagate(False)
        self.dash_frame.configure(width=250, height=400)

        self.main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.propagate(False)
        self.main_frame.configure(width=1150, height=700)

        self.Reg_btn = tk.Button(self.dash_frame, text='Registration', font=('Bold', 20), fg="#158aff", bd=0, bg="grey", padx=10, command=lambda: self.change_indicator_color(self.Reg_ind, self.Reg_page))
        self.Reg_btn.place(x=22, y=50)
        self.Reg_ind = tk.Label(self.dash_frame, text="", bg="grey")
        self.Reg_ind.place(x=3, y=50, width=8, height=50)

        self.Menu_btn = tk.Button(self.dash_frame, text='MENU', font=('Bold', 20), fg="#158aff", bd=0, bg="grey", padx=10, command=lambda: self.change_indicator_color(self.Menu_ind, self.Menu_page))
        self.Menu_btn.place(x=22, y=100)
        self.Menu_ind = tk.Label(self.dash_frame, text="", bg="grey")
        self.Menu_ind.place(x=3, y=100, width=8, height=50)

        self.Exit_btn = tk.Button(self.dash_frame, text='Exit', font=('Bold', 20), fg="#158aff", bd=0, bg="grey", padx=10, command=lambda: self.change_indicator_color(self.Exit_ind, self.Exit_page))
        self.Exit_btn.place(x=22, y=600)
        self.Exit_ind = tk.Label(self.dash_frame, text="", bg="grey")
        self.Exit_ind.place(x=3, y=600, width=8, height=50)

        self.accept_var = tk.StringVar(value="Not Accepted")

    def change_indicator_color(self, label, page):
        self.hide_indicator()
        label.config(bg="#158aff")
        self.delete_page()
        page()

    def hide_indicator(self):
        self.Reg_ind.config(bg="grey")
        self.Menu_ind.config(bg="grey")
        self.Exit_ind.config(bg="grey")

    def Reg_page(self):
        Reg_frame = tk.Frame(self.main_frame)
        lb = tk.Label(Reg_frame, text="Gym Registration", padx=40, font=("times new roman", 15))
        lb.grid(row=0, column=0, columnspan=4)

        user_info_frame = tk.LabelFrame(Reg_frame, text="Membership Information")
        user_info_frame.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

        first_name_label = tk.Label(user_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0, sticky="w")
        last_name_label = tk.Label(user_info_frame, text="Last Name")
        last_name_label.grid(row=1, column=0, sticky="w")

        self.first_name_entry = tk.Entry(user_info_frame)
        self.last_name_entry = tk.Entry(user_info_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        Sex_label = tk.Label(user_info_frame, text="Gender")
        self.Sex_combobox = ttk.Combobox(user_info_frame, values=["", "Male", "Female", "Others"])
        Sex_label.grid(row=2, column=0, sticky="w")
        self.Sex_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        age_label = tk.Label(user_info_frame, text="Age")
        self.age_spinbox = tk.Spinbox(user_info_frame, from_=8, to=110)
        age_label.grid(row=3, column=0, sticky="w")
        self.age_spinbox.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        contact_label = tk.Label(user_info_frame, text="Contact number")
        validate_contact_number = (self.root.register(self.validate_contact_num), "%d", "%P")
        contact_label.grid(row=4, column=0)
        self.contact_entry = tk.Entry(user_info_frame, validate="key", validatecommand=validate_contact_number)
        self.contact_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        subscription_label = tk.Label(user_info_frame, text="Subscription Duration (months)")
        subscription_label.grid(row=5, column=0, sticky="w")
        self.subscription_spinbox = tk.Spinbox(user_info_frame, from_=1, to=24)
        self.subscription_spinbox.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        terms_frame = tk.LabelFrame(Reg_frame, text="Terms & Conditions")
        terms_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)

        terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                     variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        terms_check.grid(row=0, column=0, columnspan=4, pady=5)

        # Button to enter data
        enter_button = tk.Button(Reg_frame, text="Enter data", command=self.enter_data)
        enter_button.grid(row=4, column=0, columnspan=2)

        Reg_frame.pack(pady=20)

    def validate_contact_num(self, action, value_if_allowed):
        if action == "1":  # 1 means insertion
            if value_if_allowed.isdigit():
                if len(value_if_allowed) <= 11:
                    return True
                else:
                    messagebox.showerror("Error", "Contact number cannot exceed 11 digits.")
                    return False
            else:
                messagebox.showerror("Error", "Invalid contact number. Only digits are allowed.")
                return False
        return True

    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            # User info
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            title = self.Sex_combobox.get()
            age = self.age_spinbox.get()
            contact = self.contact_entry.get()
            subscription_duration = self.subscription_spinbox.get()

            # Validate data
            if not firstname or not lastname or not title or not age or not contact or not subscription_duration:
                messagebox.showerror("Error", "Please fill in all fields")
                return

            # Calculate expiry date
            expiry_date = datetime.now() + timedelta(days=int(subscription_duration) * 30)

            # Append data to the global list
            data_list.append({
                "First Name": firstname,
                "Last Name": lastname,
                "Title": title,
                "Age": age,
                "Contact number": contact,
                "Subscription Duration": subscription_duration,
                "Expiry Date": expiry_date.strftime('%Y-%m-%d')
            })
            messagebox.showinfo("Success", "Data entered and saved.")
        else:
            messagebox.showwarning(title="Error", message="You have not accepted the terms")

    def Menu_page(self):

            Menu_frame = tk.Frame(self.main_frame)

    # Add search interface to upper right corner
            search_frame = tk.Frame(Menu_frame)
            search_frame.pack(side=tk.RIGHT, padx=10, pady=10)

            lb = tk.Label(Menu_frame, text="Registered Members", font=("times new roman", 20))
            lb.pack(pady=10)

            columns = ("First Name", "Last Name", "Title", "Age", "Contact number", "Subscription Duration", "Expiry Date")
            self.tree = ttk.Treeview(Menu_frame, columns=columns, show="headings")
            self.tree.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

            for col in columns:
               self.tree.heading(col, text=col)
               self.tree.column(col, minwidth=0, width=100)

    # Insert data into the Treeview
            for entry in data_list:
               self.tree.insert("", tk.END, values=(entry["First Name"], entry["Last Name"], entry["Title"], entry["Age"], entry["Contact number"], entry["Subscription Duration"], entry["Expiry Date"]))

    # Add a scrollbar
            scrollbar = ttk.Scrollbar(Menu_frame, orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Add Update and Delete buttons
            button_frame = tk.Frame(Menu_frame)
            button_frame.pack(fill=tk.X, pady=10)

            update_button = tk.Button(button_frame, text="Update", command=self.update_entry)
            update_button.pack(side=tk.LEFT, padx=10)

            delete_button = tk.Button(button_frame, text="Delete", command=self.delete_entry)
            delete_button.pack(side=tk.LEFT, padx=10)
  
            search_button = tk.Button(button_frame, text="Search", command=self.search)
            search_button.pack(side=tk.RIGHT, padx=10)

            self.search_entry = tk.Entry(button_frame)
            self.search_entry.pack(side=tk.RIGHT, padx=10)

            search_label = tk.Label(button_frame, text="Search:")
            search_label.pack(side=tk.RIGHT, padx=10)

            Menu_frame.pack(expand=True, fill=tk.BOTH, pady=20, padx=20)



    def search(self):
            query = self.search_entry.get().lower()  # Get the search query from the entry field and convert to lowercase

    # Clear the current data in the Treeview
            self.tree.delete(*self.tree.get_children())

    # Filter the data_list based on the search query
            for entry in data_list:
                  if query in entry["First Name"].lower() or query in entry["Last Name"].lower() or query in entry["Contact number"].lower():
            # Insert the matching entry into the Treeview
                   self.tree.insert("", tk.END, values=(entry["First Name"], entry["Last Name"], entry["Title"], entry["Age"], entry["Contact number"], entry["Subscription Duration"], entry["Expiry Date"]))



    def update_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected")
            return
    

        self.selected_item = selected_item
    # Get values of selected item
        item_values = self.tree.item(selected_item, 'values')

    # Create a new window for editing
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Edit Details")
        self.edit_window.geometry("400x300")
    
    # Labels and entry fields for editing
        tk.Label(self.edit_window, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.first_name_entry = tk.Entry(self.edit_window)
        self.first_name_entry.insert(0, item_values[0])
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edit_window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.last_name_entry = tk.Entry(self.edit_window)
        self.last_name_entry.insert(0, item_values[1])
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edit_window, text="Gender:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.sex_combobox = ttk.Combobox(self.edit_window, values=["", "Male", "Female", "Others"])
        self.sex_combobox.set(item_values[2])
        self.sex_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edit_window, text="Age:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.age_spinbox = tk.Spinbox(self.edit_window, from_=8, to=110)
        self.age_spinbox.insert(0, item_values[3])
        self.age_spinbox.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edit_window, text="Contact number:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.contact_entry = tk.Entry(self.edit_window)
        self.contact_entry.insert(0, item_values[4])
        self.contact_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edit_window, text="Subscription Duration (months):").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.subscription_spinbox = tk.Spinbox(self.edit_window, from_=1, to=24)
        self.subscription_spinbox.insert(0, item_values[5])
        self.subscription_spinbox.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    # Save button
        save_button = tk.Button(self.edit_window, text="Save Changes", command=self.save_changes)
        save_button.grid(row=6, column=0, columnspan=2, pady=10)



    




    def save_changes(self):
        new_values = [
          self.first_name_entry.get(),
          self.last_name_entry.get(),
          self.sex_combobox.get(),
          self.age_spinbox.get(),
          self.contact_entry.get(),
          self.subscription_spinbox.get()
        ]

    # Validate data
        if not all(new_values):
            messagebox.showerror("Error", "Please fill in all fields")
            return

    # Calculate expiry date
        expiry_date = datetime.now() + timedelta(days=int(new_values[5]) * 30)

    # Update data_list with new values
        item_index = self.tree.index(self.selected_item)
        data_list[item_index] = {
        "First Name": new_values[0],
        "Last Name": new_values[1],
        "Title": new_values[2],
        "Age": new_values[3],
        "Contact number": new_values[4],
        "Subscription Duration": new_values[5],
        "Expiry Date": expiry_date.strftime('%Y-%m-%d')
    }

    # Update Treeview with new values
        self.tree.item(self.selected_item, values=new_values)

        messagebox.showinfo("Success", "Data updated successfully")

    # Close the edit window
        self.edit_window.destroy()



    def delete_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?")
        if confirm:
            item_index = self.tree.index(selected_item)
            self.tree.delete(selected_item)
            data_list.pop(item_index)
            messagebox.showinfo("Deleted", "Entry deleted successfully")

    def Exit_page(self):
            Exit_frame = tk.Frame(self.main_frame)

    # Label indicating logout
            lb = tk.Label(Exit_frame, text="Are you sure you want to logout?", font=("times new roman", 30))
            lb.pack()

    # Button to confirm logout and close the program
            logout_button = tk.Button(Exit_frame, text="Logout", padx= 20 , pady=20 ,command=self.root.destroy)
            logout_button.pack()

            Exit_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    obj = AdminWindow(root)
    root.mainloop()
