# CronScheduler

CronScheduler is an application designed to automate. This project includes several key functionalities that are executed automatically at regular intervals via a cron job.

## Features

### API Queries
CronScheduler queries various external APIs based on the configuration in jsons, to obtain necessary information during the cash register closing process. The APIs queried are:
### SMS Notifications
CronScheduler sends text messages (SMS) to users to notify them about the status of the cash registers, ensuring that users are informed about the process in real-time.

### Error Logging
Errors that occur during the cash register closing process and API queries are logged in the `logs/cron_scheduler_error.log` file. This log is crucial for monitoring and troubleshooting.

### Operation Logging
All operations performed during the cash register closing process are recorded in the `logs/cron_scheduler.log` file. This log provides a detailed history of the system's activities.

### Cron Job
CronScheduler is executed automatically at regular intervals via a cron job. This cron job initiates the cash register closing process, ensuring that the system operates without constant manual intervention.

## Summary
In summary, CronScheduler is a comprehensive application that automates the cash register closing process in the Presico system. Through API queries, SMS notifications, and detailed logging of errors and operations, CronScheduler ensures efficiency and transparency in managing cash registers.

## Log Files
- **Errors:** `logs/cron_scheduler_error.log`
- **Operations:** `logs/cron_scheduler.log`

## Execution
The cron job managing the execution of CronScheduler ensures that the cash register closing process is performed at regular intervals without the need for manual intervention.

---

This project is essential for the efficient and automated management of cash register closings in the Presico system, offering continuous monitoring and real-time notifications.
