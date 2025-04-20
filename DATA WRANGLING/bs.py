import requests
from bs4 import BeautifulSoup


html_file = open('index.html', 'r')
content = html_file.read()
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

titles = soup.find_all('h5', class_="card-title")

# print(titles)

anchor = soup.find_all('a', class_="btn btn-primary")
prices = []

for i in anchor:
    prices.append(i.text.split()[-1])

# print(anchor)

for i in anchor:
    print(i.get('class'))


for i in range(len(titles)):
    print(f"Course : {titles[i].text} , Price : {prices[i]}")





















# import requests
# from bs4 import BeautifulSoup
# url = 'http://quotes.toscrape.com/'

# html_file = open('home.html', 'r')
# content = html_file.read()
# soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# response = requests.get(url)
# # print(response.text)
# soup_content = BeautifulSoup(response.text, 'lxml')
# # print(soup_content.prettify())

# span = soup_content.find("div").find('span', class_="tag-item")

# print(span)


# div, h2, h3, p, span, footer, body, head, a , img


# print(response.raise_for_status())
# data = response.json()
# print(data)

# df = pd.DataFrame(data['slip'], index=[0])
# df.to_csv("weather_data.csv", index=False)
# # userId = data[0]['userId']

# # userInfo = requests.get('https://jsonplaceholder.typicode.com/users', params= {'id' : userId}).json()

# # print(userInfo)


# # url = "https://api.openweathermap.org/data/2.5/weather"
# # # Make GET request
# # response = requests.get(url, params=params)
# # # Convert response to JSON
# # data = response.json()
# # # Print fetched data
# # print(data)

# # https://api.openweathermap.org/data/2.5/weather?q='dhaka'
