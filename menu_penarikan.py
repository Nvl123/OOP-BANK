import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3



class TarikSaldo () :

	def __init__ (self, name, nominal):
		
		self.name = name
		self.nominal = nominal

	def tarik_saldo(self, name, nominal):
		# Mendapatkan nilai integer dari IntVar
		saldo_baru_value = self.nominal
	
		# Mengecek saldo saat ini
		query_saldo_sekarang = '''SELECT saldo FROM data_mhs WHERE username=?'''
		tuple_saldo_sekarang = (self.name,)
	
		con = sqlite3.connect('data.db')
		cursor = con.cursor()
		cursor.execute(query_saldo_sekarang, tuple_saldo_sekarang)
		saldo_sekarang = cursor.fetchone()[0]
	
		# Memastikan saldo tidak menjadi negatif
		if saldo_baru.get() == 0 :
			tk.messagebox.showwarning(title="Perhatian", message="Silahkan masukkan nominal dengan benar")

		elif saldo_baru_value > saldo_sekarang:
			tk.messagebox.showwarning(title="Perhatian", message="Saldo tidak mencukupi untuk penarikan ini")

		

		else:
			# Menambahkan nilai baru ke saldo saat ini
			saldo_baru_total = saldo_sekarang - saldo_baru_value
		
			# Melakukan update saldo
			query_update_saldo = '''UPDATE data_mhs SET saldo=? WHERE username=?'''
			tuple_update_saldo = (saldo_baru_total, self.name)
			cursor.execute(query_update_saldo, tuple_update_saldo)
	
			con.commit()
			con.close()
			tk.messagebox.showinfo(title="Sukses", message="Penarikan Berhasil")
def Tariks (cur_user):
	
	tarik = TarikSaldo(cur_user, saldo_baru.get())
	tarik.tarik_saldo(cur_user, saldo_baru.get())


def selesai ():
	jendela_tarik.destroy()

def tarik_tunai(cur_user, root):
	
	global jendela_tarik

	jendela_tarik = tk.Toplevel(root)
	jendela_tarik.title("Penarikan")
	jendela_tarik.geometry("190x165")
	jendela_tarik.configure(bg = "#1a1919")
	
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
	
	current_saldo = tk.Label(jendela_tarik, text ="Saldo saat ini : Rp. {} ".format(saldo), font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	current_saldo.grid(row = 0, column = 0, columnspan = 2,  sticky = "news",pady = 10, padx = 10 )
	
	nominal_saldo = tk.Label (jendela_tarik, text = "Silahkan Masukkan Nominal ", font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	nominal_saldo.grid(row = 1, column = 0,columnspan = 2, sticky = "news",pady = 10, padx = 10)
	
	saldo_keluar = tk.Entry (jendela_tarik, font = ("Roboto", 10), textvariable = saldo_baru )
	saldo_keluar.grid(row = 2, column = 0, columnspan = 2, sticky = "news", padx = 10, pady = 10)
	
	tombol_tarik = tk.Button(jendela_tarik, text = "Tarik",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = lambda : Tariks(cur_user))
	tombol_tarik.grid(row = 3, column = 0, sticky = "news", pady = 10, padx = 10)
	
	tombol_keluar = tk.Button(jendela_tarik, text = "Keluar",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = selesai )
	tombol_keluar.grid(row = 3, column = 1, sticky = "news", pady = 10, padx = 10)