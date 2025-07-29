'''Models the OperaIncompiuta class with
a series of attribuets picked from the most useful
keys of the dataset'''

from datetime import date
from opera import Opera

class OperaIncompiuta(Opera):
    '''models an unfinished public work (Opera Incompiuta)'''
    def __init__(self,pubblicata_da:str, anno_rif:int, tipologia_opera_incompiuta:str,
                 perc_avanzamento:int|float, mancanza_fondi:str,
                 cause_tecniche:str, importo_complessivo:int|float,
                 natura_opera:str, tipologia_cup:str, ambito_oggettivo:str,
                 categoria:str, comunitaria:str,
                 data_assegnazione_cup:date, lat:int|float, lon:int|float, indirizzo:str):
        '''initialisation of instance variables'''
        super().__init__(natura_opera, tipologia_cup, ambito_oggettivo,
                         categoria, comunitaria, data_assegnazione_cup, lat, lon, indirizzo)
        self.set_pubblicata_da(pubblicata_da)
        self.set_anno_rif(anno_rif)
        self.set_tipologia_opera_incompiuta(tipologia_opera_incompiuta)
        self.set_perc_avanzamento(perc_avanzamento)
        self.set_mancanza_fondi(mancanza_fondi)
        self.set_cause_tecniche(cause_tecniche)
        self.set_importo_complessivo(importo_complessivo)
    def set_pubblicata_da(self, pubblicata_da:str):
        '''setter for pubblicata_da'''
        if not isinstance(pubblicata_da, str) and (pubblicata_da is not None):
            raise TypeError(f"Wrong pubblicata_da type: you provided {type(pubblicata_da)}")
        self._pubblicata_da = pubblicata_da
    def set_anno_rif(self, anno_rif:int):
        '''setter for anno_rif'''
        if not isinstance(anno_rif, int) and (anno_rif is not None):
            raise TypeError(f"Wrong anno_rif type: you provided {type(anno_rif)}")
        self._anno_rif = anno_rif
    def set_tipologia_opera_incompiuta(self, tipologia_opera_incompiuta:str):
        '''setter for tipologia_opera_incompiuta'''
        if not isinstance(tipologia_opera_incompiuta, str) \
            and (tipologia_opera_incompiuta is not None):
            raise TypeError(
                f"Wrong tipologia_opera_incompiuta type: "
                f"you provided {type(tipologia_opera_incompiuta)}")
        self._tipologia_opera_incompiuta = tipologia_opera_incompiuta
    def set_perc_avanzamento(self, perc_avanzamento:int|float):
        '''setter for perc_avanzamento'''
        if not isinstance(perc_avanzamento, (int,float)) and (perc_avanzamento is not None):
            raise TypeError(f"Wrong perc_avanzamento type: you provided {type(perc_avanzamento)}")
        self._perc_avanzamento = perc_avanzamento
    def set_mancanza_fondi(self, mancanza_fondi:str):
        '''setter for mancanza_fondi'''
        if not isinstance(mancanza_fondi, str) and (mancanza_fondi is not None):
            raise TypeError(f"Wrong mancanza_fondi type: you provided {type(mancanza_fondi)}")
        self._mancanza_fondi = mancanza_fondi
    def set_cause_tecniche(self, cause_tecniche:str):
        '''setter for cause_tecniche'''
        if not isinstance(cause_tecniche, str) and (cause_tecniche is not None):
            raise TypeError(f"Wrong cause_tecniche type: you provided {type(cause_tecniche)}")
        self._cause_tecniche = cause_tecniche
    def set_importo_complessivo(self, importo_complessivo:int|float):
        '''setter for importo_complessivo'''
        if not isinstance(importo_complessivo, (int,float)) and (importo_complessivo is not None):
            raise TypeError(
                f"Wrong importo_complessivo type: you provided {type(importo_complessivo)}")
        self._importo_complessivo = importo_complessivo

    def get_pubblicata_da(self) -> str:
        '''getter for pubblicata_da'''
        return self._pubblicata_da
    def get_anno_rif(self) -> int:
        '''getter for anno_rif'''
        return self._anno_rif
    def get_tipologia_opera_incompiuta(self) -> str:
        '''getter for tipologia_opera_incompiuta'''
        return self._tipologia_opera_incompiuta
    def get_perc_avanzamento(self) -> int|float:
        '''getter for perc_avanzamento'''
        return self._perc_avanzamento
    def get_mancanza_fondi(self) -> str:
        '''getter for mancanza_fondi'''
        return self._mancanza_fondi
    def get_cause_tecniche(self) -> str:
        '''getter for cause_tecniche'''
        return self._cause_tecniche
    def get_importo_complessivo(self) -> int|float:
        '''getter for importo_complessivo'''
        return self._importo_complessivo

    def __str__(self):
        '''string of Opera object'''
        return (f"OPERA:\n\nPubblicata_da: {self.get_pubblicata_da()},\n"
        f"Anno_rif: {self.get_anno_rif()},\n"
        f"Tipologia_opera_incompiuta: {self.get_tipologia_opera_incompiuta()},\n"
        f"Perc_avanzamento: {self.get_perc_avanzamento()},\n"
        f"Mancanza_fondi: {self.get_mancanza_fondi()},\n"
        f"Cause_tecniche: {self.get_cause_tecniche()},\n"
        f"Importo_complessivo: {self.get_importo_complessivo()},\n"
        f"Natura_opera: {self.get_natura_opera()},\n"
        f"Tipologia_cup: {self.get_tipologia_cup()},\n"
        f"Ambito_oggettivo: {self.get_ambito_oggettivo()},\n"
        f"Categoria: {self.get_categoria()},\n"
        f"Comunitaria: {self.get_comunitaria()},\n"
        f"Data_assegnazione_cup: {self.get_data_assegnazione_cup()},\n"
        f"Lat: {self.get_lat()},\n"
        f"Lon: {self.get_lon()},\n"
        f"Indirizzo: {self.get_indirizzo()}\n")
    def __repr__(self):
        '''string of Opera object'''
        return (f"Opera:[pubblicata_da: {self.get_pubblicata_da()} |\n"
        f"anno_rif: {self.get_anno_rif()} |\n"
        f"Tipologia_opera_incompiuta: {self.get_tipologia_opera_incompiuta()} |\n"
        f"Perc_avanzamento: {self.get_perc_avanzamento()} |\n"
        f"Mancanza_fondi: {self.get_mancanza_fondi()} |\n"
        f"Cause_tecniche: {self.get_cause_tecniche()} |\n"
        f"Importo_complessivo: {self.get_importo_complessivo()} |\n"
        f"Natura_opera: {self.get_natura_opera()} |\n"
        f"Tipologia_cup: {self.get_tipologia_cup()} |\n"
        f"Ambito_oggettivo: {self.get_ambito_oggettivo()} |\n"
        f"Categoria: {self.get_categoria()} |\n"
        f"Comunitaria: {self.get_comunitaria()} |\n"
        f"Data_assegnazione_cup: {self.get_data_assegnazione_cup()} |\n"
        f"Lat: {self.get_lat()} |\n"
        f"Lon: {self.get_lon()} |\n"
        f"Indirizzo: {self.get_indirizzo()}]")
