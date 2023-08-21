# Assignment - Internet of Things

Hardware and sensors are constantly added to our lives. Sensors produce data, data that often need to be collected and analyzed. Having a basic knowledge of IoT protocols opens many doors for exciting projects as a web developer. This assignment aims to create a thing that connects to the web, a Web Thing.
IOT 2023

## Description

Build a thing that connects to the internet, either independently or through a gateway. The function and if it should have actions, properties, or both are up to you and your project. Create a web interface for your thing. Do you collect a lot of data? Why not show it on a chart?

Looking for inspiration? Please have a look at [some of our example projects](https://coursepress.lnu.se/kurser/webben-som-applikationsplattform/iot/exempel)

## Requirements

The requirements for the assignment are quite straightforward. But, they can be discussed if they are stopping you from achieving your goals.

### Must

* The Raspberry Pi Pico W microcontroller is connected to WiFi.
* The Raspberry Pi Pico W microcontroller reads the temperature and humidity data of sensor DHT11.
* The Raspberry Pi Pico W microcontroller sends the temperature and humidity data to the Adafruit MQTT Broker using the MQTT protocol. The data need to be prepared in a JSON format.
* The Raspberry Pi Pico W microcontroller must be controlled by a button on the Adafruit dashboard i.e. if Rpi Pico W receives the command "ON" or "OFF" on the "LED" topic, the built-in LED of Rpi Pico W must be on or off.
* Written report (PDF file) and prerecorded presentation (MP4 file). The assignment files (PDF and MP4) must follow the format:  "yourlnucode_1DV027_IoT.pdf", "yourlnucode_1DV027_IoT.mp4"

## Assignment Report

Your application will be presented using a "Tutorial style" assignment report. For details, see the included [template](./Template.md). It is recommended that you replace this README.md with your final report, but you are free to place the report wherever you want as long as it is linked in the Merge Request.

## Merge Request

You hand in the assignment by making a Merge Request of your project against the lnu/submit-branch. It is OK to have additional projects and repositories, but include a link to them in the Submission report.
Pay extra attention to including a link to your Assignment Report.
