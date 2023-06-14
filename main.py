import time
import ubinascii
from umqttsimple import MQTTClient
import machine
import random
from dht import DHT11
import json
import project_secrets


# Default  MQTT_BROKER to connect to
CLIENT_ID = ubinascii.hexlify(machine.unique_id()) #To create an MQTT client, we need to get the PICOW unique ID
MQTT_BROKER = "io.adafruit.com" # MQTT broker IP address or DNS  
#EXAMPLE IP ADDRESS
#MQTT_BROKER = '192.168.1.144'
PORT = 1883
SUBSCRIBE_TOPIC = b"ellinor_henriksson/feeds/led"
PUBLISH_TOPIC = b"ellinor_henriksson/groups/temperatureandhumidity/json"

# Setup built in PICOW LED as Output
led = machine.Pin("LED", machine.Pin.OUT)

# Setup DHT11 sensor
pin = machine.Pin(28, machine.Pin.OUT, machine.Pin.PULL_DOWN)
sensor = DHT11(pin)


# Publish MQTT messages after every set timeout
LAST_PUBLISH = time.time()  # last_publish variable will hold the last time a message was sent.
publish_interval = 5 #5 seconds --> this means a new message will be sent every 5 seconds


# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))
    if msg.decode() == "ON":
        led.value(1)
    else:
        led.value(0)


# if PicoW Failed to connect to MQTT broker. Reconnecting...'
def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()

# Generate temperature readings
def get_temperature_reading():
    temp = None
    while temp is None:
        try:
            temp = sensor.temperature
        except Exception as error:
            print("An exception occurred: ", error)
    return temp

# Generate humidity readings
def get_humidity_reading():
    humidity = None
    while humidity is None:
        try:
            humidity = sensor.humidity
        except Exception as error:
            print("An exception occurred: ", error)
    return humidity

def main():
    print(f"Begin connection with MQTT Broker :: {MQTT_BROKER}")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, PORT, project_secrets.ADAFRUIT_USERNAME, project_secrets.ADAFRUIT_PASSWORD, keepalive=60)
    mqttClient.set_callback(sub_cb) # whenever a new message comes (to picoW), print the topic and message (The call back function will run whenever a message is published on a topic that the PicoW is subscribed to.)
    mqttClient.connect()
    mqttClient.subscribe(SUBSCRIBE_TOPIC)
    print(f"Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    while True:
        # Non-blocking wait for message
        mqttClient.check_msg()
        global LAST_PUBLISH
        if (time.time() - LAST_PUBLISH) >= publish_interval:
            temp = get_temperature_reading()
            humidity = get_humidity_reading()
            data = {
                "feeds": {
                    "temperature": temp,
                    "humidity": humidity
                }
            }
            json_data = json.dumps(data)
            mqttClient.publish(PUBLISH_TOPIC, json_data.encode())
            LAST_PUBLISH = time.time()
            print("Sent temperature and humidity data...")
        time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()
