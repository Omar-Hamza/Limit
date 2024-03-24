

  // MQTT Broker configuration
  const brokerUrl = 'wss://mqtt.eclipseprojects.io:443/mqtt';
  const client = mqtt.connect(brokerUrl);

  // Handle MQTT connection
  client.on('connect', () => {
    console.log('Connected to MQTT broker');
  });

  // Handle MQTT errors
  client.on('error', (error) => {
    console.log('MQTT broker Error:', error);
  });

  // Function to publish action via MQTT
  
  function toggleAction()
  {
    const readyToggle = document.getElementById('readyToggle');
    if (readyToggle.checked) {
      toggleState = "on";
    } else {
      toggleState = "off";
    }
    sendAction(toggleState);
  }
  
  function sendAction(action) {
    if (client.connected) {
      client.publish('robot/control', action);
      console.log('Published action:', action);
    } else {
      console.log('Not connected to MQTT broker');
    }
  }

  