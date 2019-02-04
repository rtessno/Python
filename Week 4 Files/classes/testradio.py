### testradio.py

### import the radio module
import radio

def main():
    ### make a new radio instance
    car_radio = radio.Radio('FM',89.7,5)
    ### display status of radio object
    print(car_radio)

    ### change band, station and volume
    car_radio.set_band('AM')
    car_radio.set_station(620)
    car_radio.set_volume(6)
    ### display status of radio object
    print(car_radio)

    band2 = input('Enter band for other radio in car ')
    ### instantiate another radio object
    radio2 = radio.Radio(band2,1010,0)
    radio2.set_volume(4)
    print(radio2)

    print(radio2.get_station())
    
    
    
main()
