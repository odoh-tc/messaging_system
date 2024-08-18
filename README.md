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

### Local Installation

1. RabbitMQ Local Installation: I ran the debian installation script

```sh
#!/bin/sh

sudo apt-get install curl gnupg apt-transport-https -y

## Team RabbitMQs main signing key
curl -1sLf "https://keys.openpgp.org/vks/v1/by-fingerprint/0A9AF2115F4687BD29803A206B73A36E6026DFCA" | sudo gpg --dearmor | sudo tee /usr/share/keyrings/com.rabbitmq.team.gpg > /dev/null
## Community mirror of Cloudsmith: modern Erlang repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg > /dev/null
## Community mirror of Cloudsmith: RabbitMQ repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.9F4587F226208342.gpg > /dev/null

## Add apt repositories maintained by Team RabbitMQ
sudo tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
## Provides modern Erlang/OTP releases
##
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

# another mirror for redundancy
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

## Provides RabbitMQ
##
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main

# another mirror for redundancy
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
EOF

## Update package indices
sudo apt-get update -y

## Install Erlang packages
sudo apt-get install -y erlang-base \
                        erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                        erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                        erlang-runtime-tools erlang-snmp erlang-ssl \
                        erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl

## Install rabbitmq-server and its dependencies
sudo apt-get install rabbitmq-server -y --fix-missing
```

To confirm if RabbitMQ is installed correctly, run this command

```sh
sudo rabbitmqctl status
```

2. Celery Installation

```sh
sudo apt install python3.10-venv
python3 -m venv env
# start up the virtual environment
source env/bin/activate
pip install celery
# confirm celery installation
celery --version
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

```

### Docker deployment

```bash
docker-compose up --build
```
