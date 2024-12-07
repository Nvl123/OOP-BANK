import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3




def keluar_info ():
	jendela_informasi.destroy()


def cetak_informasi(root, cur_user):
	# Mencetak informasi pribadi
	query = '''SELECT gender, umur, pasword, saldo FROM data_mhs WHERE username=?'''
	data = (cur_user,)
	
	con = sqlite3.connect('data.db')
	cursor = con.cursor()
	cursor.execute(query, data)
	result = cursor.fetchone()
		
	gender, umur, pasword, saldo = result
	
	global jendela_informasi
	
	jendela_informasi = tk.Toplevel(root)
	jendela_informasi.title("Info")
	jendela_informasi.geometry("195x177")
	jendela_informasi.configure(bg = "#1a1919")
	
	informasi = tk.Text(jendela_informasi, font = ("Roboto", 13), width = 17, height = 5)
	informasi.grid(row = 0, column = 0, sticky = "news", pady = 10, padx = 10)
	
	informasi.insert(tk.END, "Nama \t: "+ cur_user + "\n")
	informasi.insert(tk.END, "Gender \t: " + gender + "\n")
	informasi.insert(tk.END, "Umur \t: " + str (umur) + " Th \n")
	informasi.insert(tk.END, "Sandi \t: " + str(pasword) + "\n")
	informasi.insert(tk.END, "Saldo \t: {} ".format(saldo))
	
	kelar = tk.Button(jendela_informasi, text = "Keluar",font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000", command = keluar_info)
	kelar.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

