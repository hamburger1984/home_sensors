# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


# for this to work, copy config.py.template to config.py
# ..and set wlanSSID and wlanPass for your network.
import config
import network

n = network.WLAN(network.STA_IF)
n.active(True)

s = n.scan()
for (ssid, bssid, channel, RSSI, authmode, hidden) in s:
    if ssid == config.wlanSSID:
        print('connecting to {0} on channel {1}..'.format(ssid, channel))
        n.connect(ssid, config.wlanPass)
        break
