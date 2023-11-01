import tkinter as tk
from selenium import webdriver
from bs4 import BeautifulSoup

def get_gold_data():
    # Selenium ile web sayfasını açın
    url = "https://bigpara.hurriyet.com.tr/altin/"
    driver = webdriver.Chrome()
    driver.get(url)

    # Sayfa yüklendikten sonra BeautifulSoup ile verileri çekin
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    doviz_bar = soup.find(class_='table wide pgAltin')

    # Verileri Text widget'ına yazdırın
    text.delete(1.0, tk.END)
    text.insert(tk.END, doviz_bar.get_text())

    # Tarayıcıyı kapatın
    driver.quit()

# Tkinter arayüzü oluşturun
root = tk.Tk()
root.title("Altın Verileri")

label = tk.Label(root, text="Döviz Bar Altın Verileri")
label.pack()

text = tk.Text(root, height=40, width=90)
text.pack()

# "Verileri Çek" butonunu oluşturun ve arayüze ekleyin
get_data_button = tk.Button(root, text="Verileri Çek", command=get_gold_data)
get_data_button.pack()

# Tkinter arayüzünü çalıştırın
root.mainloop()
