## Email sending microservice using Gmail smtp and Kafka

### Quickstart
1. Clone repo
    ```
    git clone https://github.com/sandnima/email-microservice.git
    ```
2. Create `.env` file:
    ```
    HOSTNAME=smtp.gmail.com
    PORT=465
    GMAIL_USERNAME=<gmail-used-to-sending-messages>
    GMAIL_PASSWORD=<password-of-your-google-account>
    KAFKA_TOPIC=<kafka-topic default is "email_send">
    KAFKA_CONSUMER_GROUP=<kafka-consumer-group-id default is "email_send">
    KAFKA_BOOTSTRAP_SERVERS=<kafka-bootstrap-server default is localhost:9092>
    ```
3. Create virtual environment
    ```
    python venv venv
    ```
4. Install requirements 
    ```
    pip install -r requirements.txt
    ```
5. Start consumer
    ```
    python consumer.py
    ```

### ToDo:
- [x] Email sending functionality using Gmail smtp
- [x] Integration with Kafka server
- [ ] Test
- [ ] Dockerize
