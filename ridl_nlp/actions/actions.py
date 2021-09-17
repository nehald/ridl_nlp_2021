from typing import Text, List, Any, Dict
import webbrowser
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import requests
import pdb
class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_login_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
        login_account = tracker.slots['login_account']
        pdb.set_trace()
        if login_account == 'google':
           try: 
              request_str = "http://localhost:5000/api/login/{0}".format(slot_value)
              pdb.set_trace()
              webbrowser.open("http://sheets.google.com",new=1)
              response = requests.get(request_str) 
              return {"response": "logged in"}
           except:
              pass    
        elif login_account == 'ridl':
           pdb.set_trace()
           login_password = tracker.slots['login_password']
           if 'nehal' in login_password:
             return {"response":"logged in"}
        else:
             return {"response":"logged in"} 
