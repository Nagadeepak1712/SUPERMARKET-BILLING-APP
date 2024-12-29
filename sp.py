import tkinter as tk
from tkinter import ttk, messagebox
import os

# Correct credentials
correct_username = "user"
correct_password = "pass"

# Function to check credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == correct_username and password == correct_password:
        login_canvas.pack_forget()
        show_billing_page()
    else:
        show_locked_window()

# Function to display locked window
def show_locked_window():
    locked_window = tk.Toplevel(root)
    locked_window.title("Locked")
    locked_window.geometry("300x150")
    tk.Label(locked_window, text="Access Denied!", font=("Arial", 14), bg="red", fg="white").pack(pady=20)
    tk.Button(locked_window, text="Close", command=locked_window.destroy).pack()

# Function to show the billing page
def show_billing_page():
    billing_canvas.pack(fill="both", expand=True)

# Function to open chatbot window
def open_chatbot():
    chatbot_window = tk.Toplevel(root)
    chatbot_window.title("Chatbot Assistant")
    chatbot_window.geometry("400x500")
    tk.Label(chatbot_window, text="Welcome to zsos Supermarket Assistant!", font=("Arial", 14)).pack(pady=10)
    tk.Text(chatbot_window, height=20, width=50).pack(pady=10)
    tk.Entry(chatbot_window, width=40).pack(pady=10)
    tk.Button(chatbot_window, text="Send", command=lambda: messagebox.showinfo("Chatbot", "AI response here")).pack(pady=10)

# Function to exit the application
def exit_app():
    root.destroy()

# Function to print the bill
def print_bill():
    bill_content = bill_text.get("1.0", tk.END)
    customer_satisfaction = "\nThank you for shopping with us!\nCustomer Satisfaction is our priority!\n"
    full_bill = "zsos Supermarket\n" + bill_content + customer_satisfaction
    
    with open("bill.txt", "w") as file:
        file.write(full_bill)

    os.system("notepad.exe bill.txt")
    
    show_offers_popup()

# Function to show offers pop-up
def show_offers_popup():
    offers_window = tk.Toplevel(root)
    offers_window.title("Special Offers")
    offers_window.geometry("300x150")
    tk.Label(offers_window, text="Exclusive Offers!", font=("Arial", 14), bg="green", fg="white").pack(pady=20)
    tk.Label(offers_window, text="Get 10% off on your next purchase!", font=("Arial", 12), fg="black").pack(pady=10)
    tk.Button(offers_window, text="Close", command=offers_window.destroy).pack(pady=10)

# Main Window
root = tk.Tk()
root.title("Supermarket Billing System")
root.attributes('-fullscreen', True)  # Full screen mode
root.configure(bg="black")  # High contrast background

# Login Canvas
login_canvas = tk.Canvas(root, bg="black")
login_canvas.pack(fill="both", expand=True)

tk.Label(login_canvas, text="zsos Supermarket", font=("Arial", 40, "bold"), bg="black", fg="yellow").pack(pady=20)
tk.Label(login_canvas, text="Login", font=("Arial", 20), bg="black", fg="white").pack(pady=20)

username_label = tk.Label(login_canvas, text="Username", bg="black", fg="white")
username_label.pack()
username_entry = tk.Entry(login_canvas)
username_entry.pack()

password_label = tk.Label(login_canvas, text="Password", bg="black", fg="white")
password_label.pack()
password_entry = tk.Entry(login_canvas, show="*")
password_entry.pack()

login_button = tk.Button(login_canvas, text="Login", command=check_login, bg="yellow", fg="black")
login_button.pack(pady=20)

# Assist button
assist_button = tk.Button(login_canvas, text="Assist", command=open_chatbot, bg="yellow", fg="black", font=("Arial", 14, "bold"))
assist_button.pack(pady=20)

# Exit button for login page
exit_login_button = tk.Button(login_canvas, text="Exit", command=exit_app, bg="red", fg="white", font=("Arial", 14, "bold"))
exit_login_button.pack(pady=20)

# Billing Canvas (hidden initially)
billing_canvas = tk.Canvas(root, bg="#2C3E50")

# zsos Supermarket logo on billing page
logo_label = tk.Label(billing_canvas, text="zsos Supermarket", font=("Arial", 40, "bold"), bg="#2C3E50", fg="yellow")
logo_label.pack(pady=20)

# Frame for the product list and selection
frame = tk.Frame(billing_canvas, bg="#34495E")
frame.pack(side=tk.LEFT, padx=20, pady=20)

# Frame for the bill output
bill_frame = tk.Frame(billing_canvas, bg="#1ABC9C")
bill_frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Label for the bill section
bill_label = tk.Label(bill_frame, text="Bill Output", font=("Arial", 16), bg="#1ABC9C", fg="white")
bill_label.pack()

# Text widget to display the bill
bill_text = tk.Text(bill_frame, height=30, width=40, bg="white", fg="black")
bill_text.pack()

# Sample product list
products = {
    "Apple": 1.0,
    "Banana": 0.5,
    "Orange": 0.75,
    "Milk": 1.5,
    "Bread": 2.0,
    # Add more products here
}

# Function to add item to the bill
def add_to_bill(product, price):
    bill_text.insert(tk.END, f"{product} - ${price}\n")
    total = float(total_label.cget("text")) + price
    total_label.config(text=f"{total:.2f}")

# Creating product buttons
for product, price in products.items():
    button = ttk.Button(frame, text=f"{product} - ${price}", command=lambda p=product, pr=price: add_to_bill(p, pr))
    button.pack(pady=5)

# Total label
total_label = tk.Label(bill_frame, text="0.00", font=("Arial", 14), bg="#1ABC9C", fg="white")
total_label.pack(pady=10)

# Print button
print_button = tk.Button(billing_canvas, text="Print", command=print_bill, bg="green", fg="white", font=("Arial", 14, "bold"))
print_button.pack(pady=20)

# Exit button on billing page
exit_button = tk.Button(billing_canvas, text="Exit", command=exit_app, bg="red", fg="white", font=("Arial", 14, "bold"))
exit_button.pack(pady=20)

root.mainloop()
