# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action


class ActionSearchRestaurants(Action):
    @classmethod
    def name(cls):
        return 'action_search_restaurants'

    @classmethod
    def run(cls, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found")
        return []


class ActionSuggest(Action):
    @classmethod
    def name(cls):
        return 'action_suggest'

    @classmethod
    def run(cls, dispatcher, tracker, domain):
        dispatcher.utter_message("papi's pizza place")
        return []

