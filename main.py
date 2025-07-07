import tkinter as tk
import messagebox
import re
root = tk.Tk()
root.minsize(300,300)
FONT = ("arial",12,"normal")



Romen_numerals = {
    "I":1,"II":2,"III":3,"IV":4,"V":5,
    "VI":6,"VII":7,"VIII":8,"IX":9,"X":10,
    "XX":20,"XXX":30,"XL":40,"L":50,"LX":60,
    "LXX":70,"LXXX":80,"XC":90,"C":100,"CC":200,
    "CCC":300,"CD":400,"D":500,"DC":600,"DCC":700,
    "DCCC":800,"CM":900,"M":1000,"MM":2000,"MMM":3000,
    "_IV":4000,"_V":5000
}

#Numara tespit kısmı

def is_valid_roman(s):
    pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.match(pattern, s) is not None

sonuc_label = None
hazır_numara = None
def Romen_numeral_calculater():
    global sonuc_label,hazır_numara
    try:
        hazır_sayı = []
        if len(tk_entry.get()) == 0:
            messagebox.showinfo(title="BOŞ DEĞER",message="Bir romen rakamı girin")
        toplanacak_sayılar = []
        if tk_entry.get() in Romen_numerals:
            hazır_sayı.append(Romen_numerals[tk_entry.get()])
        i = 0
        digit_to_convert = tk_entry.get().replace(" "," ").upper()
        if not is_valid_roman(digit_to_convert):
            messagebox.showinfo(title="YANLIŞ YAZIM", message="Geçersiz veya yanlış yazılmış Romen rakamı girdiniz.")
            return

        while i < len(digit_to_convert):
            if "VV" in digit_to_convert or "LLL" in digit_to_convert or "DDD" in digit_to_convert:
                messagebox.showinfo(title="Yanlış harf dizimi",message="Yanlş harf dizimi girdiniz (VV)")
                return
            if "IIII" in digit_to_convert or "XXXX" in digit_to_convert or "CCCC" in digit_to_convert or "MMMM" in digit_to_convert:
                messagebox.showinfo(title="YANLIŞ YAZIM",message="Yanlış bir yazı girdiniz(IIII)")
                return
            if (digit_to_convert[i:i + 2] == "IV" or
                digit_to_convert[i:i + 2] == "IX" or
                digit_to_convert[i:i + 2] == "XL" or
                digit_to_convert[i:i + 2] == "XC" or
                digit_to_convert[i:i + 2] == "CD" or
                digit_to_convert[i:i + 2] == "CM") and Romen_numerals[digit_to_convert[i]] < Romen_numerals[digit_to_convert[i + 1]]:
                toplanacak_sayılar.append(Romen_numerals[digit_to_convert[i:i + 2]])
                i += 2
            elif digit_to_convert[i:i + 2] not in ["IV", "IX", "XL", "XC", "CD", "CM"] and Romen_numerals[digit_to_convert[i]] >= Romen_numerals[digit_to_convert[i + 1]] and digit_to_convert[i:i+2] in Romen_numerals:
                toplanacak_sayılar.append(Romen_numerals[digit_to_convert[i:i+2]])
                i +=2
            if digit_to_convert[i:i+2] in Romen_numerals:
                toplanacak_sayılar.append(Romen_numerals[digit_to_convert[i:i+2]])
                i+=2
            else:
                if i+1 < len(digit_to_convert):
                    if digit_to_convert[i] < digit_to_convert[i+1] and digit_to_convert[i] == "I" or digit_to_convert[i] == "X" or digit_to_convert[i] == "C":
                        if digit_to_convert[i:i+2] in Romen_numerals:
                            toplanacak_sayılar.append(Romen_numerals[digit_to_convert[i:i+1]])
                            i+=1
                        else:
                            if i+1 < len(digit_to_convert):
                                if digit_to_convert[i:i+2] not in Romen_numerals:
                                    toplanacak_sayılar.append(Romen_numerals[digit_to_convert[i]])
                                    i += 1
                    else:
                        toplanacak_sayılar.append(Romen_numerals[digit_to_convert[i]])
                        i+=1

        toplanmıs_sayılar = sum(toplanacak_sayılar)
        if hazır_numara is not None:
            hazır_numara.destroy()
        if tk_entry.get() == Romen_numerals:
            hazır_numara = tk.Label(text=f"SAYINIZ {hazır_sayı}")
            print("bu sondaki if")
            hazır_numara.pack()

        if sonuc_label is not None:
            sonuc_label.destroy()
        if len(tk_entry.get()) != 0:
            sonuc_label = tk.Label(text=f"SAYINIZ {toplanmıs_sayılar}")
            sonuc_label.pack()
        tk_entry.delete(0, tk.END)


    except KeyError as e:
        messagebox.showinfo(title="BOŞLUK",message=f"Boşluk bırakmayınız harf aralarında{e}")

#tkinter kısmı
tk_label = tk.Label(text="bir Romen rakamı girin",font=FONT)
tk_label.pack()

tk_entry = tk.Entry(width=20)
tk_entry.pack()


tk_button = tk.Button(text="Hesapla",font=FONT,command=Romen_numeral_calculater)
tk_button.pack()

root.mainloop()
