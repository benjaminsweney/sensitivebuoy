# Design notes for sensitive buoy

## introduction

. Sensitive Bouy is a low cost marine capable device for measuring environmental factors

Initial environmental factors will be

-- Turbidity of water

-- Wave Height

## Background
### bouys
[History of nautical bouys]
(https://cdip.ucsd.edu/?nav=documents&sub=index&xitem=gauge#buoys)

### Wave height
[Discussion on Wave Height calculation]
(https://cdip.ucsd.edu/?nav=documents&sub=index&xitem=waves)

[More on Wave hieght calculation]
(https://www.smhi.se/en/theme/measuring-and-calculating-waves-1.12267)
### Turbdity Measurement
https://www.lenntech.com/turbidity.htm
Measuring turbidity
http://camblab.info/wp/index.php/how-can-i-measure-turbidity/

## IOT device
Pycom Devices

### Development Platform
* Windows 10
* PyCom Maker
* Programming Language : Micro Python
* Atom
* Pycom libraries

An IPX7 level enclosure will be custom built to contain. The enclosure can be a moification of a standard marine bouy

* pycom pi sense board - Light and acceleromator temp pressure
https://docs.pycom.io/chapter/pytrackpysense/apireference/pysense.html
* pycom pi track board - GPS

### Turbidity
* Turbidity will be mearsured with the Light meter measuring the LUX through a light shining through a translucent tube
* Calculation : convert LUX to a 1 to 100 value
* Pycom API CAlls
* Frequency : Once per hour

### Wave Hieght
* Acceleromter 
* Calculation - double integral to get area of wave hieght
* Pycom API calls
* Frequency : Once per 12 hours
3d axis accelerometer to to measure acceleration, 
integrate acceleration over time to get the speed, 
integrate speed over time to get distanceaddd
it boils down to a formula like  height = sum(0.5*a*t^2)   // sum as long as the vertical acceleration has the same sign. 


### Location
* Location from periodic GPS readings
* Calculation : output two values latitude and longtitude
* Frequency : Once per 12 hours


## Pysicical deployment
### Physical structure
Custom 3d enclosure or standard marine buoy
### Power usage
Power designed for Bouy to transmit once every 12 hours for 30 days

## Networks

### GPS 
* Standard GPS commercial network
* Accuracy:

### LORA
* Data output
* Queue packets LORA when in range will be used 
* Data inoput
* Ping and queries of device health

## Device Monitoring
Heartbeat sent via LORA at configurable intervals parameter
