from typing import Text, List, Any, Dict
import webbrowser
from rasa_sdk import Action,Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import ridl_api
import requests
import pdb
import c

class CreateFormAction(Action):
    def __init__(self):
        self.finish_string = "Ok everything is setup.  Now you'll need to login and open your Google Sheets" 
        self.last_string = "You can list your spreadsheet by typing  -- list spreadsheet -- in the chat window" 
    def name(self) -> Text:
        return "action_login_account"

    def run(self,dispatcher,tracker,domain):
        google_oauth_token = None
        creds = c.credentials()
        slots = tracker.slots
        username = slots['username'] 
        ridl_api.create_account(username) 
        dispatcher.utter_message(text=self.finish_string + "\n" + self.last_string +"\n")
        return []

class Help(Action):
    def name(self) -> Text:
        return "action_help_topic"
    def run(self,dispatcher,tracker,domain):
        return []

class ListFileAction(Action):
    def name(self) -> Text:
        return "action_list_files"
    def run(self,dispatcher,tracker,domain):
        slots = tracker.slots

        return [] 

