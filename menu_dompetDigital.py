import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3



from abc import ABC, abstractmethod

class dmptDigital(ABC):
	
	@abstractmethod
	def TopUp (self, nama, nominal):
		pass

class Dompet (dmptDigital):

	def __init__ (self, nama, nominal):
	
		self.nama = nama
		self.nominal = nominal

	def TopUp (self, nama, nominal):
		
		saldo_baru_value = self.nominal

		query_saldo_sekarang = '''SELECT saldo FROM data_mhs WHERE username=?'''
		tuple_saldo_sekarang = (self.nama,)
	
		con = sqlite3.connect('data.db')
		cursor = con.cursor()
		cursor.execute(query_saldo_sekarang, tuple_saldo_sekarang)
		saldo_sekarang = cursor.fetchone()[0]
	
		# Memastikan saldo tidak menjadi negatif
		if saldo_baru_value > saldo_sekarang:
			tk.messagebox.showwarning(title="Perhatian", message="Saldo tidak mencukupi untuk transaksi ini")

		else:
			# Mengurangi saldo
			saldo_baru_total = saldo_sekarang - saldo_baru_value
		
			# Melakukan update saldo
			query_update_saldo = '''UPDATE data_mhs SET saldo=? WHERE username=?'''
			tuple_update_saldo = (saldo_baru_total, self.nama)
			cursor.execute(query_update_saldo, tuple_update_saldo)

			con.commit()
			con.close()
			tk.messagebox.showinfo(title="Sukses", message="Top Up Berhasil")



def tambah_up (cur_user):

	
	if nama_DD.get() == "Pilih Dompet Digital" or noTujuan.get() == 0 or nominalUp.get() == 0  :
		
		tk.messagebox.showwarning(title="Perhatian", message="Semua Kolom Wajib terisi")

	else:
	
		saku = Dompet(use,nominalUp.get())
		saku.TopUp(use,nominalUp.get())
	


def keluar_jendelaDD ():
	
	jendela_dd.destroy()

def dompetDigital(root, cur_user):
	
	global use
	use= cur_user
	
	
	global jendela_dd
	
	jendela_dd = tk.Toplevel(root)
	jendela_dd.title("Dompet Digital")
	jendela_dd.geometry("290x230")
	jendela_dd.configure(bg = "#1a1919")
	
	global nominalUp
	global noTujuan
	global nama_DD

	nominalUp = tk.IntVar()
	noTujuan =  tk.StringVar()
	nama_DD = tk.StringVar()
	
	
	h1 = tk.Label(jendela_dd, text = "Dompet Digital", font = ("Roboto", 15), bg = "#1a1919", fg = "#ffffff")
	h1.grid(row = 0, column = 0, columnspan = 2, sticky = "news", pady = 10, padx = 20 )
	
	dompet = ttk.Combobox(jendela_dd,font = ("Roboto", 10), value = ["Gopay", "LinkAja", "OVO", "ShopeePay", "DANA", "i.Saku"], textvariable = nama_DD)
	dompet.grid(row = 1, column = 0, columnspan = 2, sticky = "news", pady = 10, padx = 20)
	
	dompet.set("Pilih Dompet Digital")
	dompet ["state"] = 'readonly'
	
	nomor = tk.Label(jendela_dd, text = "No. Tujuan",font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	nomor.grid(row = 2, column = 0, sticky =  "news", pady = 10, padx = 20 )
	
	no_tujuan = tk.Entry(jendela_dd,font = ("Roboto", 10), textvariable = noTujuan )
	no_tujuan.grid(row = 2, column = 1 , sticky =  "news", pady = 10, padx = 20)
	
	nominal = tk.Label(jendela_dd, text = "Nominal",font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	nominal.grid(row = 3, column = 0, sticky =  "news", pady = 10, padx = 20 )
	
	nominal_entry = tk.Entry(jendela_dd,font = ("Roboto", 10), textvariable = nominalUp )
	nominal_entry.grid(row = 3, column = 1 , sticky =  "news", pady = 10, padx = 20)
	
	tombol_topUp = tk.Button(jendela_dd, text = "Top Up",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = lambda : tambah_up(cur_user))
	tombol_topUp.grid(row = 4, column = 0, sticky = "news", pady = 10, padx = 20 )
	
	tombol_keluar = tk.Button(jendela_dd, text = "Keluar",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = keluar_jendelaDD)
	tombol_keluar.grid(row = 4, column = 1, sticky = "news", pady = 10, padx = 20 )	
