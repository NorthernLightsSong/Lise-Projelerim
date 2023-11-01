import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_weather_data():
    # Chrome sürücüsünü başlatın
    driver = webdriver.Chrome()

    # Bir web sitesini açın
    driver.get('https://weather.com/tr-TR/weather/today/l/ed8836414f5ddcfdb604ac41ff6553f00f99a51650314a46fba455f970d7c74d')

    # Sayfanın tamamen yüklenmesini bekleyin
    time.sleep(5)

    # Belirli bir sınıfa ait tüm öğeleri bulun
    elements = driver.find_elements(By.CLASS_NAME, 'Card--content--1GQMr')

    # Verileri bir metin dizesine toplayın
    data = "\n".join(element.text for element in elements)

    # Tarayıcıyı kapatın
    driver.quit()

    # Verileri Tkinter penceresinde görüntüle
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, data)

# Tkinter penceresi oluşturun
root = tk.Tk()
root.title("Hava Durumu Verileri")

# Veri görüntüleme alanını oluşturun
result_text = tk.Text(root, wrap=tk.WORD, width=90, height=40)
result_text.pack()

# "Verileri Al" düğmesini oluşturun
get_data_button = tk.Button(root, text="Verileri Al", command=get_weather_data)
get_data_button.pack()

# Ana döngüyü başlatın
root.mainloop()
