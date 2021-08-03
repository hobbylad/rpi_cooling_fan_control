from gpiozero import CPUTemperature
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import RPi.GPIO as GPIO
import time

fan_port = 17

fig = plt.figure()
ax_temperature = fig.add_subplot(1, 1, 1)

sample = list()
temperature = list()

def animate(i):
    cpu = CPUTemperature()

    temperature.append(cpu.temperature)

    ax_temperature.clear()   
    ax_temperature.plot(temperature[-1000:])
    plt.title("Temperature (degrees C) vs Time sample")

animation = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

