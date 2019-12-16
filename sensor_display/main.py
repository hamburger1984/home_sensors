from machine import Pin

# pull pin 23 high to not start sensor_display stuff
DISABLE = Pin(23, Pin.IN)
if DISABLE.value() == 1:
    print('pin 23 is high - not starting.')
else:
    import sensor_display
    if sensor_display.check_requirements():
        sensor_display.start()
