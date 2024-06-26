const kue = require('kue');
const queue = kue.createQueue();

// Function to process seat reservation job
const processSeatReservation = async () => {
  const { getCurrentAvailableSeats, reserveSeat, reservationEnabled } = require('./redisClient');

  if (!reservationEnabled) {
    return { status: 'Reservation are blocked' };
  }

  try {
    let availableSeats = await getCurrentAvailableSeats();

    if (availableSeats === 0) {
      reservationEnabled = false;
      return { status: 'Reservation are blocked' };
    }

    availableSeats--;
    reserveSeat(availableSeats);

    if (availableSeats >= 0) {
      return { status: 'Reservation successful' };
    } else {
      throw new Error('Not enough seats available');
    }
  } catch (error) {
    throw new Error('Reservation failed');
  }
};

// Process the reserve_seat job in the queue
queue.process('reserve_seat', async (job, done) => {
  try {
    const result = await processSeatReservation();
    console.log(`Seat reservation job ${job.id} completed`);
    done(null, result);
  } catch (error) {
    console.error(`Seat reservation job ${job.id} failed: ${error.message}`);
    done(error);
  }
});

module.exports = queue;
