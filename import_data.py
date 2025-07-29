'''Useful function to import data in the main app 
and create a list of objects of OperaIncompiuta class.
Separated file from "tools" in order to avoid circular imports'''

import os
import json
from tools import str_to_date, str_to_num, clear_str, shorten_str
from operaincompiuta import OperaIncompiuta
import requests

def dataset_import(url:str, relative_path:str) -> list :
    '''creates a json file at "relative_path" with data got from url;
    returns data as a list of dictionaries'''
    if not os.path.exists(relative_path):
        response = requests.get(url)
        data = response.json()
        with open(relative_path,"w", encoding="utf-8") as json_file:
            json.dump(data,json_file)
    with open(relative_path, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def create_opere_incompiute_list(url:str,relative_path:str):
    '''creates a list of objects of OperaIncompiuta class'''
    # save data as a json file and import it as a list of dictionaries
    data = dataset_import(url, relative_path)
    opere_incompiute_list = []
    # fill the list
    for item in data:
        try:
            opere_incompiute_list.append(OperaIncompiuta(
                pubblicata_da=clear_str(item['pubblicata_da']),
                anno_rif=str_to_num(item['anno_rif'],integ=True),
                tipologia_opera_incompiuta=clear_str(item['tipologia_opera_incompiuta'])[0],
                perc_avanzamento=str_to_num(item['perc_avanzamento'],perc=True),
                mancanza_fondi=clear_str(item['mancanza_fondi']),
                cause_tecniche=clear_str(item['cause_tecniche']),
                importo_complessivo=str_to_num(
                    item['importo_complessivo_lavori_aggiornato_ultimo_sal'],",","."),
                natura_opera=clear_str(item['natura_opera']),
                tipologia_cup=shorten_str(clear_str(item['tipologia_cup']),
                                          chars_each_word=5, char_limit=20),
                ambito_oggettivo=clear_str(item['ambito_oggettivo']),
                categoria=clear_str(item['categoria']),
                comunitaria=clear_str(item['comunitaria']),
                data_assegnazione_cup=str_to_date(item['data_assegnazione_cup']),
                lat=str_to_num(item['lat'],"."), lon=str_to_num(item['lon'],"."),
                indirizzo=clear_str(item['indirizzo'])))
        except TypeError as ex:
            print(f"error: {ex}")
        except ValueError as ex:
            print(f"error: {ex}")
    return opere_incompiute_list
