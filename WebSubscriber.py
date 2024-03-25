
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("robot/control")
    else:
        print("Failed to connect to MQTT broker")

def on_message(client, userdata, msg):
    control_command = msg.payload.decode()
    print("Received control command:", control_command)
    # Implement logic to execute control command on the robot

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

# Replace 'broker.example.com' with the address of your MQTT broker
client.connect("mqtt.eclipseprojects.io", 1883)

client.loop_forever()
