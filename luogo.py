'''This class models a geographic place
with latitude, longitude and address ("indirizzo")'''

import unittest
import math as m
from custom_exs import LatValueError,LonValueError

class Luogo:
    '''class modeling a place'''
    def __init__(self, lat:int|float, lon:int|float, indirizzo: str = ""):
        '''initialisation of instance variables'''
        self.set_lat(lat)
        self.set_lon(lon)
        self.set_indirizzo(indirizzo)
    def set_lat(self, lat:int|float):
        '''setter for lat'''
        if not isinstance(lat, (int, float)) and (lat is not None):
            raise TypeError(f"Wrong lat type: you provided {type(lat)}")
        if lat is not None:
            if (lat>90 or lat<-90):
                raise LatValueError("Lat out of range (-90;+90)")
        self._lat = lat
    def set_lon(self, lon:int|float):
        '''setter for lon'''
        if not isinstance(lon, (int, float)) and (lon is not None):
            raise TypeError(f"Wrong lon type: you provided {type(lon)}")
        if lon is not None:
            if (lon>180 or lon<-180):
                raise LonValueError("Lon out of range (-180;+180)")
        self._lon = lon
    def set_indirizzo(self,indirizzo:str):
        '''setter for address'''
        if not isinstance(indirizzo, str) and (indirizzo is not None):
            raise TypeError(f"Wrong address type: you provided {type(indirizzo)} ")
        self._indirizzo = indirizzo
    def get_lat(self) -> int|float:
        '''getter for lat'''
        return self._lat
    def get_lon(self) -> int|float:
        '''getter for lon'''
        return self._lon
    def get_indirizzo(self) -> str:
        '''getter for address'''
        return self._indirizzo
    def __str__(self):
        '''string of Luogo object'''
        return f"Luogo:[lat={self.get_lat()},lon={self.get_lon()},address={self.get_indirizzo()}]"
    def __repr__(self):
        '''representation string of Luogo object'''
        return f"[Lat:{self.get_lat()}|Lon:{self.get_lon()}|Address:{self.get_indirizzo()}]"
    def haversine_distance(self,place):
        '''returns the Haversine distance (km) between the place and another provided'''
        radius = 6371 # average Earth radius in Italy
        if not isinstance(place,Luogo):
            raise TypeError(f"Wrong type. You provided {type(place)}")
        if  self.get_lat() is None or self.get_lon() is None:
            return None
        _lat = m.radians(self.get_lat())
        _lon = m.radians(self.get_lon())
        _lat_place = m.radians(place.get_lat())
        _lon_place = m.radians(place.get_lon())
        _delta_lat = _lat - _lat_place
        _delta_lon = _lon - _lon_place
        a = (m.sin(_delta_lat / 2) ** 2 + m.cos(_lat_place) *
             m.cos(_lat) * m.sin(_delta_lon / 2) ** 2)
        l = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))
        distance = radius * l
        return distance

class LuogoTest(unittest.TestCase):
    '''class tester for unittset'''
    def setUp(self):
        '''setup methods'''
        self._lat = 43.5727
        self._lon = 13.4918
        self._indirizzo = "Via Roma"
        self.luogo = Luogo(self._lat,self._lon,self._indirizzo)
    def testLat(self):
        '''method to test lat: getter,exceptions,setter'''
        # check getter
        self.assertAlmostEqual(self.luogo.get_lat(),self._lat)
        # check exceptions
        with self.assertRaises(TypeError):
            self.luogo.set_lat('43.5727')
        with self.assertRaises(LatValueError):
            self.luogo.set_lat(-91.5678)
        # check setter
        new_lat = 43.6727
        self.luogo.set_lat(new_lat)
        self.assertEqual(self.luogo.get_lat(),new_lat)
    def testLon(self):
        '''method to test lon: getter,exceptions,setter'''
        # check getter
        self.assertAlmostEqual(self.luogo.get_lon(),self._lon)
        # check exceptions
        with self.assertRaises(TypeError):
            self.luogo.set_lon('13.4918')
        with self.assertRaises(LonValueError):
            self.luogo.set_lon(-181.9658)
        # check setter
        new_lon = 13.5918
        self.luogo.set_lon(new_lon)
        self.assertEqual(self.luogo.get_lon(),new_lon)
    def testIndirizzo(self):
        '''method to test address: getter,exceptions,setter'''
        # check getter
        self.assertEqual(self.luogo.get_indirizzo(),self._indirizzo)
        # check exceptions
        with self.assertRaises(TypeError):
            self.luogo.set_indirizzo(46)
        # check setter
        new_address = "Via Trento"
        self.luogo.set_indirizzo(new_address)
        self.assertEqual(self.luogo.get_indirizzo(),new_address)
    def testHaversine_distance(self):
        '''method to test haversine_distance Raise Error'''
        with self.assertRaises(TypeError):
            self.luogo.haversine_distance((43, 13))

if __name__=='__main__':
    unittest.main(verbosity=2)
