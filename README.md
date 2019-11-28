# Prepare

Fetch stable build from https://micropython.org/download#esp32

Erase flash and program firmware as described

# Connect to repl

picocom /dev/ttyUSB0 -b115200

C-a, C-x to exit

# Take a look around

```
import esp32
import time

def test_hall(count=100):
    for x in range(count):
        print(' .. {} .. {}'.format(x, esp32.hall_sensor()
        time.sleep_ms(100)
```


# Sample

https://boneskull.com/micropython-on-esp32-part-1/
https://boneskull.com/micropython-on-esp32-part-2/

https://www.hackster.io/bucknalla/mqtt-micropython-044e77
https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
https://micropython-iot-hackathon.readthedocs.io/en/latest/mqtt.html

# More reading

https://www.espressif.com/en/products/hardware/esp32/overview
https://www.espressif.com/en/products/hardware/esp32/resources

https://docs.micropython.org/en/latest/esp32/general.html
https://docs.micropython.org/en/latest/esp32/quickref.html

https://github.com/micropython/micropython
https://github.com/micropython/micropython/tree/master/ports/esp32

https://www.instructables.com/id/ESP32-With-Battery-Holder/

https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/
https://randomnerdtutorials.com/esp32-pinout-reference-gpios/
https://randomnerdtutorials.com/esp32-hall-effect-sensor/
https://makeradvisor.com/esp32-development-boards-review-comparison/

