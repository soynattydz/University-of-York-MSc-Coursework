const net = require('net');
const client = new net.Socket();

client.connect(6100, 'localhost', () => {
    console.log('Connected to server');

    // Send CONNECT command
    const connectCommand = JSON.stringify({
        command: "CONNECT",
        device_id: "IoT-Device-001",
        device_type: "Thermostat",
        auth_token: "abcdef12345"
    });
    client.write(connectCommand);

    // Send another command, e.g., SET_MODE
    setTimeout(() => {
        const setModeCommand = JSON.stringify({
            command: "SET_MODE",
            device_id: "IoT-Device-001",
            mode: "energy_saving"
        });
        client.write(setModeCommand);
    }, 1000);

    // Disconnect after a short delay
    setTimeout(() => {
        client.write(JSON.stringify({
            command: "DISCONNECT"
        }));
        client.end();
    }, 2000);
});

client.on('data', (data) => {
    console.log('Received from server:', data.toString());
});

client.on('close', () => {
    console.log('Connection closed');
});

client.on('error', (error) => {
    console.error('Connection error:', error);
});
