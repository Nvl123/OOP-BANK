import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3


import daftar
import login


root = tk.Tk()
root.title("Bank Bersama")
root.geometry("310x310")
root.configure(bg = "#1a1919")

img = Image.open("icon.png")
resizeimg = img.resize((100,100))
img = ImageTk.PhotoImage(resizeimg)
gambar = tk.Label(root, image = img, bg = "#1a1919")

gambar.grid(row = 0, column = 0, padx = 10, pady = 40, columnspan = 2, sticky = "news")


judul = tk.Label (root, text = "Selamat Datang di Bank Bersama", font = ("Roboto", 12), bg = "#1a1919", fg = "#ffffff")
judul.grid(row = 1, column = 0, padx = 10, pady = 5, columnspan = 2, sticky = "news")

judul2 = tk.Label (root, text = "Silahkan Login (*atau daftar jika belum mempunyai akun)", font = ("Roboto", 8), bg = "#1a1919", fg = "#ffffff")
judul2.grid(row = 2, column = 0, padx = 10, pady = 5, columnspan = 2, sticky = "news")

mendaftar = tk.Button(root, text = "Mendaftar", bg = "#f8bd05", fg ="#000000", command=lambda: daftar.daftar(root))
masuk = tk.Button(root, text = "Masuk", bg = "#f8bd05", fg ="#000000", command=lambda: login.masuks(root))
mendaftar.grid(row = 3, column =  0, sticky = "news", padx = 10, pady = 10 )
masuk.grid(row = 3, column = 1, sticky = "news", padx = 10, pady = 10)


root.mainloop()

