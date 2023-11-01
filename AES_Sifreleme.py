import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def sifrele():
    anahtar = anahtar_giris.get()
    metin = metin_giris.get()
    aes_anahtar = pad(anahtar.encode('utf-8'), AES.block_size)
    sifreleyici = AES.new(aes_anahtar, AES.MODE_CBC)
    sifreli_metin = sifreleyici.encrypt(pad(metin.encode('utf-8'), AES.block_size))
    sonuc.delete(0, 'end')
    sonuc.insert(0, base64.b64encode(sifreleyici.iv + sifreli_metin).decode('utf-8'))

def coz():
    anahtar = anahtar_giris.get()
    sifreli_metin = base64.b64decode(metin_giris.get())
    aes_anahtar = pad(anahtar.encode('utf-8'), AES.block_size)
    iv = sifreli_metin[:AES.block_size]
    sifreli_metin = sifreli_metin[AES.block_size:]
    cozucu = AES.new(aes_anahtar, AES.MODE_CBC, iv=iv)
    cozulmus_metin = unpad(cozucu.decrypt(sifreli_metin), AES.block_size).decode('utf-8')
    sonuc.delete(0, 'end')
    sonuc.insert(0, cozulmus_metin)

pencere = tk.Tk()
simge_yolu = "C:/Users/north/OneDrive/Masaüstü/İcon/sevimli.ico"
pencere.iconbitmap(simge_yolu)
pencere.configure(bg='black')
pencere.geometry('300x150')
pencere.title("AES Şifreleme")

anahtar_giris = tk.Entry(pencere)
anahtar_giris.pack(pady=3)

metin_giris = tk.Entry(pencere)
metin_giris.pack(pady=3)

sonuc = tk.Entry(pencere)
sonuc.pack(pady=3)

sifrele_buton = tk.Button(pencere, text="Şifrele",  bg='red', command=sifrele)
sifrele_buton.pack(pady=3)

coz_buton = tk.Button(pencere, text="Çöz",  bg='green', command=coz)
coz_buton.pack(pady=3)

pencere.mainloop()