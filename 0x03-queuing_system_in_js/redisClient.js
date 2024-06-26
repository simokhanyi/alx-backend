const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();

client.on('connect', () => {
  console.log('Connected to Redis');
});

// Function to reserve seats
const reserveSeat = (number) => {
  client.set('available_seats', number);
};

// Async function to get current available seats
const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats) || 0;
};

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservation status
let reservationEnabled = true;

module.exports = { reserveSeat, getCurrentAvailableSeats, reservationEnabled };
