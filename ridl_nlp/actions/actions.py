from typing import Text, List, Any, Dict
import webbrowser
from rasa_sdk import Action,Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import requests
import pdb


class CreateLogin(Action):
    def name(self) -> Text:
        return "action_create_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
            pdb.set_trace()
            try: 
               account_type = tracker.slots['login_account'] 
               account_name = tracker.slots['login_name'] 
               account_password = tracker.slots['login_password'] 
            except:
                dispatcher.utter_message("you didn't fill in the info correctly")
            ## create an ridl account   


return []
