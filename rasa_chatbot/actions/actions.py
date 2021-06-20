from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":""}

headers = {
    'x-rapidapi-key': "974553fd41mshe12b4d7bb94bf87p165921jsn71b64ff42aaa",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

class WeatherInfo(Action):

    def name(self) -> Text:
        return "weather_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            location = tracker.latest_message['entities'][0]['value']
            querystring["q"] = location

            response = requests.request("GET", url, headers=headers, params=querystring)
            json_data = response.json()
            weather = json_data["weather"][0]["main"]
            temp = int(json_data["main"]["temp"] - 273)
            wind_speed = json_data["wind"]["speed"]

            response = f"In {location}, the weather is dominated by {weather}, the temperature is {temp}°C while the wind speed is about {wind_speed}."
        except:
            response = "I can't retrieve the weather in the specified location."
        finally:
            dispatcher.utter_message(text=response)

        return []
