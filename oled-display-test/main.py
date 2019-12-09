from machine import Pin, I2C
import ssd1306
from time import sleep_ms

i2c = I2C(-1, scl=Pin(16), sda=Pin(17))

oled_w = 128
oled_h =  64

oled = ssd1306.SSD1306_I2C(oled_w, oled_h, i2c, addr=0x3c)

c = 0
while c < oled_w:
    oled.fill(0)
    t = 'Hello {}'.format(c)
    oled.text(t, c % oled_w - 20, c % oled_h - 8)
    oled.show()
    sleep_ms(20)
    c = c+3

oled.poweroff()