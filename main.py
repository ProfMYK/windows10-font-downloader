from customtkinter import *
import os

fonts_dir = "./fonts"

set_appearance_mode("dark")
set_appearance_mode("dark-yellow")

root = CTk()
root.geometry("700x300")

fonts = ["All", *os.listdir(fonts_dir)]


def download_fonts():
    pass


gap = 15
font = ("Roboco", 24)

frame = CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = CTkLabel(master=frame, text="Download Microsoft Windows Fonts", text_font=font)
label.pack(pady=gap)
menu = CTkOptionMenu(master=frame, values=fonts, text_font=font, width=300)
menu.pack(pady=gap)
button = CTkButton(master=frame, text="Download", text_font=font, command=download_fonts, width=300)
button.pack(pady=gap)

root.mainloop()