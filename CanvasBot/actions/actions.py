
from bs4 import BeautifulSoup
import pandas as pd
import quandl
import pymongo
import requests
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Mongo Code
client = MongoClient("mongodb+srv://adityasahu:Bond007*@cluster0.z9zia26.mongodb.net/test")
# database
db = client["chatbot"]
# collection
conn_info= db["info"]
conn_grade = db["grades_db"]

#Scrapping Code
browser = webdriver.Chrome("C:/Users/adity/Desktop/SJSU work/AI DS/project/dummy/actions/chromedriver")
url = 'https://sjsu.instructure.com/courses/1487741/'
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


count=0
name=""

class ActionUser(Action):

    def name(self) -> Text:
        return "action_user"

    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global count
        global name
        user_info = db["user"]
        name=tracker.latest_message['text']
        ch = 'a'
        if count != -1:
            x = chr(ord(ch) + count)
            d = {x: name}
            count += 1
        user_info.insert(d)
        dispatcher.utter_template("utter_start",tracker,temp=name)

        return []

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data['main']
        temp=int(format_add['temp']-273)
        dispatcher.utter_template("utter_temp",tracker,temp=temp)

        return []

class ActionGrade(Action):

    def name(self) -> Text:
        return "action_grade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        newl = 'https://sjsu.instructure.com/courses/1487741/grades'
        browser.get(newl)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        table = soup.find_all('table')[0]
        df1 = pd.read_html(str(table))
        df = pd.DataFrame(df1[0])
        df = df.drop(['Status', 'Details', 'Submission Progress Status', 'Due' , 'Score'], axis=1)
        df2 = pd.DataFrame(df[16:])
        print("sdfdssdfdsf")
        df.reset_index(inplace=True)
        data_dict = df2.to_dict("records")
        conn_grade.drop()
        conn_grade.insert_many(data_dict)
        df_grade = pd.DataFrame(list(conn_grade.find()))
        df_grade = df_grade.drop(['_id'], axis=1)
        print(df_grade.to_string)
        msg = df_grade.to_string()
        dispatcher.utter_message(text=msg)
        # dispatcher.utter_message(text="Hello World!")
        return []

class ActionInstructor(Action):

    def name(self) -> Text:
        return "action_instructor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info_d = conn_info.find_one()
        msg=""
        for i in info_d:
            if i == 'Instructor':
                msg = info_d[i]
        dispatcher.utter_message(text=msg)
        #dispatcher.utter_message(text="Hello World!")
        return []

class ActionInstructorMail(Action):

    def name(self) -> Text:
        return "action_instructor_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info_d = conn_info.find_one()
        msg=""
        for i in info_d:
            if i == 'Instructor_mail':
                msg = info_d[i]
        dispatcher.utter_message(text=msg)
        return []

class ActionISA(Action):

    def name(self) -> Text:
        return "action_isa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info_d = conn_info.find_one()
        msg=""
        for i in info_d:
            if i == 'ISAs':
                msg = info_d[i]
        dispatcher.utter_message(text=msg)
        return []

class ActionIsaMail(Action):

    def name(self) -> Text:
        return "action_isa_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info_d = conn_info.find_one()
        msg=""
        for i in info_d:
            if i == 'ISA1':
                msg = msg + info_d[i] + " & "
            if i == 'ISA2':
                msg = msg + info_d[i]
        dispatcher.utter_message(text=msg)
        return []

class ActionLocation(Action):

    def name(self) -> Text:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info_d = conn_info.find_one()
        msg=""
        for i in info_d:
            if i == 'Location':
                msg = info_d[i]
        dispatcher.utter_message(text=msg)
        return []

class ActionAnn(Action):

    def name(self) -> Text:
        return "action_announcement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ann_info = db["ann"]
        ann_d = ann_info.find_one()
        dispatcher.utter_message(text=ann_d['1'])
        dispatcher.utter_message(text=ann_d['2'])
        dispatcher.utter_message(text=ann_d['3'])

        return []
