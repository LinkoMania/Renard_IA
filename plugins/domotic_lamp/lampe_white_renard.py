import tinytuya

# Remplacez les informations ci-dessous par les vôtres
bulb_device_id = "bf410f2735249b01f4pnpo"
bulb_ip_address = "192.168.129.35"
local_key = "p}eXt:#T/4X'sci5"

# Créez une instance de l'appareil
bulb_device = tinytuya.BulbDevice(bulb_device_id, bulb_ip_address, local_key)
bulb_device.set_version(3.3)

# Réglez la couleur de l'ampoule en blanc
bulb_device.set_white(1000, 1000)  # Réglez la luminosité sur 1000 et la température de couleur sur 1000
