from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class WeatherInfo(Action):

    def name(self) -> Text:
        return "weather_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.latest_message['entities'][0]['value']
        response = "In " + location + ", the temperature is ...° and the humidity is about ..."
        dispatcher.utter_message(text=response)
        return []
