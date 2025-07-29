'''Models the Opera class'''

from datetime import date
import unittest
from luogo import Luogo
from tools import str_to_date

class Opera(Luogo):
    '''models a public work (Opera)'''
    def __init__(self, natura_opera:str, tipologia_cup:str, ambito_oggettivo:str,
                 categoria:str, comunitaria:str,
                 data_assegnazione_cup:date,
                 lat:int|float, lon:int|float, indirizzo:str):
        '''initialisation of instance variables'''
        super().__init__(lat, lon, indirizzo)
        self.set_natura_opera(natura_opera)
        self.set_tipologia_cup(tipologia_cup)
        self.set_ambito_oggettivo(ambito_oggettivo)
        self.set_categoria(categoria)
        self.set_comunitaria(comunitaria)
        self.set_data_assegnazione_cup(data_assegnazione_cup)

    def set_natura_opera(self, natura_opera:str):
        '''setter for natura_opera'''
        if not isinstance(natura_opera, str) and (natura_opera is not None):
            raise TypeError(f"Wrong natura_opera type: you provided {type(natura_opera)}")
        self._natura_opera = natura_opera
    def set_tipologia_cup(self, tipologia_cup:str):
        '''setter for tipologia_cup'''
        if not isinstance(tipologia_cup, str) and (tipologia_cup is not None):
            raise TypeError(f"Wrong tipologia_cup type: you provided {type(tipologia_cup)}")
        self._tipologia_cup = tipologia_cup
    def set_ambito_oggettivo(self, ambito_oggettivo:str):
        '''setter for ambito_oggettivo'''
        if not isinstance(ambito_oggettivo, str) and (ambito_oggettivo is not None):
            raise TypeError(f"Wrong ambito_oggettivo type: you provided {type(ambito_oggettivo)}")
        self._ambito_oggettivo = ambito_oggettivo
    def set_categoria(self, categoria:str):
        '''setter for categoria'''
        if not isinstance(categoria, str) and (categoria is not None):
            raise TypeError(f"Wrong categoria type: you provided {type(categoria)}")
        self._categoria = categoria
    def set_comunitaria(self, comunitaria:str):
        '''setter for comunitaria'''
        if not isinstance(comunitaria, str) and (comunitaria is not None):
            raise TypeError(f"Wrong comunitaria type: you provided {type(comunitaria)}")
        self._comunitaria = comunitaria
    def set_data_assegnazione_cup(self, data_assegnazione_cup:date):
        '''setter for data_assegnazione_cup'''
        if not isinstance(data_assegnazione_cup, date) and (data_assegnazione_cup is not None):
            raise TypeError(
                f"Wrong data_assegnazione_cup type: you provided {type(data_assegnazione_cup)}")
        self._data_assegnazione_cup = data_assegnazione_cup

    def get_natura_opera(self) -> str:
        '''getter for natura_opera'''
        return self._natura_opera
    def get_tipologia_cup(self) -> str:
        '''getter for tipologia_cup'''
        return self._tipologia_cup
    def get_ambito_oggettivo(self) -> str:
        '''getter for ambito_oggettivo'''
        return self._ambito_oggettivo
    def get_categoria(self) -> str:
        '''getter for categoria'''
        return self._categoria
    def get_comunitaria(self) -> str:
        '''getter for comunitaria'''
        return self._comunitaria
    def get_data_assegnazione_cup(self) -> date:
        '''getter for data_assegnazione_cup'''
        return self._data_assegnazione_cup

    def __str__(self):
        '''string of Opera object'''
        return (f"Opera: [natura_opera: {self.get_natura_opera()},\n"
        f"tipologia_cup: {self.get_tipologia_cup()},\n"
        f"ambito_oggettivo: {self.get_ambito_oggettivo()},\n"
        f"categoria: {self.get_categoria()},\n"
        f"comunitaria: {self.get_comunitaria()},\n"
        f"data_assegnazione_cup: {self.get_data_assegnazione_cup()},\n"
        f"lat: {self.get_lat()},\n"
        f"lon: {self.get_lon()},\n"
        f"indirizzo: {self.get_indirizzo()}]")
    def __repr__(self):
        '''representation string of Opera object'''
        return (f"Natura_opera: {self.get_natura_opera()} |\n"
        f"Tipologia_cup: {self.get_tipologia_cup()} |\n"
        f"Ambito_oggettivo: {self.get_ambito_oggettivo()} |\n"
        f"Categoria: {self.get_categoria()} | "
        f"Comunitaria: {self.get_comunitaria()} |\n"
        f"Data_assegnazione_cup: {self.get_data_assegnazione_cup()} |\n"
        f"Lat: {self.get_lat()} |\n"
        f"Lon: {self.get_lon()} |\n"
        f"Indirizzo: {self.get_indirizzo()}]")

class OperaTest(unittest.TestCase):
    '''class tester for unittset. 
    Only "comunitaria" and "data_assegnazione_cup" attributes are tested'''
    def setUp(self):
        '''setup methods'''
        self._natura_opera = ""
        self._tipologia_cup = ""
        self._ambito_oggettivo = ""
        self._categoria = ""
        self._comunitaria = "si"
        self._data_assegnazione_cup = str_to_date("19/07/2002")
        self._lat = 0.0
        self._lon = 0.0
        self._indirizzo = ""
        self.opera = Opera(self._natura_opera, self._tipologia_cup, self._ambito_oggettivo,
                           self._categoria, self._comunitaria, self._data_assegnazione_cup,
                           self._lat, self._lon, self._indirizzo)
    def testComunitaria(self):
        '''method to test comunitaria: getter,exceptions,setter'''
        # check getter
        self.assertEqual(self.opera.get_comunitaria(),self._comunitaria)
        # check exceptions
        with self.assertRaises(TypeError):
            self.opera.set_comunitaria(1)
        # check setter
        new_comunitaria = 'no'
        self.opera.set_comunitaria(new_comunitaria)
        self.assertEqual(self.opera.get_comunitaria(),new_comunitaria)
    def testData_assegnazione_cup(self):
        '''method to test data_assegnazione_cup: getter,exceptions,setter'''
        # check getter
        self.assertEqual(self.opera.get_data_assegnazione_cup(),self._data_assegnazione_cup)
        # check exceptions
        with self.assertRaises(TypeError):
            self.opera.set_data_assegnazione_cup("19/07/2002")
        # check setter
        new_data_assegnazione_cup = str_to_date("25/10/2003")
        self.opera.set_data_assegnazione_cup(new_data_assegnazione_cup)
        self.assertEqual(self.opera.get_data_assegnazione_cup(),new_data_assegnazione_cup)

if __name__ == "__main__":
    unittest.main(verbosity=2)
