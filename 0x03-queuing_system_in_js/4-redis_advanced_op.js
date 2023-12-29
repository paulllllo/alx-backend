import { createClient } from 'redis';

const redis = require('redis');

const client = createClient();

client.connect().then(() => {
  console.log('Redis client connected to the server');
}).catch((err) => {
  console.log('Redis client not connected to the server:', err.message);
})
const HASH = 'HolbertonSchools';

client.hSet(HASH, 'Portland', '50', redis.print);
client.hSet(HASH, 'Seattle', '80', redis.print);
client.hSet(HASH, 'New York', '20', redis.print);
client.hSet(HASH, 'Bogota', '20', redis.print);
client.hSet(HASH, 'Cali', '40', redis.print);
client.hSet(HASH, 'Paris', '2', redis.print);

client.hGetAll(HASH).then((data) => console.log(data));
