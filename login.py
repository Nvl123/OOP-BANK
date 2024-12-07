import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3


from daftar import user
import menu_cetak
import menu_penarikan
import menu_setor
import menu_dompetDigital
import menu_tokenListrik

class LogIn(user):
	
	def __init__ (self,namaAkun, sandi):
		self.sandi = sandi
		self.namaAkun = namaAkun
		
	def cek_login(self):
		# Mengecek username dan password
		query_cek = '''SELECT * FROM data_mhs WHERE username=? AND pasword=?'''
		tuple_cek = (self.namaAkun, self.sandi)
		con = sqlite3.connect('data.db')
		cursor = con.cursor()
		cursor.execute(query_cek, tuple_cek)
		result = cursor.fetchone()
		con.close()

		return result is not None

def login (root):
	coba_masuk = LogIn( usern.get(), passwd.get())
	
	if coba_masuk.cek_login():
			
		global cur_user
		cur_user = (usern.get())

		jendela_masuk.destroy()
	
		global jendela_utama

		jendela_utama = tk.Toplevel(root)
		jendela_utama.title("Utama")
		jendela_utama.geometry("360x367")
		jendela_utama.configure(bg = "#1a1919")
		
		h1 = tk.Label(jendela_utama, text = "Menu Utama", font=("Roboto", 20),bg = "#1a1919", fg = "#ffffff")
		h1.grid(row = 0, column = 0, columnspan = 2,  sticky = "news", padx = 100, pady = 10)
		
		frame1 = tk.LabelFrame(jendela_utama, text = "Informasi Pribadi")
		frame1.configure(bg = "#DB1C12", fg = "#ffffff")
		frame1.grid(row = 1, column= 0, columnspan = 2, sticky = "news", padx = 20, pady = 10)
		
		pribadi = tk.Button(frame1, text = "Cetak Informasi Pribadi",font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000" , width = 42, command = lambda : menu_cetak.cetak_informasi(root,  cur_user))
		pribadi.grid(row = 0, column= 0,columnspan = 2, sticky = "ew", padx = 10, pady = 10)
		
		frame2 = tk.LabelFrame(jendela_utama, text = "Transaksi")
		frame2.configure(bg = "#DB1C12", fg = "#ffffff")
		frame2.grid(row = 2, column= 0, columnspan = 2, sticky = "news", padx = 20, pady = 10)
		
		tarikTunai = tk.Button(frame2, text="Tarik Tunai", font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000", width = 19, command = lambda : menu_penarikan.tarik_tunai(cur_user, root) )
		tarikTunai.grid (row=0, column=0, sticky= "news", padx = 10, pady = 10 )
		
		setorTunai = tk.Button(frame2, text="Setor Tunai", font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000", width = 19,  command = lambda : menu_setor.setor_tunai(cur_user, root) )
		setorTunai.grid (row=0, column=1, sticky= "news", padx = 10, pady = 10 )

		frame3 = tk.LabelFrame(jendela_utama, text = "Dompet Digital & Listrik")
		frame3.configure(bg = "#DB1C12", fg = "#ffffff")
		frame3.grid(row = 3, column= 0, columnspan = 2, sticky = "news", padx = 20, pady = 10)
		
		saldoDigital = tk.Button(frame3, text="Top Up", font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000", width = 19, command = lambda : menu_dompetDigital.dompetDigital(root, cur_user) )
		saldoDigital.grid (row=0, column=0, sticky= "news", padx = 10, pady = 10 )
		
		tokenListrik = tk.Button(frame3, text="Isi Token", font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000", width = 19, command = lambda : menu_tokenListrik.tok_lik(root, cur_user) )
		tokenListrik.grid (row=0, column=1, sticky= "news", padx = 10, pady = 10 )

		keluar = tk.Button (jendela_utama, text = "Keluar", font = ("Roboto", 10), bg = "#f8bd05", fg ="#000000", command = logout )
		keluar.grid (row = 4, column = 0, columnspan = 2, sticky = "news", padx = 20, pady = 10)

			
	else :
		tk.messagebox.showerror(title = "Gagal", message = "Password atau Username yang dimasukkan salah") 

def logout ():
	
	jendela_utama.destroy()


def masuks (root):
	
	global jendela_masuk
	
	jendela_masuk = tk.Toplevel(root)
	jendela_masuk.title("Masuk")
	jendela_masuk.geometry("400x240")
	jendela_masuk.configure(bg = "#1a1919")	
		
	global passwd
	global usern
		
	passwd = tk.StringVar()
	usern = tk.StringVar()
	
	h1 = tk.Label(jendela_masuk, text ="Masuk", font = ("Roboto", 20), bg = "#1a1919", fg = "#ffffff")
	h1.grid(row = 0, column= 0, columnspan = 2, padx =155, pady = 5, sticky = "news")
	
	h2 = tk.Label(jendela_masuk, text ="Silahkan masukkan username dan password yang telah dibuat", font = ("Roboto",8), bg = "#1a1919", fg = "#ffffff")
	h2.grid(row = 1, column = 0, columnspan = 2, padx = 15, pady = 15, sticky = "news")
	
	user1= tk.Label(jendela_masuk, text="Username", font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff" )
	user1.grid(row=2, column=0, padx=5, pady = 5, sticky= "news")
	
	userMasuk = tk.Entry(jendela_masuk,  font = ("Roboto", 10), textvariable = usern )
	userMasuk.grid(row=2, column=1, padx=5, pady = 10, sticky= "news")
	
	pas1= tk.Label(jendela_masuk, text="Passwoard", font = ("Roboto", 10), bg = "#1a1919", fg = "#ffffff" )
	pas1.grid(row=3, column=0, padx=5, pady = 10, sticky= "news")
	
	pasMasuk = tk.Entry(jendela_masuk,  font = ("Roboto", 10), show="*" , textvariable = passwd)
	pasMasuk.grid(row=3, column=1, padx=5, pady = 10, sticky= "news")
	
	tombolMasuk = tk.Button(jendela_masuk, text="Masuk", bg = "#f8bd05", fg ="#000000", font = ("Roboto", 8), command=lambda: login(root) )
	tombolMasuk.grid(row=4,column=0, columnspan=2, padx=5, pady = 10, sticky= "news")
	