# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from rst_policy import RestaurantPolicy

nlu_model_path = '../rst_models/rst_nlu/current/default/model_20171222-104704'

def run_rst_bot_online(input_channel, interpreter):
    training_data_file = "../restaurantData/babi_task5_trn_rasa_with_slots.md"
    domain_path = '../restaurant_domain.yml'
    agent = Agent(domain=domain_path, policies=[MemoizationPolicy(), RestaurantPolicy()], interpreter=interpreter)
    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    run_rst_bot_online(ConsoleInputChannel(), RasaNLUInterpreter(nlu_model_path))