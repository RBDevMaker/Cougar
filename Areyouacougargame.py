import tkinter as tk
from tkinter import messagebox

def categorize_age():
    try:
        age = entry.get().strip()
        if not age.isdigit():
            raise ValueError("Input must be a valid number.")
        age = int(age)
        
        if 0 <= age <= 17:
            category = "You are a Kitten!"
        elif 18 <= age <= 21:
            category = "You are a Wildcat!"
        elif 22 <= age <= 29:
            category = "You are a Lynx!"
        elif 30 <= age <= 39:
            category = "You are a Puma!"
        elif 40 <= age <= 49:
            category = "You are a Cougar!"
        elif 50 <= age <= 59:
            category = "You are a Jaguar!"
        elif 60 <= age <= 68:
            category = "You are a Panther!"
        elif age == 69:
            category = "You are a Pussycat!"
        elif 70 <= age <= 79:
            category = "You are a Cheetah!"
        elif 80 <= age <= 89:
            category = "You are a Leopard!"
        elif 90 <= age <= 99:
            category = "You are a Tiger!"
        elif age == 100:
            category = "You are a Lion!"
        else:
            category = "Sorry, I can only categorize ages from 0 to 100."
        
        messagebox.showinfo("Feline Type", category)

        # Ask the user if they want to enter another age
        reset_response = messagebox.askquestion("Continue", "Would you like to enter another age?")
        
        if reset_response == 'no':
            messagebox.showinfo("Goodbye", "Stay safe out there, you Wild Cat!")
            root.quit()  # Close the application
        else:
            entry.delete(0, tk.END)  # Clear the entry field for new input

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Feline Age Classifier")
root.geometry("300x200")

# Label, Entry, and Button in a more organized layout
tk.Label(root, text="Enter your age:", font=('Arial', 12)).pack(pady=10)
entry = tk.Entry(root, font=('Arial', 12))
entry.pack(pady=5)

tk.Button(root, text="Find My Feline!", font=('Arial', 12), command=categorize_age).pack(pady=15)

root.mainloop()
