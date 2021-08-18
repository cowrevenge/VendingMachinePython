from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time

window_main = Tk()
window_main.geometry("1024x768")
window_main.title("Welcome To The Soda Shop")
window_main.configure(bg='#ffca05')


def update_total_user_yen():
    global current_yen
    disp_tf.delete(0, END)
    disp_tf.insert(0, current_yen)


def disable_buttons():
    button1['state'] = "disabled"
    button_yen_thousand['state'] = "disabled"
    button_yen_five_hundred['state'] = "disabled"
    button_yen_one_hundred['state'] = "disabled"
    button_yen_five_ten['state'] = "disabled"
    button_yen_one_ten['state'] = "disabled"


def enable_buttons():
    button1['state'] = "active"
    button_yen_thousand['state'] = "active"
    button_yen_five_hundred['state'] = "active"
    button_yen_one_hundred['state'] = "active"
    button_yen_five_ten['state'] = "active"
    button_yen_one_ten['state'] = "active"


def get_drink():
    global current_yen

    if current_yen >= soda_price:
        disable_buttons()
        text_area.configure(state='normal')
        text_area.insert(END, "- " + str(soda_price) + " Yen Dispensing soda. Please Wait" + '\n')
        text_area.configure(state='disabled')
        current_yen = current_yen - soda_price
        update_total_user_yen()
        animatedloop = 1
        while animatedloop < 96:
            animated_soda = "expandedsoda/" + str(animatedloop) + ".png"
            stg_img = PhotoImage(file=animated_soda)
            vending_static.configure(image=stg_img)
            vending_static.image = stg_img
            time.sleep(.04)
            window_main.update_idletasks()
            animatedloop = animatedloop + 1
        enable_buttons()
        text_area.configure(state='normal')
        text_area.insert(END, "You may take your soda. Your change is " + str(current_yen) + " Yen" + '\n')
        text_area.configure(state='disabled')
        current_yen = 0
        update_total_user_yen()

    elif current_yen <= soda_price:
        text_area.configure(state='normal')
        text_area.insert(END, "Insufficient funds. Please add more Yen" + '\n')
        text_area.configure(state='disabled')





def add_1000():
    global current_yen
    if current_yen >= 100:
        text_area.configure(state='normal')
        text_area.insert(END, "Current Yen balance too high. Bill rejected" + '\n')
        text_area.configure(state='disabled')

    elif current_yen <= 100:
        current_yen = current_yen + 1000
        update_total_user_yen()
        text_area.configure(state='normal')
        text_area.insert(END, "Bill accepted. Your new balance is " + str(current_yen) + "Yen" + '\n')
        text_area.configure(state='disabled')


def add_500():
    global current_yen
    current_yen = current_yen + 500
    update_total_user_yen()
    text_area.configure(state='normal')
    text_area.insert(END, "500 Yen accepted. Your new balance is " + str(current_yen) + "Yen" + '\n')
    text_area.configure(state='disabled')


def add_100():
    global current_yen
    current_yen = current_yen + 100
    update_total_user_yen()
    text_area.configure(state='normal')
    text_area.insert(END, "100 Yen accepted. Your new balance is " + str(current_yen) + "Yen" + '\n')
    text_area.configure(state='disabled')


def add_50():
    global current_yen
    current_yen = current_yen + 50
    update_total_user_yen()
    text_area.configure(state='normal')
    text_area.insert(END, "50 Yen accepted. Your new balance is " + str(current_yen) + "Yen" + '\n')
    text_area.configure(state='disabled')


def add_10():
    global current_yen
    current_yen = current_yen + 10
    update_total_user_yen()
    text_area.configure(state='normal')
    text_area.insert(END, "10 Yen accepted. Your new balance is " + str(current_yen) + "Yen" + '\n')
    text_area.configure(state='disabled')


current_yen = 0
soda_price = 100

label1 = Label(window_main, text="Welcome To The Soda Shop", font=("arial", 16, "bold"))
label1.pack()

button1 = Button(window_main, text="Get Drink", font=("arial", 16, "bold"), command=get_drink)
button1.pack()

yen_thousand = PhotoImage(file="yen/yen_bill.png")
button_yen_thousand = Button(window_main, image=yen_thousand, command=add_1000, height=140, width=280)
button_yen_thousand.place(x=25, y=100)

yen_five_hundred = PhotoImage(file="yen/500.png")
button_yen_five_hundred = Button(window_main, image=yen_five_hundred, command=add_500, height=140, width=140)
button_yen_five_hundred.place(x=335, y=100)

yen_one_hundred = PhotoImage(file="yen/100.png")
button_yen_one_hundred = Button(window_main, image=yen_one_hundred, command=add_100, height=140, width=140)
button_yen_one_hundred.place(x=505, y=100)

yen_five_ten = PhotoImage(file="yen/50.png")
button_yen_five_ten = Button(window_main, image=yen_five_ten, command=add_50, height=140, width=140)
button_yen_five_ten.place(x=675, y=100)

yen_one_ten = PhotoImage(file="yen/10.png")
button_yen_one_ten = Button(window_main, image=yen_one_ten, command=add_10, height=140, width=140)
button_yen_one_ten.place(x=845, y=100)

stg_img = PhotoImage(file="expandedsoda/1.png")
vending_static = Label(window_main, image=stg_img, highlightthickness=0, bd=0)
vending_static.place(x=25, y=250)

disp_tf = Entry(window_main, width=5, font=('Arial', 14))
disp_tf.pack()
disp_tf.insert(0, current_yen)

text_area = ScrolledText(window_main, width=50, height=31, state='disabled')
text_area.configure(font='TkFixedFont')
text_area.place(x=475, y=251)

text_area.configure(state='normal')
text_area.insert(END, "The current price of soda is " + str(soda_price) + '\n')
text_area.configure(state='disabled')

window_main.mainloop()
