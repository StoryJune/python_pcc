#Jiahao Cai & Jason Li
#Decmeber 10, 2025
#Pizza Project
#Making a pizza application


#requirements:

"""
Must add a picture to the GUI.
Must add at least one label, textfield, button, one set of checkboxes, and one set of radio buttons. 
Create a click() function that is invoked when the user submits their order.
In the click() function, implement the logic to calculate the total cost based on the user's selections and display a receipt on the GUI.
You do not have to do any data validation. You should assume that the user will always enter valid inputs.
You have to work with a partner of your choice. If you do not have a partner, let me know immediately.
"""

import tkinter as tk
from PIL import Image, ImageTk

#root window
root = tk.Tk()
root.configure(bg="white")
root.title("Pizza Order")

#500 pixel by 600 pixels
root.geometry("800x450")

#initializing values for tkinter to be stored and processed
#Since we are going to have buttons for size, crust and toppings
size_var = tk.StringVar(value = None)
crust_var = tk.StringVar(value = None)
toppings_vars = {
    "Pepperoni": tk.BooleanVar(),
    "Sausage": tk.BooleanVar(),
    "Mushrooms": tk.BooleanVar(),
    "Onions": tk.BooleanVar(),
}                        

#load pizza image
img = Image.open("pizza.png")
img = img.resize((360, 100))
pizza_image = ImageTk.PhotoImage(img)
tk.Label(root, image=pizza_image, bg="white").place(x=55, y=75)

#Select size label
tk.Label(root, text="Select Size:").place(x=200, y=50)

#Small
tk.Radiobutton(root, text="Small", variable=size_var, value="Small").place(x=50, y=180)
tk.Label(root, text="Price: $10.99", font=("Arial", 10)).place(x=50, y=200)


#Medium
tk.Radiobutton(root, text="Medium", variable=size_var, value="Medium").place(x=200, y=180)
tk.Label(root, text="Price: $12.99", font=("Arial", 10)).place(x=200, y=200)


#Large
tk.Radiobutton(root, text="Large", variable=size_var, value="Large").place(x=350, y=180)
tk.Label(root, text="Price: $14.99", font=("Arial", 10)).place(x=350, y=200)

#crust
tk.Label(root, text="Select Crust:", bg="white").place(x=56, y=240)

tk.Radiobutton(root, text="Hand-tossed", variable=crust_var, value="Hand-tossed").place(x=56, y=270)
tk.Radiobutton(root, text="Deep-dish", variable=crust_var, value="Deep-dish").place(x=56, y=295)
tk.Radiobutton(root, text="Thin-crust", variable=crust_var, value="Thin-crust").place(x=56, y=320)

#toppings
tk.Label(root, text="Select Toppings: \n(each extra topping $1.25)", bg="white").place(x=190, y=240)

tk.Checkbutton(root, text="Pepperoni", variable=toppings_vars["Pepperoni"]).place(x=190, y=290)
tk.Checkbutton(root, text="Sausage", variable=toppings_vars["Sausage"]).place(x=190, y=315)
tk.Checkbutton(root, text="Mushrooms", variable=toppings_vars["Mushrooms"]).place(x=190, y=340)
tk.Checkbutton(root, text="Onions", variable=toppings_vars["Onions"]).place(x=190, y=365)

#Name getter 
name_label = tk.Label(root, text="Enter your name:")
name_label.place(x=525, y=25)

entry = tk.Entry(root, width=15)
entry.place(x=520, y=50)

#submission
receipt_label = tk.Label(root, text="", justify="left", bg="white", font=("Arial", 10))
receipt_label.place(x=520, y=150)

def click():
    size_prices = {"Small": 10.99, "Medium": 12.99, "Large": 14.99}
    topping_prices = 1.25
    
    #getting user input from ui
    size = size_var.get()
    crust = crust_var.get()
    total = size_prices.get(size, 0)
    
    #store selected toppings in list
    selected_toppings = ["Cheese"]
    extra_topping_count = 0
    
    #loop through
    for topping, var in toppings_vars.items():
        if var.get():
            selected_toppings.append(topping)
            extra_topping_count += 1
    total += extra_topping_count * topping_prices
    # calculate tax
    tax_rate = 0.0875   # 8.75%
    tax_amount = total * tax_rate
    grand_total = total + tax_amount
    
    # Build receipt text
    receipt = f"Receipt for {entry.get()}:\n"
    receipt += f"Size: {size} (${size_prices.get(size,0):.2f})\n"
    receipt += f"Crust: {crust}\n"
    receipt += "Toppings:\n"
    for t in selected_toppings:
        receipt += f" - {t}\n"
    receipt += f"\nSubtotal: ${total:.2f}\n"
    receipt += f"Tax (8.75%): ${tax_amount:.2f}\n"
    receipt += f"Your final cost is: ${grand_total:.2f}"
    
    receipt_label.config(text=receipt)

#submission button
tk.Button(root, text="Submit Order", command=click).place(x=525, y=100)

#MUST HAVE: need this to print image
root.mainloop()
