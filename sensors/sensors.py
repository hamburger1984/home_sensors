BME280_ID = 0x76

def check_requirements(i2c_ids):
    if not BME280_ID in i2c_ids:
        print('bme280 id not in i2c ids')
        return False

    import upip
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

def connect(i2c):
    import bme280

    modes = [bme280.BME280_OSAMPLE_1,
             bme280.BME280_OSAMPLE_2,
             bme280.BME280_OSAMPLE_4,
             bme280.BME280_OSAMPLE_8, # default
             bme280.BME280_OSAMPLE_16]
    return bme280.BME280(mode=modes[4], i2c=i2c)

def measure(bme):
    (t, p, h) = bme.read_compensated_data()

    p = p // 256

    return (t / 100, p / 100, h / 1024)

