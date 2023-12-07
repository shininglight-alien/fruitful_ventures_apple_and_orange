import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

# setup
root = tk.Tk()
root.title("Ellaine's Fruitful Ventures")

# set window size to full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# background image
background_image = PhotoImage(file=r"C:\Users\Ellaine\Downloads\Fruitful Ventures.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# fonts
label_font = ("Comic Sans Ms", 20, "bold")
button_font = ("Comic Sans Ms", 20, "bold")
result_font = ("Comic Sans Ms", 24, "bold")

# apple frame
apple_frame = tk.Frame(root,bg="red")
apple_frame.pack(side=tk.LEFT, padx=40, pady=50)

# apple 
tk.Label(apple_frame, text="🍎 Price: 20 pesos per apple", font=label_font, fg="white", bg="red").pack(side=tk.TOP)  # Set text color to red
tk.Label(apple_frame, text="An apple a day, keeps the DOCTOR AWAY!", font=label_font, fg="white", bg="red").pack(side=tk.TOP)  # Set text color to red
tk.Label(apple_frame, text="How many apples will you buy, Ma'am/Sir?", font=label_font, fg="white", bg="red").pack(side=tk.TOP)  # Set text color to red
apple_entry = tk.Entry(apple_frame, font=label_font)
apple_entry.pack(side=tk.TOP)

# orange frame
orange_frame = tk.Frame(root,bg="dark orange")
orange_frame.pack(side=tk.RIGHT, padx=40, pady=50)

# orange
tk.Label(orange_frame, text="🍊 Price: 25 pesos per orange", font=label_font, fg="white", bg="dark orange").pack(side=tk.TOP)  
tk.Label(orange_frame, text="Zest Up Your Day!", font=label_font, fg="white", bg="dark orange").pack(side=tk.TOP)  
tk.Label(orange_frame, text="How many oranges will you buy, Ma'am/Sir?", font=label_font, fg="white", bg="dark orange").pack(side=tk.TOP) 
orange_entry = tk.Entry(orange_frame, font=label_font)
orange_entry.pack(side=tk.TOP)

def calculate_total_amount(apple_quantity, orange_quantity):
    apple_price = 20  # Price of one apple in pesos
    orange_price = 25  # Price of one orange in pesos

    apple_total = apple_quantity * apple_price
    orange_total = orange_quantity * orange_price
    grand_total = apple_total + orange_total

    return apple_total, orange_total, grand_total

def calculate_and_display_total():
    try:
        apple_quantity = int(apple_entry.get())
        orange_quantity = int(orange_entry.get())

        apple_total, orange_total, grand_total = calculate_total_amount(apple_quantity, orange_quantity)

        result_label.config(text=f"Total Price of Apple: {apple_total} pesos\nTotal Price of Orange: {orange_total} pesos\nGrand Total: {grand_total} pesos", fg="black") 
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for apples and oranges.")

# button to calculate total amount
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_and_display_total, font=button_font, fg="red")  # Set text color to red
calculate_button.pack(side=tk.BOTTOM, pady=250)

# result frame
result_frame = tk.Frame(root,bg="red")
result_frame.place(relx=0.5, rely=0.9, anchor="s")

# display result label
result_label = tk.Label(result_frame, text="", font=result_font)
result_label.pack()

# run the GUI
root.mainloop()
