import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'

response = requests.get(url)
print(response.text)
# soup_content = BeautifulSoup(response.text, 'lxml')
# print(soup_content.text)

# span = soup_content.find("footer").find('p', class_="copyright")
# span = soup_content.find('p', class_="container")

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

# # https://kash_meranaseb_itna_mehrbanhota-kizarapehle_mulaqat_hojati_unse.monzim.com/api/dsc/boss/events/registrations?eventId=0ecf2a61-db53-482

# # url = "https://api.openweathermap.org/data/2.5/weather"
# # params = {"q": "Singapore", "appid": "f2cf9344dc6b01a2a3723979a6bd1f73"}
# # # Make GET request
# # response = requests.get(url, params=params)
# # # Convert response to JSON
# # data = response.json()
# # # Print fetched data
# # print(data)

# # https://api.openweathermap.org/data/2.5/weather?q='dhaka'
