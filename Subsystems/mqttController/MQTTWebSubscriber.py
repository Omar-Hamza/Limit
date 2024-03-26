"""
This code snippet demonstrates how to connect to an MQTT broker using the Paho MQTT client library and subscribe to a specific topic. 

It also shows how to handle incoming messages and execute control commands based on the received payload.

The `on_connect` function is called when the client successfully connects to the MQTT broker. 

It checks the return code (`rc`) to determine if the connection was successful or not. If successful, it prints a success message and subscribes to the "robot/control" topic.

The `on_message` function is called whenever a new message is received. It decodes the payload of the message and prints the control command. You can implement the logic to execute the control command on the robot in this function.

The code creates an instance of the MQTT client and sets the `on_connect` and `on_message` callbacks. It then connects to the MQTT broker using the specified address and port. Finally, it enters a loop to continuously process incoming messages.

To use this code snippet, replace 'broker.example.com' with the address of your MQTT broker.

Note: This code snippet assumes that you have already installed the Paho MQTT client library.
"""
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
