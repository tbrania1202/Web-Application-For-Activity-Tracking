import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def scrape_website():
    scraped_text = {}
    try:
        url = "https://pogoda.interia.pl/prognoza-szczegolowa-krakow,cId,4970"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            scraped_text["temperature"] = soup.find(class_="weather-currently-temp-strict").text.strip()
            scraped_text["pressure"] = soup.find(class_="weather-currently-details-item pressure").text.strip()[10:]
            scraped_text["wind"] = soup.find(class_="weather-currently-details-item wind").text.strip()[6:]
            scraped_text["sun_rise"] = soup.find(class_="weather-currently-info-sunrise").text.strip()
            scraped_text["sun_set"] = soup.find(class_="weather-currently-info-sunset").text.strip()
            scraped_text["moon_rise"] = soup.find(class_="weather-currently-info-moonrise").text.strip()
            scraped_text["moon_set"] = soup.find(class_="weather-currently-info-moonset").text.strip()

            weather = soup.find(class_="weather-currently-icon-description").text.strip()
            try:
                translator = Translator()
                translated_weather = translator.translate(weather, src='pl', dest='en')
                scraped_text["weather"] = translated_weather.text
            except Exception as e:
                print(f"Error: {e}")
                scraped_text["weather"] = ""
        else:
            scraped_text["error"] = "Failed to fetch data."
    except Exception as e:
        scraped_text["error"] = f"Error: {e}"

    return scraped_text

