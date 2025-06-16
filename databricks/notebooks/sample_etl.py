# Databricks notebook: sample_etl_job.py

from pyspark.sql.functions import col

# Load data
df = spark.read.option("header", True).csv("dbfs:/mnt/raw/input.csv")

# Transform
df_transformed = df.withColumn("amount_double", col("amount").cast("double"))

# Write to lake
df_transformed.write.format("delta").mode("overwrite").save(
    "dbfs:/mnt/processed/output"
)
