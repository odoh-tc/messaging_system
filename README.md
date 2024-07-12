# Messaging System with RabbitMQ/Celery and Python Application behind Nginx

This project implements a messaging system using RabbitMQ, Celery for asynchronous task processing, and a FastAPI-based Python application served behind Nginx. ngrok is used to expose the local application endpoint for external testing.

## Overview

This project sets up a messaging system where:

- RabbitMQ handles message queuing.
- Celery manages asynchronous tasks for email sending.
- FastAPI provides the web service endpoints.
- Nginx serves as a reverse proxy for the FastAPI application.
- ngrok is used to expose the local FastAPI application endpoint for testing.

## Features

- **sendmail Endpoint:** Sends an email using SMTP and queues the task with RabbitMQ/Celery.
- **talktome Endpoint:** Logs the current time to `/var/log/messaging_system.log`.
- **Nginx Configuration:** Routes requests to the FastAPI application.
- **Ngrok Setup:** Exposes the local application endpoint for external access.

## Prerequisites

Before starting, ensure you have the following installed and set up:

- Docker
- ngrok (for testing purposes)
- RabbitMQ
- Celery
- Python 3.x

## Setup

### Installing Dependencies

Clone the repository:

```bash
git clone https://github.com/your-username/messaging_system.git
cd messaging_system
```

## Configuration

1. Environment Variables:
   configure with appropriate values

```bash
SMTP_SERVER=your_smtp_server
SMTP_PORT=your_smtp_port
SMTP_USER=your_smtp_username
SMTP_PASSWORD=your_smtp_password
EMAIL_FROM=your_email_from_address
NGROK_AUTHTOKEN=?
RABBITMQ_DEFAULT_USER=?
RABBITMQ_DEFAULT_PASS=?

```

2. Running the Application

```bash
docker-compose up --build
```
