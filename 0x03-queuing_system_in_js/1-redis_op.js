import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a value in Redis for a given key
 * @param {string} schoolName - The key to set in Redis
 * @param {string} value - The value to set for the key
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Gets and logs the value from Redis for a given key
 * @param {string} schoolName - The key to get the value for
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting key: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions to demonstrate functionality
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
