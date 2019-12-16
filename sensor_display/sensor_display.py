# connect oled (128x32) and bme280 to a common I2C
# pin 18 - SCL
# pin 19 - SDA

SCL = 18
SDA = 19

def check_requirements():
    import upip
    try:
        try:
            from ssd1306 import SSD1306_I2C
            print('ssd1306 module exists')
        except:
            upip.install('micropython-ssd1306')
            print('ssd1306 module installed')
    except:
        print('failed to find or install ssd1306')
        return False

    try:
        try:
            import bme280
            print('bme280 module exists')
        except:
            upip.install('micropython-bme280')
            print('bme280 module installed')
    except:
        print('failed to find or install bme280')
        return False
    return True


OLED_W = 128
OLED_H = 32 #64
CHAR_W = 8
CHAR_H = 8

def start():
    from ssd1306 import SSD1306_I2C
    import bme280
    from machine import Pin, I2C

    i2c = I2C(-1, scl=Pin(SCL), sda=Pin(SDA))
    ids = i2c.scan()
    print('found {} on i2c bus (scl={}, sda={})'.format(ids, SCL, SDA))

    if not 0x76 in ids:
        print('could not find bme sensor on i2c bus (scl={}, sda={}) .. exit'.format(SCL, SDA))
        return

    if not 0x3c in ids:
        print('no ssd1306 display found on i2c bus (scl={}, sda={})'.format(SCL, SDA))

    oled = SSD1306_I2C(OLED_W, OLED_H, i2c) if 0x3c in ids else None

    modes = [bme280.BME280_OSAMPLE_1,
             bme280.BME280_OSAMPLE_2,
             bme280.BME280_OSAMPLE_4,
             bme280.BME280_OSAMPLE_8, # default
             bme280.BME280_OSAMPLE_16]
    bme = bme280.BME280(mode=modes[3], i2c=i2c)

    run(oled, bme)


def run(oled, bme):
    from time import sleep

    i = 0
    while True:
        (t, p, h) = bme.read_compensated_data()

        p = p // 256
        pi = p // 100
        pd = p - pi * 100

        hi = h // 1024
        hd = h * 100 // 1024 - hi * 100

        td = t / 100

        if oled is None:
            print('{0:+2.1f}C {1}.{2:02d}% {3}.{4:02d}hPa'.format(td, hi, hd, pi, pd))
        else:
            oled.fill(0)
            #oled.hline(0, 0, OLED_W, 1)

            oled.text(' {0:+2.1f}C   {1}.{2:02d}%'.format(td, hi, hd), 0, 2)
            #oled.hline(0, CHAR_H+3, OLED_W, 1)

            oled.text('   {0}.{1:02d}hPa'.format(pi, pd), 0, CHAR_H+5)
            #oled.hline(0, 2*CHAR_H+6, OLED_W, 1)

            oled.hline(0, OLED_H-6, OLED_W, 1)
            i = (i+1) % OLED_W
            for x in range(i-20, i+1, 2):
                oled.vline(x, OLED_H-4, 2, 1)
            oled.hline(0, OLED_H-1, OLED_W, 1)

            oled.show()
        sleep(5 if oled is None else 2)
