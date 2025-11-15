from hx711 import HX711

hx = HX711(dout_pin=5, pd_sck_pin=6)

def get_weight():
    val = hx.get_weight_mean(10)
    return round(val, 2)