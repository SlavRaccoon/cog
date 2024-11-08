#Web scraping postupak
import requests
from bs4 import BeautifulSoup
URL = "https://www.timeanddate.com/weather/"
LOCATION_PATH = 'croatia/zadar'
full_url = URL + LOCATION_PATH
response = requests.get(full_url)
soup = BeautifulSoup(response.content,'html.parser')
win = "Wind: "
print("Zadatak - rudarenje podataka - Nikola Čusek - " + LOCATION_PATH)
try:
    # Izvlacenje temperature
    temperature = soup.find("div", {"class":"h2"}).text.strip()
    print(f"Temperature: {temperature}")
except:
    print("Ne mogu izvuci tu informaciju.")
try:
    # Izvlacenje brzine vjetra - Profesore, kod nije radio zato što, koliko barem ja vidim klasa "wind-value" ne postoji, pa sam napravio bandaid fix
    wind_info = soup.find("div", {"id":"qlook"}).findAll("p")
    wind_info.pop(0)
    type(wind_info[0])
    for i in wind_info[0]:
        c=0
        for g in i:
            if c>5:
                wind_speed = g
                break
            if g != win[c]:
                break
            else:
                c = c + 1
    print("Brzina vjertra: " + str(wind_speed) + "km/h")
    #if wind_info:
    #    wind_speed = wind_info[0].text
    #    print(f"Brzina vjetra:{wind_speed}")
except:
    print("Ne mogu izvuci tu informaciju.")
try:
    # Izvlacenje opisa vremena
    weather_description = soup.find("div", {"id":"qlook"}).find("p").text
    print(f"Opis vremena: {weather_description.strip()}")
except:
    print("Ne mogu izvuci tu informaciju.")