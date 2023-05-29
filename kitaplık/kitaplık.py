from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

def ekle():
    baglanti = sqlite3.connect("kutuphane.db")
    im = baglanti.cursor()
    im.execute("""INSERT INTO kayit ('Kitap_Adi','Yazar_Adi','Yayinevi')
VALUES (?,?,?)""",(girisKitapAdi.get(),girisYazarAdi.get(),girisYayineviAdi.get()))
    baglanti.commit()
    girisKitapAdi.delete(0,END)
    girisYazarAdi.delete(0,END)
    girisYayineviAdi.delete(0,END)
    messagebox.showinfo("Bilgi","Kayıt Girildi")
def bul():
    try:
        pencere2 = Toplevel()

        tablo = ttk.Treeview(pencere2)

        tablo["columns"] = ("A","B","C")
        tablo.column("#0",width = 100)
        tablo.column("A", width=200)
        tablo.column("B", width=200)
        tablo.column("C", width =200)

        tablo.heading("#0", text = "Kayıt No")
        tablo.heading("A", text = "Kitap Adı")
        tablo.heading("B", text = "Yazarı")
        tablo.heading("C", text= "Yayınevi")

        baglanti = sqlite3.connect("kutuphane.db")
        im = baglanti.cursor()

        im.execute(" SELECT * FROM kayit WHERE Kitap_Adi = ? OR Yazar_Adi = ? OR Yayinevi = ? ",
                   (girisKitapAdi.get(),girisYazarAdi.get(),girisYayinevi.get(),girisKayit.get()))
        veriler = im.fetchall()
        print(veriler)
        for i in range(0,len(veriler)):
            tablo.insert('',"end", text=veriler[i][0], values=(veriler[i][1],
                                                               veriler[i][2],
                                                               veriler[i][3]))
            tablo.pack()

    except:
        pencere2.destroy()
        messagebox.showinfo("Kayıt Bulunamadı", " Doğru girdiğinizden Emin Olunuz")

        
    girisKitapAdi.delete(0,END)
    girisYazarAdi.delete(0,END)
    girisYayineviAdi.delete(0,END)


pencere = Tk()
pencere.title("Kitap Kayıt Formu")
pencere.geometry("500x200+500+250")

etiketKitapAdi = Label(text = "Kitap Adı")
etiketKitapAdi.place(x = 60,y = 50)

girisKitapAdi = Entry(width = 50)
girisKitapAdi.place(x = 160,y =50)

etiketYazarAdi = Label(text = "Yazar Adı")
etiketYazarAdi.place(x = 60,y = 80)

girisYazarAdi = Entry(width = 50)
girisYazarAdi.place(x = 160,y =80)

etiketYayineviAdi = Label(text = "Yayınevi Adı")
etiketYayineviAdi.place(x = 60,y = 110)

girisYayineviAdi = Entry(width = 50)
girisYayineviAdi.place(x = 160,y = 110)

btnEkle = Button(text = "Ekle" , command = ekle)
btnEkle.place(x = 200,y= 140)

btnBul = Button(text = "Bul", command = bul)
btnBul.place(x = 250,y = 140)

btnCikis = Button(text = "Çıkış", command = pencere.destroy)
btnCikis.place(x =300,y = 140)

mainloop()


