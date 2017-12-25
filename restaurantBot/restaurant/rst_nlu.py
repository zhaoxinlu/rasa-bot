# -*- coding: utf-8 -*-
"""
Function: train NLU model
{
	"pipeline": ["nlp_mitie","tokenizer_mitie", "ner_mitie", "ner_synonyms", "intent_featurizer_mitie", "intent_classifier_sklearn"],
	"mitie_file": "./data/total_word_feature_extractor.dat",
	"path": "./models",
	"data": "./data/jarvis_testdata_5.json",
	"emulate": "luis"
}
"""
import os

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

Main_path = os.path.dirname(__file__)

def train_restaurant_nlu():
    train_data = load_data('../restaurantData/franken_data.json')
    trainer = Trainer(RasaNLUConfig("../restaurantData/config_mitie.json"))
    trainer.train(train_data)
    model_dir = trainer.persist('../rst_models/rst_nlu/current')
    return model_dir

def predict_restaurant_nlu(model_dir):
    from rasa_nlu.model import Metadata, Interpreter
    interpreter = Interpreter.load(model_dir, RasaNLUConfig("../restaurantData/config_nlu.json"))
    intent_entities = interpreter.parse('thanks, good bye')
    return intent_entities

if __name__ == '__main__':
    #model_dir = train_restaurant_nlu()
    # ../rst_models/rst_nlu/current/default/model_20171222-104704
    #print model_dir
    intent_entities = predict_restaurant_nlu('../rst_models/rst_nlu/current/default/model_20171222-104704')
    print intent_entities
    # print Main_path