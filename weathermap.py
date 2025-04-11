import tkinter as tk
from tkinter import messagebox
import requests

# Hava durumu verilerini alacak fonksiyon
def get_weather(city, api_key, language):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang={language}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']

        # Ekranda hava durumu bilgilerini göstermek için
        weather_info_label.config(text=f" Şehir: {city_name}\n Sıcaklık: {temp}°C\n Hissedilen: {feels_like}°C\n Durum: {description.capitalize()}")
    else:
        # Hata durumunda mesaj
        messagebox.showerror("Hata", "❌ Şehir bulunamadı veya API hatası var. Lütfen tekrar deneyin.")

# Tkinter GUI kurulum
root = tk.Tk()
root.title("Hava Durumu Uygulaması")
root.geometry("450x500")
root.config(bg="#2a3d4f")  # Arka plan rengini koyu bir ton yapıyoruz

# Başlık etiketini ekleyelim
title_label = tk.Label(root, text="Hava Durumu Öğren", font=("Helvetica", 18, "bold"), bg="#2a3d4f", fg="#ffffff")
title_label.pack(pady=20)

# Dil seçimi
language_label = tk.Label(root, text="Dil Seçin:", font=("Helvetica", 12), bg="#2a3d4f", fg="#ffffff")
language_label.pack(pady=5)
language_var = tk.StringVar(value="tr")  # Varsayılan dil Türkçe
language_menu = tk.OptionMenu(root, language_var, "tr", "en")  # Türkçe (tr) ve İngilizce (en)
language_menu.config(font=("Helvetica", 12), bg="#00b8d4", fg="#ffffff", relief="flat")
language_menu.pack(pady=5)

# Kullanıcıdan şehir girmesini isteyecek etiket ve giriş alanı
city_label = tk.Label(root, text="Şehri Girin:", font=("Helvetica", 12), bg="#2a3d4f", fg="#ffffff")
city_label.pack(pady=5)
city_entry = tk.Entry(root, font=("Helvetica", 12), width=25, relief="flat", bd=2)
city_entry.pack(pady=5)

# API anahtarınızı buraya ekleyin
api_key = "b56fc5552d5c5d6811550d8ec00dac08"  # Buraya doğru API anahtarınızı ekleyin

# Hava durumu bilgisini alacak fonksiyonla birleştirilen buton
def on_check_weather():
    city = city_entry.get()
    language = language_var.get()  # Seçilen dili alıyoruz
    if city:
        get_weather(city, api_key, language)
    else:
        messagebox.showwarning("Uyarı", "Lütfen geçerli bir şehir adı girin.")

# Şehir sorgulama butonu
check_button = tk.Button(root, text="Hava Durumunu Göster", font=("Helvetica", 12), bg="#00b8d4", fg="#ffffff", relief="flat", command=on_check_weather)
check_button.pack(pady=15)

# Hava durumu bilgisini gösterecek etiket
weather_info_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#2a3d4f", fg="#ffffff", justify="left", anchor="w")
weather_info_label.pack(pady=20)

# Uygulamayı başlat
root.mainloop()
