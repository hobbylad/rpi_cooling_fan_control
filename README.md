# raspberry-pi-cooling-fan-control

##Raspberry Pi Cooling Fan Control

All Raspberry Pi models perform some sort of thermal management reducing performance to avoid overheating under heavy load. The temperature of the CPU core is monitored and clock speed reduced or “throttled” at certain limits. Fan cooling can prevent these limits being reached. This is even more important on “overclocked” systems were stability margin has been reduced. 

The RPi has no hardware support for a fan but a simple fan controller can be written in Python running as a “systemd” service.

See the [blog page for this project](https://hobbylad.wordpress.com/2021/07/24/raspberry-pi-cooling-fan-control/). 

