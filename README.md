# Real-time Streaming Data Pipeline

This project demonstrates an end-to-end real-time streaming data pipeline using Azure Event Hub, Databricks, Azure Stream Analytics, and Power BI. The pipeline involves generating random data, processing it, and visualizing it in real-time.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Create a Dummy Data Generator](#step-1-create-a-dummy-data-generator)
- [Step 2: Set Up Azure Event Hub](#step-2-set-up-azure-event-hub)
- [Step 3: Capture the Incoming Event Hub Stream Using Structured Streaming in Databricks](#step-3-capture-the-incoming-event-hub-stream-using-structured-streaming-in-databricks)
- [Step 4: Add a 'Risk' Column to the Stream](#step-4-add-a-risk-column-to-the-stream)
- [Step 5: Capture the Output Stream in a Separate Event Hub](#step-5-capture-the-output-stream-in-a-separate-event-hub)
- [Step 6: Connect the Output Stream to Power BI Using Stream Analytics](#step-6-connect-the-output-stream-to-power-bi-using-stream-analytics)
- [Step 7: Build a Real-time Dashboard in Power BI](#step-7-build-a-real-time-dashboard-in-power-bi)

## Prerequisites
- Azure subscription
- Databricks workspace
- Power BI account

## Step 1: Create a Dummy Data Generator

Create a Python script that generates random numbers between 50 and 100 every 2 seconds and sends them to Azure Event Hub.

## Step 2: Set Up Azure Event Hub

1. Create an Event Hub namespace in the Azure portal.
2. Within the namespace, create an Event Hub instance.

## Step 3: Capture the Incoming Event Hub Stream Using Structured Streaming in Databricks

Create a Databricks notebook to read the stream from Event Hub, process it, and write it back to another Event Hub.

## Step 4: Add a 'Risk' Column to the Stream

Process the stream in Databricks to add a 'Risk' column where values greater than 80 are marked as 'High' and others as 'Low'.

## Step 5: Capture the Output Stream in a Separate Event Hub

Send the processed stream with the 'Risk' column to another Event Hub.

## Step 6: Connect the Output Stream to Power BI Using Stream Analytics

Set up Azure Stream Analytics to route data from the Event Hub to Power BI.

## Step 7: Build a Real-time Dashboard in Power BI

Create a real-time dashboard in Power BI to visualize the data, showing counts of 'High' and 'Low' risk values.
