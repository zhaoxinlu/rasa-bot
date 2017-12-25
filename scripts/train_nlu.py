# -*- coding: utf-8 -*-
"""
Function: train NLU model
"""
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

def train_nlu():
    train_data = load_data('../tickets/data/nlu.json')
    trainer = Trainer(RasaNLUConfig("../tickets/nlu_model_config.json"))
    trainer.train(train_data)
    model_dir = trainer.persist('../models')
    return model_dir

def predict_nlu(model_dir):
    from rasa_nlu.model import Metadata, Interpreter
    interpreter = Interpreter.load(model_dir, RasaNLUConfig("../tickets/nlu_model_config.json"))
    intent_entities = interpreter.parse(u"我想订16张去往宁波的票")
    return intent_entities

if __name__ == '__main__':
    # model_dir = train_nlu()
    # ../models/default/model_20171213-172714
    # print model_dir
    intent_entities = predict_nlu('../models/default/model_20171213-172714')
    print intent_entities