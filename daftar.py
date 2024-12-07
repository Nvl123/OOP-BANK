import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class user():
	def __init__(self,username, gender, umur, passw) :
		self.username = username
		self.gender = gender
		self.umur = umur
		self.passw = passw
	
	
	def daftar (self):
		#input data
		saldo = 0
		query_insert = '''INSERT INTO data_mhs VALUES (?,?,?,?,?)'''
		tuple_insert = (self.username, self.gender, self.umur, self.passw, saldo)
		con = sqlite3.connect('data.db')
		cursor = con.cursor()
		con.execute(query_insert, tuple_insert)
		con.commit()
		con.close()
		tk.messagebox.showinfo(title = "Sukses", message = "Akun berhasil dibuat")


	def cek_nama_sama(self):
        	# Mengecek username
	        query_cek = '''SELECT * FROM data_mhs WHERE username=?'''
        	tuple_cek = (self.username,)
	        con = sqlite3.connect('data.db')
        	cursor = con.cursor()
	        cursor.execute(query_cek, tuple_cek)
        	result = cursor.fetchone()
	        con.close()

	        return result is not None

def daftar (root):
	
		
	global nama1
	global jenis
	global usia1
	global pasw	
	
	nama1 = tk.StringVar()
	jenis = tk.StringVar()
	usia1 = tk.StringVar()
	pasw =  tk.StringVar()

	jendela_daftar = tk.Toplevel(root)
	jendela_daftar.title("Pendaftaran")
	jendela_daftar.geometry("350x320")
	jendela_daftar.configure(bg = "#1a1919")
	
	h1 = tk.Label(jendela_daftar, text ="Pendaftaran", font = ("Roboto", 16), bg = "#1a1919", fg = "#ffffff")
	h1.grid(row = 0, column= 0, columnspan = 2, padx =110, pady = 20, sticky = "news")
	
	nm_dpn = tk.Label(jendela_daftar, text = "Username", font = ("Roboto", 12),bg = "#1a1919", fg = "#ffffff")
	nm_dpn.grid(row = 1, column = 0, sticky = "news", padx = 5, pady = 10)
	
	entry_user = tk.Entry(jendela_daftar,  font = ("Roboto"), textvariable = nama1)
	entry_user.grid(row = 1, column = 1, sticky= "news", padx = 5, pady = 10)
	
	txgender = tk.Label(jendela_daftar, text = "Gender", font = ("Roboto", 12),bg = "#1a1919", fg = "#ffffff")
	gender = ttk.Combobox(jendela_daftar, value= ["Laki-Laki", "Wanita"], font = ("Roboto", 12), textvariable = jenis)
	
	gender.set("Pilih Gender")
	gender ["state"] = 'readonly'
	
	txgender.grid(row = 2, column = 0, padx = 5, pady = 10, sticky = "news") 
	gender.grid(row = 2, column = 1, padx = 5, pady = 10,  sticky = "news")
	
	usia_txt = tk.Label(jendela_daftar, text = "Umur",  font = ("Roboto", 12),bg = "#1a1919", fg = "#ffffff")
	usia = tk.Spinbox(jendela_daftar, from_ = "1", to = "infinity", font = ("Roboto", 12), textvariable = usia1)
	
	usia_txt.grid(row = 3, column = 0, padx = 5, pady = 10, sticky = "news" )
	usia.grid(row = 3, column = 1,  padx = 5, pady = 10, sticky = "news")
	
	pas1 = tk.Label(jendela_daftar, text = "Password",   font = ("Roboto", 12),bg = "#1a1919", fg = "#ffffff")
	pas2 = tk.Entry(jendela_daftar, show = "*",   font = ("Roboto", 12), textvariable = pasw)
	
	pas1.grid(row = 4, column = 0, sticky= "news", padx = 5, pady = 10)
	pas2.grid(row = 4, column = 1, sticky= "news", padx = 5, pady = 10)
	
	tombol_daftar = tk.Button(jendela_daftar, text = "Daftar",  font = ("Roboto", 12), bg = "#f8bd05", fg ="#000000", command = regis)
	tombol_daftar.grid(row = 5, column = 0, columnspan = 2, sticky = "news", padx = 5, pady = 10)


def regis():
	nama_user = nama1.get()
	gender = jenis.get()
	umur = usia1.get()
	pasword = pasw.get()
	
	# Memastikan semua kolom terisi
	if nama_user == "" or gender == "Pilih Gender" or umur == "" or pasword == "":
		
		tk.messagebox.showwarning(title="Perhatian", message="Semua kolom wajib terisi")
	else:
		registrasi = user(nama1.get(), jenis.get(), usia1.get(), pasw.get())
		
		if registrasi.cek_nama_sama():
			tk.messagebox.showwarning(title="Perhatian", message="Akun sudah ada")
		else:
			registrasi.daftar()