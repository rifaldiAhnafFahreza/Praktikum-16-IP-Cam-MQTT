import paho.mqtt.client as mqtt
subscribe = "Rifaldi"
def on_message(client, userdata, message):
    data = str(message.payload.decode())
    print(data)
    return
client = mqtt.Client()
client.on_message = on_message
server = "mqtt-dashboard.com"
client.connect(server, 1883)
client.subscribe(subscribe)
while True:
    client.loop()
    client.loop_stop()