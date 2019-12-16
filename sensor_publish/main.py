from machine import Pin, I2C, Timer
from micropython import schedule
import sensors
import publish

I2C_SCL=18
I2C_SDA=19

def start():
    i2c = I2C(-1, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
    ids = i2c.scan()

    if not sensors.check_requirements(ids):
        print('requirements for sensors not satisfied ..exit')
        return

    if not publish.check_requirements():
        print('requirements for publish not satisfied ..exit')
        return

    pub = publish.connect()
    if pub is None:
        print('failed to connect for publishing ..exit')
        return

    sens = sensors.connect(i2c)

    def update(_):
        #print('update')
        (t, p, h) = sensors.measure(sens)
        publish.publish(pub, t, p, h)

    # see https://docs.micropython.org/en/latest/library/machine.Timer.html
    # ..and https://docs.micropython.org/en/latest/reference/isr_rules.html
    update_ref = update

    def callback(timer):
        #print('tick')
        schedule(update_ref, 0)

    def callback2(timer):
        schedule(update_ref, 0)
        timer.deinit()

    t = Timer(-1)
    t.init(period=30000, callback=callback)

    t2 = Timer(-2)
    t2.init(mode=Timer.ONE_SHOT, period=750, callback=callback)


# pull pin 23 high to not start sensor_display stuff
DISABLE = Pin(23, Pin.IN)
if DISABLE.value() == 1:
    print('pin 23 is high - not starting.')
else:
    start()