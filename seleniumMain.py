from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

def search_result():
    bot = webdriver.Edge()
    bot.get('https://google.com')
    time.sleep(10)
    window.quit()
    result = bot.find_element_by_name('q')
    result.clear()
    result.send_keys(entry1.get())
    result.send_keys(Keys.RETURN)

def facebook():
    bot = webdriver.Edge()
    bot.get('https://www.facebook.com')

window = Tk()
window.geometry("450x200")
search = Label(window, text="what are you thinking .....", font='times 15')
search.place(x=10, y=10)
entry1 = Entry(window)
entry1.place(x=250, y=10)

b1 = Button(window, text="search", command=search_result, width=12, bg='gray')
b1.place(x=150, y=50)

b2 = Button(window, text="Facebook",
            command=facebook, width=12, bg='gray')
b2.place(x=150, y=100)

window.mainloop()
