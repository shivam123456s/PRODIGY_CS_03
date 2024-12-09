import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    
    # Initialize criteria counts
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()_+~" for char in password)

    # Count the number of criteria met
    strength_count = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback
    if strength_count == 5:
        feedback = "Strong password!"
    elif strength_count >= 3:
        feedback = "Moderate password. Add more variety to make it stronger."
    else:
        feedback = "Weak password. Try to include a mix of uppercase, lowercase, numbers, and special characters."
    
    messagebox.showinfo("Password Feedback", feedback)

# Create the main window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x200")

# Create widgets
label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Check Password Strength", command=check_password_strength, font=("Arial", 12))
button.pack(pady=10)

# Run the application
root.mainloop()
