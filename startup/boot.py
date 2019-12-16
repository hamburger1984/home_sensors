# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


# for this to work, copy config.py.template to config.py
# ..and set wlanSSID and wlanPass for your network.
import config
import network
from time import sleep

n = network.WLAN(network.STA_IF)
if not n.active():
    n.active(True)

if not n.isconnected():
    s = n.scan()
    for (ssid, bssid, channel, RSSI, authmode, hidden) in s:
        if ssid == config.wlanSSID:
            print('connecting to {0} on channel {1}..'.format(ssid, channel))
            n.connect(ssid, config.wlanPass)
            waiting = 0
            while waiting < 10 and not n.isconnected():
                sleep(1)
                waiting = waiting + 1
            break
