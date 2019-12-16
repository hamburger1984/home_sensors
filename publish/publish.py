from machine import unique_id
from config import mqttHost, mqttSSL, mqttUser, mqttPass, mqttTopicRoot

ID = ''.join('{:2x}'.format(b) for b in unique_id())

def check_requirements():
    import upip
    try:
        try:
            import umqtt.simple
            print('umqtt.simple module exists')
        except:
            upip.install('python-umqtt.simple')
            print('umqtt.simple module installed')
    except:
        print('unable to find or install umqtt.simple module')
        return False

    try:
        try:
            from umqtt.robust import MQTTClient
            print('umqtt.robust module exists')
        except:
            upip.install('python-umqtt.robust')
            print('umqtt.robust module installed')
    except:
        print('unable to find or install umqtt.robust module')
        return False
    return True


def connect():
    from umqtt.robust import MQTTClient
    c = MQTTClient(ID, mqttHost, ssl=mqttSSL,
                   user=mqttUser, password=mqttPass)
    c.DEBUG = True
    if not c.connect():
        c.set_last_will('{}/{}/status'.format(mqttTopicRoot, ID), 'offline', retain=True)
        c.publish('{}/{}/status'.format(mqttTopicRoot, ID), 'connected', retain=True)
        return c
    return None

def publish(client, temperature, pressure, humidity):
    client.publish('{}/{}/t'.format(mqttTopicRoot, ID), '{:.2f}C'.format(temperature), retain=True)
    client.publish('{}/{}/p'.format(mqttTopicRoot, ID), '{:.2f}hPa'.format(pressure), retain=True)
    client.publish('{}/{}/h'.format(mqttTopicRoot, ID), '{:.2f}%'.format(humidity), retain=True)
