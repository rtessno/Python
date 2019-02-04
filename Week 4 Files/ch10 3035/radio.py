### radio.py

class Radio:
    def __init__(self,band,station,volume):
        self.__band = band
        self.__station = station
        self.__volume = volume
        
    def set_band(self,band):
        self.__band = band

    def set_station(self,station):
        self.__station = station

    def set_volume(self,volume):
        self.__volume = volume

    def get_band(self):
        return self.__band

    def get_station(self):
        return self.__station

    def get_volume(self):
        return self.__volume
        
    def __str__(self):
        s = 'Now playing ' + self.__band + ' ' + str(self.__station)
        s += ' at volume ' + str(self.__volume)
        return s

    
