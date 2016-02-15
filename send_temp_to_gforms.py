
# SE TOIMII, ELI VOIN OHJELMALLISESTI LISATA DATAA GOOGLEN SPREADSHEETIIN!
import requests
url = 'https://docs.google.com/forms/d/1DMmjYbJZqOMPvyXUyR7qsdY3uMTiI83RZAN2MWv8byE/formResponse'
form_data = {'entry.1575876063': '12.3',
            'draftResponse':[],
            'pageHistory':0}
user_agent = {'Referer':'https://docs.google.com/forms/d/1DMmjYbJZqOMPvyXUyR7qsdY3uMTiI83RZAN2MWv8byE/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
while True:
    temp_reading = float(ser.readline())
    form_data['entry.1575876063'] = str(temp_reading)
    print "add datapoint", temp_reading, "to google forms"
    r = requests.post(url, data=form_data, headers=user_agent)
