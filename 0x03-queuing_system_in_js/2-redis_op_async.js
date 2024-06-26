import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
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

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

/**
 * Gets and logs the value from Redis for a given key using async/await
 * @param {string} schoolName - The key to get the value for
 */
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error getting key: ${err.message}`);
  }
}

// Call the functions to demonstrate functionality
(async () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
