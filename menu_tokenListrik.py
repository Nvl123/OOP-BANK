import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3



import random
from zope.interface import Interface, implementer

class TokenListrik(Interface):

	def IsiToken(self, nama, nominal):

		pass

@implementer (TokenListrik)
class Listrik():

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
			tk.messagebox.showinfo(title="Sukses", message="Transaksi Berhasil")	


def TokenPLN (root, cur_user):
	
	
	if int(noPLN.get()) == 0  or bayarPLN.get() == 0 or noPLN.get() == "" :
		
		tk.messagebox.showwarning(title="Perhatian", message="Semua Kolom Wajib terisi")
	

	else :
	
		PLN = Listrik(cur_user,bayarPLN.get())
		PLN.TopUp(cur_user,bayarPLN.get())
		
		noToken = [str(random.randint(10000, 99999)) for _ in range (5)]
		token = '-'.join(noToken)
		
		out.insert(tk.END, str(token))

def keluarpln ():
	
	jendela_tl.destroy()


def tok_lik (root, cur_user):

	global jendela_tl
	global noPLN
	global bayarPLN
	
	global out
	
	jendela_tl = tk.Toplevel(root)
	jendela_tl.title("Token Listrik")
	jendela_tl.geometry("290x260")
	jendela_tl.configure(bg = "#1a1919")
	
	
	noPLN = tk.IntVar()
	bayarPLN = tk.IntVar()
	
	h1 = tk.Label(jendela_tl, text = "Token Listrik", font = ("Roboto", 15), bg = "#1a1919", fg = "#ffffff")
	h1.grid(row = 0, column = 0, columnspan = 2, sticky = "news", pady = 10, padx = 20 )

	nomor = tk.Label(jendela_tl, text = "No. Meter",font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	nomor.grid(row = 1, column = 0, sticky =  "news", pady = 10, padx = 20 )
	
	no_tujuan = tk.Entry(jendela_tl,font = ("Roboto", 10), textvariable = noPLN )
	no_tujuan.grid(row = 1, column = 1 , sticky =  "news", pady = 10, padx = 20)
	
	nominal = tk.Label(jendela_tl, text = "Nominal",font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff")
	nominal.grid(row = 2, column = 0, sticky =  "news", pady = 10, padx = 20 )
	
	nominal_entry = tk.Entry(jendela_tl,font = ("Roboto", 10), textvariable = bayarPLN)
	nominal_entry.grid(row = 2, column = 1 , sticky =  "news", pady = 10, padx = 20)
	

	frame1 = tk.LabelFrame(jendela_tl, text= "Nomor Token")
	frame1.grid(row = 3, column = 0, columnspan = 2, sticky = "news", pady = 10, padx = 20)
	frame1.configure(bg = "#DB1C12", fg = "#ffffff")	

	out = tk.Text(frame1, font = ("Roboto", 10), width = 30, height =1)
	out.grid(row = 0, column = 0, columnspan = 2, sticky = "news", pady = 10, padx = 20)
	
	
	tombol_token = tk.Button(jendela_tl, text = "Isi Token",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = lambda : TokenPLN(root, cur_user))
	tombol_token.grid(row = 4, column = 0, sticky = "news", pady = 10, padx = 20 )
	
	tombol_keluar = tk.Button(jendela_tl, text = "Keluar",font = ("Roboto", 10),  bg = "#f8bd05", fg ="#000000", command = keluarpln)
	tombol_keluar.grid(row = 4, column = 1, sticky = "news", pady = 10, padx = 20 )	
