import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class NambahSaldo ():

	def __init__ (self, name, nominal):
		
		self.name = name
		self.nominal = nominal


	def update_saldo(self, name, nominal):
		
		# Mendapatkan nilai integer dari IntVar
		saldo_baru_value = saldo_baru.get()
	
		# Mengecek saldo saat ini
		query_saldo_sekarang = '''SELECT saldo FROM data_mhs WHERE username=?'''
		tuple_saldo_sekarang = (self.name,)
	
		con = sqlite3.connect('data.db')
		cursor = con.cursor()
		cursor.execute(query_saldo_sekarang, tuple_saldo_sekarang)
		saldo_sekarang = cursor.fetchone()[0]
	
		# Menambahkan nilai baru ke saldo saat ini
		saldo_baru_total = saldo_sekarang + saldo_baru_value
	
		# Melakukan update saldo
		query_update_saldo = '''UPDATE data_mhs SET saldo=? WHERE username=?'''
		tuple_update_saldo = (saldo_baru_total, self.name)
		cursor.execute(query_update_saldo, tuple_update_saldo)
	
		con.commit()
		con.close()	
		tk.messagebox.showinfo(title="Sukses", message="Saldo Anda Bertambah")

def tambahSaldo(cur_user) :
	
	if saldo_baru.get() == 0 :
		tk.messagebox.showwarning(title="Perhatian", message="Silahkan masukkan nominal dengan benar")
	else :
	
		tambah = NambahSaldo(cur_user, saldo_baru.get())
		tambah.update_saldo(cur_user, saldo_baru.get())

def kelardah():
		
	jendela_setor.destroy()

def setor_tunai(cur_user, root):
	
	global jendela_setor
	
	
	salmasuk = tk.IntVar()
	
	jendela_setor = tk.Toplevel(root)
	jendela_setor.title("Setoran")
	jendela_setor.geometry("190x165")
	jendela_setor.configure(bg = "#1a1919")
	
	# Mencetak informasi pribadi
	query = '''SELECT saldo FROM data_mhs WHERE username=?'''
	data = (cur_user,)
	
	con = sqlite3.connect('data.db')
	cursor = con.cursor()
	cursor.execute(query, data)
	result = cursor.fetchone()
		
	saldo = result
	
	global saldo_baru
	saldo_baru = tk.IntVar()
	
	current_saldo = tk.Label(jendela_setor, text ="Saldo saat ini : Rp. {} ".format(saldo), font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	current_saldo.grid(row = 0, column = 0, columnspan = 2,  sticky = "news",pady = 10, padx = 10 )
	
	nominal_saldo = tk.Label (jendela_setor, text = "Silahkan Masukkan Nominal ", font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	nominal_saldo.grid(row = 1, column = 0,columnspan = 2, sticky = "news",pady = 10, padx = 10)
	
	saldo_masuk = tk.Entry (jendela_setor, font = ("Roboto", 10), textvariable = saldo_baru )
	saldo_masuk.grid(row = 2, column = 0, columnspan = 2, sticky = "news", padx = 10, pady = 10)
	
	tombol_masuk = tk.Button(jendela_setor, text = "Masukkan",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = lambda : tambahSaldo(cur_user))
	tombol_masuk.grid(row = 3, column = 0, sticky = "news", pady = 10, padx = 10)
	
	tombol_keluar = tk.Button(jendela_setor, text = "Keluar",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = kelardah )
	tombol_keluar.grid(row = 3, column = 1, sticky = "news", pady = 10, padx = 10)

