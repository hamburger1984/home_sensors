# Home Sensors

## Idea

Monitor humidity and temperature using micropython on an ESP32 board.

Maybe push the measured values to a MQTT broker to fetch, display, record
and maybe plot them. Either use some free(?) existing broker or install one on a
raspberry pi in the local network.

### Hardware

[WEMOS ESP32 board with battery holder](http://www.raspberrypiwiki.com/index.php/WEMOS_ESP32_Board_with_18650_Battery_Holder)

[ADSONG AM2302 / DHT22](https://learn.adafruit.com/dht)


### Wiring diagram

```
              +--------------+
+---------+   |              |
|         |   | +-----+      |
| AMS2302 |   | |     |      |
|         |   | | +---+------+----------------+
|         |   | | |  P22    GND               |
|   D     |   | | |                           |
| V A   G |   | | |      ESP32 Board          |
| C T N N |   | | |                           |
| C A C D |   | | |                           |
+-+-+-+-+-+   | | | VCC                       |
  | | | |     | | +--+------------------------+
  | | + +-----+ |    |
  | |           |    |
  | +-----------+    |
  |                  |
  +------------------+
```


### Testing the sensor


```
from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(22))

while True:
    try:
        sleep(2)
        sensor.measure()
        print('Temperature {} C, {} % .. {}'.format(sensor.temperature(),
                                                    sensor.humidity(),
                                                    sensor.buf))
    except OSError:
        print('Failed to measure')
```
