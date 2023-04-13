import RPi.GPIO as GPIO
import time

sensor_pin = 18  # Conectar el pin de salida del sensor al pin 18 de la Raspberry Pi
Fotocelula_pin =21 
umbral_Fotocelula = 500
sensor_pin2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(sensor_pin2, GPIO.IN)
GPIO.setup(Fotocelula_pin,GPIO.IN)

try:
    while True:
        valor_fotocelula= GPIO.input(Fotocelula_pin)  # Leer el valor del sensor  
        hay_poca_luz = valor_fotocelula < umbral_Fotocelula
        sensor=GPIO.input(sensor_pin2)
                
        if GPIO.input(sensor_pin) and hay_poca_luz:
                x=sensor_pin
                sensor_value = GPIO.input(sensor_pin)
                print("Valor del sensor: ",sensor_value)
                time.sleep(0.5)  # Esperar medio segundo antes de l
                print("valor del sensor 2",sensor)        
        else: print("hay mucha luz")
except KeyboardInterrupt:
    GPIO.cleanup()
