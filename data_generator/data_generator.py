import time
import random
from azure.eventhub import EventHubProducerClient, EventData

CONNECTION_STR = "Your Event Hub Namespace Connection String"
EVENTHUB_NAME = "Your Event Hub Name"

producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)

def generate_data():
    while True:
        value = random.randint(50, 100)
        event_data = EventData(str(value))
        producer.send_batch([event_data])
        print(f"Sent: {value}")
        time.sleep(2)

generate_data()
