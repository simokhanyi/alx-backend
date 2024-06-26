import kue from 'kue';
import redis from 'redis';

// Create Redis client for Kue
const client = redis.createClient();
const queue = kue.createQueue({ redis: { createClientFactory: () => client } });

// Event listener for successful connection to Redis
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Object containing job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!'
};

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData);

// Event handler when job is created
job.on('created', () => {
  console.log(`Notification job created: ${job.id}`);
});

// Event handler when job completes successfully
job.on('complete', () => {
  console.log('Notification job completed');
  // Remove job from Redis when completed (optional)
  job.remove();
});

// Event handler when job fails
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();

// Process any errors in the queue
queue.on('error', (err) => {
  console.log(`Kue queue error: ${err.message}`);
});
