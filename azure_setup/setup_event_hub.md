# Set Up Azure Event Hub

Follow these steps to set up an Azure Event Hub:

1. **Create an Event Hub Namespace:**
   - Go to the Azure portal.
   - Navigate to "Create a resource" > "Event Hubs".
   - Create a new Event Hub Namespace and provide the required details.
   
2. **Create an Event Hub:**
   - Inside the Event Hub Namespace, create a new Event Hub instance.
   - Note the connection string and Event Hub name for use in the data generator script.

3. **Create a Consumer Group:**
   - In the Event Hub instance, create a new consumer group for Databricks to read the stream.
