# Email sending microservice using Gmail smtp and Kafka 

Microservice sending emails from provided gmail account.
Consuming Apache Kafka messages.

## Quickstart 

Clone repo 
 ```
 git clone https://github.com/sandnima/email-microservice.git
 ```
Create `.env` file 
 ```
 HOSTNAME=smtp.gmail.com
 PORT=465
 GMAIL_USERNAME=<gmail-used-to-sending-messages>
 GMAIL_PASSWORD=<password-of-your-google-account>
 KAFKA_TOPIC=<kafka-topic default is "email_send">
 KAFKA_CONSUMER_GROUP=<kafka-consumer-group-id default is "email_send">
 KAFKA_BOOTSTRAP_SERVERS=<kafka-bootstrap-server default is localhost:9092>
```
Create virtual environment 
 ```
 python venv venv
 ```
Install requirements 
 ```
 pip install -r requirements.txt
 ```
Start consuming 
 ```
 python consumer.py
 ```
## Produces message schema 

JSON message
```
{
    "sent_from": "Sample Team",
    "to": ["someone@someservice.com"],
    "subject": "My first microservice",
    "body": "This is a test email from my newly luched microservice."
}
```

## ToDo 

- [x] Email sending functionality using Gmail smtp
- [x] Integration with Kafka server
- [ ] Test
- [ ] Message schema check
- [ ] Dockerize
