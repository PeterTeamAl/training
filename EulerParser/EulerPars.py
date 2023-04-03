from bs4 import BeautifulSoup as bs
import requests

url = 'https://euler.jakumo.org/problems/search.html?s=1'

txt = requests.get(url)
print(txt.status_code) #check work

tasks = []

soup = bs(txt.text, 'html.parser')

tasks = soup.findAll('div', class_='problem_content')

num = int(input("Enter task's number."))
if type(num) is int:
    print(f"Task number {num} : /n {(tasks[num-1]).text}")
elif num < 1:
    print("Number must be more or equal 1.")

else:
    print(f"Sorry, {num} is not a number.")