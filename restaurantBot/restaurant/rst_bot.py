# -*-coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter

nlu_model_path = '../rst_models/rst_nlu/current/default/model_20171222-104704'
policy_model_path = '../rst_models/rst_policy/current'

def run_rst_bot(server_forever=True):
    agent = Agent.load(policy_model_path, RasaNLUInterpreter(nlu_model_path))

    if server_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent

if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    run_rst_bot(server_forever=True)
