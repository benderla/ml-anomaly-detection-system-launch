# ML Anomaly Detection System Architecture

## Objective
Deploy a machine learning system capable of detecting anomalous network activity in near real-time.

## Data Pipeline

Data Sources
(Network Logs, Authentication Logs)

        ↓

Streaming Layer
(Apache Kafka)

        ↓

Feature Engineering
(Python / Spark)

        ↓

Model Service
(Isolation Forest Model)

        ↓

Prediction API
(FastAPI)

        ↓

Alert System
(Security Dashboard / SIEM)

        ↓

Monitoring
(Model drift detection + performance metrics)