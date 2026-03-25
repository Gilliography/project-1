# 🚀 Data Engineering Project

## Overview
This project demonstrates a production-style data pipeline using:

- Kafka (streaming)
- Spark (processing)
- Airflow (orchestration)
- PostgreSQL (storage)
- MinIO (data lake)
- dbt (transformations)

## Architecture

Data Generator → Kafka → Spark → Data Lake → Warehouse → Dashboard

## How to Run

### 1. Start services
docker compose -f docker/docker-compose.yml up -d

### 2. Run producer
python streaming/producer.py

### 3. Run Spark consumer
python streaming/consumer_spark.py

### 4. Access Airflow
http://localhost:8080

## Features
- Real-time streaming
- Batch processing
- Orchestration with Airflow
- Data lake storage

## Author
Gilbert Kiprotich