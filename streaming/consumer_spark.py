from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("KafkaStream") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "rides") \
    .option("startingOffsets", "latest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)")

query = json_df.writeStream \
    .format("parquet") \
    .option("path", "data_lake/rides") \
    .option("checkpointLocation", "data_lake/checkpoints") \
    .outputMode("append") \
    .start()

query.awaitTermination()