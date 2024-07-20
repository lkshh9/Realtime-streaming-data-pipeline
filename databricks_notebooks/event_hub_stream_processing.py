from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Initialize Spark session
spark = SparkSession.builder.appName("EventHubStreaming").getOrCreate()

# Configure Event Hub connection
connectionString = "Your Event Hub Namespace Connection String"
ehConf = {
    'eventhubs.connectionString': connectionString,
    'eventhubs.consumerGroup': '$Default',
    'eventhubs.startingPosition': '@latest'
}

# Read stream from Event Hub
df = spark.readStream \
    .format("eventhubs") \
    .options(**ehConf) \
    .load()

# Convert binary values to string and add 'Risk' column
df = df.withColumn("value", df["body"].cast("string"))
df = df.withColumn("value", col("value").cast("integer"))
df = df.withColumn("Risk", expr("CASE WHEN value > 80 THEN 'High' ELSE 'Low' END"))

# Write the processed stream to another Event Hub
outputEventHubConnectionString = "Your Output Event Hub Namespace Connection String"
ehWriteConf = {
    'eventhubs.connectionString': outputEventHubConnectionString
}

query = df.writeStream \
    .format("eventhubs") \
    .options(**ehWriteConf) \
    .option("checkpointLocation", "/path/to/checkpoint/dir") \
    .start()

query.awaitTermination()
