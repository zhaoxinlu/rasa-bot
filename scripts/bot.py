# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter

nlu_model_path = '../models/default/model_20171213-172714'
policy_path = '../models/policy/current'

def run_tickets_bot(server_forever=True):
    agent = Agent.load(policy_path, RasaNLUInterpreter(nlu_model_path))

    if server_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent

if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    run_tickets_bot(server_forever=True)