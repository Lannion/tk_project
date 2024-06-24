import tkinter as tk
from tkinter import ttk, messagebox
import pymongo
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

# Connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Database"]
collection = db["GymMembers"]

class TestWindow:
    def __init__(self, root):
        # Setting up the main window
        self.root = root
        self.root.title("Registration System")
        self.root.geometry("1200x650")
        self.root.configure(background='cornsilk2')

        # Dashboard frame
        self.dash_frame = tk.Frame(root, bg='grey')
        self.dash_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.dash_frame.propagate(False)
        self.dash_frame.configure(width=250, height=400)

        # Main frame
        self.main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.propagate(False)
        self.main_frame.configure(width=1150, height=700)

        # Buttons on the dashboard
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

        # Initializing the accept_var
        self.accept_var = tk.StringVar(value="Not Accepted")

        #Change the color of the selected indicator and display the corresponding page
    def change_indicator_color(self, label, page):
        self.hide_indicator()
        label.config(bg="#158aff")
        self.delete_page()
        page()

        #Reset the color of all indicators to grey 
    def hide_indicator(self):
        self.Reg_ind.config(bg="grey")
        self.Menu_ind.config(bg="grey")
        self.Exit_ind.config(bg="grey")

        #Display the registration page
    def Reg_page(self):
        Reg_frame = tk.Frame(self.main_frame)
        lb = tk.Label(Reg_frame, text="Gym Registration", padx=40, font=("times new roman", 15))
        lb.grid(row=0, column=0, columnspan=4)

        # User info frame
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

        enter_button = tk.Button(Reg_frame, text="Enter data", command=self.enter_data)
        enter_button.grid(row=4, column=0, columnspan=2)

        Reg_frame.pack(pady=20)

     #Validate the inputed contact number
    def validate_contact_num(self, action, value_if_allowed):
        if action == "1": 
            if value_if_allowed.isdigit():
                if len(value_if_allowed) <= 11:
                    if value_if_allowed.startswith("0"):
                       return True
                    else:
                       messagebox.showerror("Error", "Contact number must start with '09'.")
                       return False
                else:
                  messagebox.showerror("Error", "Contact number must be exactly 11 digits.")
                  return False
            else:
                messagebox.showerror("Error", "Invalid contact number. Only digits are allowed.")
                return False
        return True
 
     #Enter data into the database
    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            sex = self.Sex_combobox.get()
            age = self.age_spinbox.get()
            contact = self.contact_entry.get()
            subscription_duration = self.subscription_spinbox.get()

            # Validate data/registration
            if not firstname or not lastname or not sex or not age or not contact or not subscription_duration:
                messagebox.showerror("Error", "Please fill in all fields")
                return

            expiry_date = datetime.now() + timedelta(days=int(subscription_duration) * 30)

            collection.insert_one({
                "FirstName": firstname,
                "LastName": lastname,
                "Sex": sex,
                "Age": int(age),
                "ContactNumber": contact,
                "SubscriptionDuration": subscription_duration,
                "ExpiryDate": expiry_date.strftime('%d-%m-%Y')
            })
            messagebox.showinfo("Success", "Data entered and saved.")
        else:
            messagebox.showwarning(title="Error", message="You have not accepted the terms")

        #Display the menu page
    def Menu_page(self):
        Menu_frame = tk.Frame(self.main_frame)

        search_frame = tk.Frame(Menu_frame)
        search_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        lb = tk.Label(Menu_frame, text="Registered Members", font=("times new roman", 20))
        lb.pack(pady=10)

        columns = ("First Name", "Last Name", "Sex", "Age", "Contact number", "Subscription Duration", "Expiry Date")
        self.tree = ttk.Treeview(Menu_frame, columns=columns, show="headings")
        self.tree.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)
         
         #check expiry- will turn bg to red if is not valid
        for col in columns:
           self.tree.heading(col, text=col)
           self.tree.column(col, minwidth=0, width=100)

        self.tree.tag_configure('expired', background='red')
        self.tree.tag_configure('valid', background='white')

        global data_list
        data_list = list(collection.find())
        for entry in data_list:
            expiry_date = datetime.strptime(entry["ExpiryDate"], '%d-%m-%Y')
            current_date = datetime.now()
            tag = 'expired' if expiry_date < current_date else 'valid'
            self.tree.insert("", tk.END, values=(entry["FirstName"], entry["LastName"], entry["Sex"], entry["Age"],
                                                 entry["ContactNumber"], entry["SubscriptionDuration"],
                                                 entry["ExpiryDate"]), tags=(tag,))

        scrollbar = ttk.Scrollbar(Menu_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

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

        generate_button = tk.Button(button_frame, text="Generate Image", command=self.generate_image)
        generate_button.pack(side=tk.LEFT, padx=10)

        Menu_frame.pack(expand=True, fill=tk.BOTH, pady=20, padx=20)

    def search(self):
        # Get the search query from the search entry field and convert it to lowercase
        query = self.search_entry.get().lower()  
        #clear current entries in treeview
        self.tree.delete(*self.tree.get_children())

        # Filter the data_list based on the search query
        data_list = collection.find({
            "$or": [
                {"FirstName": {"$regex": query, "$options": "i"}},
                {"LastName": {"$regex": query, "$options": "i"}},
                {"Sex": {"$regex": query, "$options": "i"}},
                {"ContactNumber": {"$regex": query, "$options": "i"}},
                {"SubscriptionDuration": {"$regex": query, "$options": "i"}},
                {"ExpiryDate": {"$regex": query, "$options": "i"}}
            ]
        })

        # Insert the filtered data into the treeview with appropriate tags
        for entry in data_list:
            expiry_date = datetime.strptime(entry["ExpiryDate"], '%d-%m-%Y')
            current_date = datetime.now()
            tag = 'expired' if expiry_date < current_date else 'valid'
            self.tree.insert("", tk.END, values=(entry["FirstName"], entry["LastName"], entry["Sex"], entry["Age"],
                                                 entry["ContactNumber"], entry["SubscriptionDuration"],
                                                 entry["ExpiryDate"]), tags=(tag,))

    def update_entry(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if selected_item:
             # Get the item details and find the corresponding member in the database
            item = self.tree.item(selected_item)
            item_id = item["values"]
            member = collection.find_one({"FirstName": item_id[0], "LastName": item_id[1]})
            if member:
                # If the member is found, open the update popup with the member's details
                self.update_popup(member)
        else:
            messagebox.showwarning("Warning", "Please select an entry to update.")

        # Create a new window for updating the entry
    def update_popup(self, member):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Entry")
        update_window.geometry("400x300")

        first_name_label = tk.Label(update_window, text="First Name")
        first_name_label.grid(row=0, column=0, padx=10, pady=5)
        first_name_entry = tk.Entry(update_window)
        first_name_entry.insert(0, member["FirstName"])
        first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        last_name_label = tk.Label(update_window, text="Last Name")
        last_name_label.grid(row=1, column=0, padx=10, pady=5)
        last_name_entry = tk.Entry(update_window)
        last_name_entry.insert(0, member["LastName"])
        last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        sex_label = tk.Label(update_window, text="Gender")
        sex_label.grid(row=2, column=0, padx=10, pady=5)
        sex_combobox = ttk.Combobox(update_window, values=["", "Male", "Female", "Others"])
        sex_combobox.set(member["Sex"])
        sex_combobox.grid(row=2, column=1, padx=10, pady=5)

        age_label = tk.Label(update_window, text="Age")
        age_label.grid(row=3, column=0, padx=10, pady=5)
        age_spinbox = tk.Spinbox(update_window, from_=8, to=110)
        age_spinbox.delete(0, "end")
        age_spinbox.insert(0, member["Age"])
        age_spinbox.grid(row=3, column=1, padx=10, pady=5)

        contact_label = tk.Label(update_window, text="Contact Number")
        contact_label.grid(row=4, column=0, padx=10, pady=5)
        contact_entry = tk.Entry(update_window)
        contact_entry.insert(0, member["ContactNumber"])
        contact_entry.grid(row=4, column=1, padx=10, pady=5)

        subscription_label = tk.Label(update_window, text="Subscription Duration")
        subscription_label.grid(row=5, column=0, padx=10, pady=5)
        subscription_spinbox = tk.Spinbox(update_window, from_=1, to=24)
        subscription_spinbox.delete(0, "end")
        subscription_spinbox.insert(0, member["SubscriptionDuration"])
        subscription_spinbox.grid(row=5, column=1, padx=10, pady=5)

        # list of updated data from the entry fields
        def save_updates():
            updated_data = {
                "FirstName": first_name_entry.get(),
                "LastName": last_name_entry.get(),
                "Sex": sex_combobox.get(),
                "Age": int(age_spinbox.get()),
                "ContactNumber": contact_entry.get(),
                "SubscriptionDuration": subscription_spinbox.get(),
                "ExpiryDate": (datetime.now() + timedelta(days=int(subscription_spinbox.get()) * 30)).strftime('%d-%m-%Y')
            }

            # Update the member information in database
            collection.update_one({"FirstName": member["FirstName"], "LastName": member["LastName"]}, {"$set": updated_data})
            messagebox.showinfo("Success", "Entry updated successfully.")

            # Refresh the TABLE
            self.tree.delete(*self.tree.get_children())
            data_list = collection.find()
            for entry in data_list:
                expiry_date = datetime.strptime(entry["ExpiryDate"], '%d-%m-%Y')
                current_date = datetime.now()
                tag = 'expired' if expiry_date < current_date else 'valid'
                self.tree.insert("", tk.END, values=(entry["FirstName"], entry["LastName"], entry["Sex"], entry["Age"],
                                                     entry["ContactNumber"], entry["SubscriptionDuration"],
                                                     entry["ExpiryDate"]), tags=(tag,))
            update_window.destroy()

        save_button = tk.Button(update_window, text="Save", command=save_updates)
        save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def delete_entry(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected")
            return

        # Get the index of the selected item and the corresponding user
        item_index = self.tree.index(selected_item)
        selected_user = data_list[item_index]

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?")
        if confirm:
            try:
                #Delete entry from database
                collection.delete_one({
                     "FirstName": selected_user["FirstName"],
                     "LastName": selected_user["LastName"],
                     "ContactNumber": selected_user["ContactNumber"]
                 })
                # Remove entry from the treeview and the data list
                self.tree.delete(selected_item)
                data_list.pop(item_index)
                messagebox.showinfo("Deleted", "Entry deleted successfully")
            except Exception as e:
               messagebox.showerror("Error", f"An error occurred while deleting the entry from the database: {str(e)}")

    def generate_image(self):
        # Remove the entry from the treeview and the data list
        selected_item = self.tree.selection()
        if not selected_item:
             messagebox.showerror("Error", "No item selected")
             return

        # Get the index of the selected item
        item_index = self.tree.index(selected_item)

        try:
            # Get the details of the selected user
            selected_user = data_list[item_index]
            full_name = f"{selected_user['FirstName']} {selected_user['LastName']}"
            expiry_date = selected_user['ExpiryDate']

            image_path = "C:/Users/Lenovo/OneDrive/Desktop/Tk_Project/img/template.png"
            image = Image.open(image_path)

            # Draw the text on the image
            d = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 40)

            text_pos = (210, 350)
            text2_pos = (210, 425)
            text_color = "black"

            d.text(text_pos, full_name, fill=text_color, font=font)
            d.text(text2_pos, expiry_date, fill=text_color, font=font)

            image.save(f"{full_name}_img.png")

            messagebox.showinfo("Success", f"Image generated and saved as '{full_name}_img.png'")
    
        except IndexError:
            messagebox.showerror("Error", "Invalid selection or no data available")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

     #Frame for exit
    def Exit_page(self):
        Exit_frame = tk.Frame(self.main_frame)

        lb = tk.Label(Exit_frame, text="Are you sure you want to logout?", font=("times new roman", 30))
        lb.pack()

        logout_button = tk.Button(Exit_frame, text="Logout", padx=20, pady=20, command=self.root.destroy)
        logout_button.pack()

        Exit_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    obj = TestWindow(root)
    root.mainloop()
