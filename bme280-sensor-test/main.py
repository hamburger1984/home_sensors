from machine import Pin, I2C
import ssd1306
import bme280_float
from time import sleep

i2c = I2C(-1, scl=Pin(18), sda=Pin(19))

oled_w = 128
oled_h =  32
char_w =   8
char_h =   8

oled = ssd1306.SSD1306_I2C(oled_w, oled_h, i2c)


modes = [bme280_float.BME280_OSAMPLE_1,
         bme280_float.BME280_OSAMPLE_2,
         bme280_float.BME280_OSAMPLE_4,
         bme280_float.BME280_OSAMPLE_8, # default
         bme280_float.BME280_OSAMPLE_16]
bme = bme280_float.BME280(mode=bme280_float.BME280_OSAMPLE_8, i2c=i2c)

i = 0
while True:
    (t, p, hum) = bme.read_compensated_data()
    hpa = p / 100
    oled.fill(0)
    oled.hline(0, 0, oled_w, 1)

    oled.text(' {0:+2.1f}C   {1:2.1f}%'.format(t, hum), 0, 2)
    oled.hline(0, char_h+3, oled_w, 1)

    oled.text('   {0:4.1f}hPa'.format(hpa), 0, char_h+5)
    oled.hline(0, 2*char_h+6, oled_w, 1)

    i = (i+1) % oled_w
    for x in range(i-20, i+1, 2):
        oled.pixel(x, 2*char_h+10, 1)
        oled.pixel(x, 2*char_h+11, 1)
    oled.hline(0, oled_h-1, oled_w, 1)

    oled.show()
    sleep(1)

#oled.poweroff()
