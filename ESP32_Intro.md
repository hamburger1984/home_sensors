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

