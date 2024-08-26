const net = require('net');

const server = net.createServer((socket) => {
    console.log('Client connected');

    socket.on('data', (data) => {
        try {
            const command = JSON.parse(data.toString());
            handleCommand(socket, command);
        } catch (error) {
            console.error('Invalid JSON:', error);
            // Optionally send a error response back to client
        }
    });

    socket.on('end', () => {
        console.log('Client disconnected');
    });
});

function handleCommand(socket, command) {
    switch (command.command) {
        case "CONNECT":
            authenticateDevice(socket, command.device_id, command.auth_token);
            break;
        case "DISCONNECT":
            socket.end(); // Close the connection
            console.log("Device disconnected");
            break;
        case "SET_MODE":
            setDeviceMode(socket, command.device_id, command.mode);
            break;
        case "GET_STATUS":
            getDeviceStatus(socket, command.device_id);
            break;
        case "GET_ALL_DEVICES":
            getAllDevices(socket);
            break;
        case "GET_ENERGY_USAGE":
            getEnergyUsage(socket, command.device_id, command.period);
            break;
        case "UPDATE_CONFIG":
            updateDeviceConfig(socket, command.device_id, command.config);
            break;
        default:
            console.log("Unknown command");
    }
}

function authenticateDevice(socket, device_id, auth_token) {
    console.log(`Device ${device_id} authenticated`);
    socket.write(JSON.stringify({response: "CONNECTED", status: "SUCCESS", device_id: device_id}));
}

function setDeviceMode(socket, device_id, mode) {
    console.log(`Mode for device ${device_id} set to ${mode}`);
    socket.write(JSON.stringify({response: "MODE_SET", device_id: device_id, mode: mode}));
}

function getDeviceStatus(socket, device_id) {
    // Example response
    const status = "OK";
    socket.write(JSON.stringify({response: "DEVICE_STATUS", device_id: device_id, status: status}));
}

function getAllDevices(socket) {
    // Example response
    const devices = ["Device1", "Device2"];
    socket.write(JSON.stringify({response: "ALL_DEVICES", devices: devices}));
}

function getEnergyUsage(socket, device_id, period) {
    // Example response
    const usage = "100 kWh";
    socket.write(JSON.stringify({response: "ENERGY_USAGE", device_id: device_id, usage: usage, period: period}));
}

function updateDeviceConfig(socket, device_id, config) {
    console.log(`Config for device ${device_id} updated`);
    socket.write(JSON.stringify({response: "CONFIG_UPDATED", device_id: device_id}));
}

server.listen(6100, () => {
    console.log('Server is listening on port 6100');
});
