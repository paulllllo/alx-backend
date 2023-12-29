import { createClient } from 'redis';

const redis = require('redis');

const client = createClient();

client.connect().then(() => {
  console.log('Redis client connected to the server');
}).catch((err) => {
  console.log('Redis client not connected to the server:', err.message);
})

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, data) => console.log(data));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
