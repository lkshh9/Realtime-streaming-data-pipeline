# Set Up Power BI Real-time Dashboard

Follow these steps to set up a real-time dashboard in Power BI:

1. **Create a Power BI Workspace:**
   - Go to the Power BI service.
   - Create a new workspace for the project.

2. **Create a Streaming Dataset:**
   - In the workspace, create a new streaming dataset with the following schema:
     - `value` (Number)
     - `Risk` (Text)
     
3. **Set Up Azure Stream Analytics:**
   - In the Azure portal, create a new Stream Analytics job.
   - Configure the input to be the Event Hub instance where the processed stream is being sent.
   - Configure the output to be the Power BI workspace and dataset created.
   - Use the provided SQL query to route data from the Event Hub to Power BI.

4. **Build the Dashboard:**
   - In Power BI, create a new report using the streaming dataset.
   - Add visualizations to count and display the 'High' and 'Low' risk values.
   - Pin the visualizations to a new dashboard to see real-time updates.
