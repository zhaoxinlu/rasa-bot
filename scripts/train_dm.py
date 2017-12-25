# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from scripts.tickets_policy import TicketsPolicy

def train_tickets_order_dm():
    training_data_file = "../tickets/data/stories.md"
    domain_path = '../tickets/domain.yml'
    model_path = '../models/policy/current'

    agent = Agent(domain=domain_path, policies=[MemoizationPolicy(), TicketsPolicy()])

    agent.train(training_data_file,
                max_history=3,
                epochs=100,
                batch_size=50,
                augmentation_factor=50,
                validation_split=0.2)

    agent.persist(model_path)

if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    train_tickets_order_dm()