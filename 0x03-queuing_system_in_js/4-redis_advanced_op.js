import redis from 'redis';

// Create Redis client
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Store hash values
function createHolbertonSchoolsHash() {
  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };

  for (const [city, value] of Object.entries(schools)) {
    client.hset('HolbertonSchools', city, value, redis.print);
  }
}

// Display hash values
function displayHolbertonSchoolsHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error getting hash: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions to demonstrate functionality
createHolbertonSchoolsHash();
displayHolbertonSchoolsHash();
