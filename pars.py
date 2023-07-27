import requests

url = 'https://nemera.net'  # Замените на URL нужного вам сайта
response = requests.get(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

# Проверка статуса ответа (200 означает успешный запрос)
if response.status_code == 200:
    html_content = response.content
else:
    print('Ошибка при получении страницы:', response.status_code)
    exit()

# Сохранение всего содержимого сайта в локальный файл
with open('whole_website.html', 'wb') as file:
    file.write(html_content)

print('Содержимое сайта успешно сохранено в файл "whole_website.html"')
