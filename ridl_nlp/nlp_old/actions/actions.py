# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import pdb
import logging
from typing import Any, Text, Dict, List
#
from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
logger = logging.getLogger(__name__)


class ActionListFile(Action):
    def name(self):
        return "action_listfiles"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="ActionListFiles")
        return []


#class ActionLogin(Action):
#    def name(self):
#        return "action_login"
#
#    def run(self, dispatcher, tracker, domain):
#        dispatcher.utter_message(text="ActionLogin")
#        return []


class ActionLoad(Action):
    def name(self):
        return "action_load"

    def run(self, dispatcher, tracker, domain):
        pdb.set_trace()
        sender_id = tracker.sender_id
        entities = tracker.latest['entities'][0]
        values = tracker.latest['entities'][0]
        return []


class ActionList(Action):
    def name(self):
        return "action_list"

    def run(self, dispatcher, tracker, domain):
        pdb.set_trace()
        sender_id = tracker.sender_id
        latest = tracker.latest_message
        entities = latest['entities'][0]
        value = entities['value']
        entity = entities['entity']



class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value,
        dispatcher,
        tracker,
        domain
    ):
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}
