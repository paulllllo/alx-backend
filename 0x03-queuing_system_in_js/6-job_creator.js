const kue = require('kue');

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '+2348164404546',
  message: 'The journey to earth 2.0 will take 116 years',
}).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('failed', () => console.log('Notification job failed'));
job.on('complete', () => console.log('Notification job completed'));
