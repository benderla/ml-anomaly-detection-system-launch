# ML Anomaly Detection System Launch (TPM Project)

## Overview
This project demonstrates how a Technical Program Manager can lead the deployment of a machine learning anomaly detection system into production.

This repo focuses on the operational deployment and system launch architecture for anomaly detection services.

## Technology Stack

Python  
scikit-learn  
Jupyter  
FastAPI (inference concept)  
Kafka (streaming concept)

## Quick Start

Install dependencies:

pip install -r requirements.txt

Run the anomaly detection demo notebook:

jupyter notebook notebooks/anomaly_detection_demo.ipynb

The notebook demonstrates:

• loading sample network logs  
• feature engineering  
• training an Isolation Forest model  
• detecting anomalous network activity

## Objectives
• Deploy a real-time anomaly detection pipeline  
• Integrate ML predictions with security monitoring tools  
• Establish program governance, risks, and launch metrics  

## Why This Project

Machine learning systems require cross-team coordination between data engineering, ML engineering, and platform teams.

This repository demonstrates how a Technical Program Manager can structure the delivery of an ML anomaly detection system from architecture design through production launch.

## Related Repositories

This project is part of a set of repositories demonstrating the machine learning lifecycle for cybersecurity anomaly detection.

• network-attack-detection  
  Model development and anomaly detection using Isolation Forest.

• ml-anomaly-detection-system-launch  
  Deployment architecture and program planning for an ML system.

• ml-model-monitoring  
  Monitoring model performance and detecting drift in production systems.

## System Architecture
See: architecture/system_architecture.md

The system ingests network logs, transforms them into behavioral features, 
applies an Isolation Forest anomaly detection model, and surfaces alerts 
through a monitoring dashboard.

## Architecture

![System Architecture](diagrams/ml-system-architecture.png)

This system is designed as an end-to-end anomaly detection workflow for network security monitoring.

Architecture flow:

Network Logs  
→ Data Ingestion Pipeline  
→ Feature Engineering  
→ Isolation Forest Model  
→ Inference Service  
→ Security Dashboard / Alerting Layer

The architecture supports the core stages needed to move an anomaly detection model from development into a production-style environment. It includes data ingestion, feature transformation, model inference, alert generation, and monitoring for drift and performance degradation.

## ML System Lifecycle

1. Data ingestion from network log sources
2. Feature engineering pipeline
3. Model training using anomaly detection
4. Model inference through API
5. Integration with monitoring dashboards
6. Continuous monitoring and model retraining

## Deployment Architecture

Model training environment
    ↓
Model registry
    ↓
Inference service (FastAPI)
    ↓
Security monitoring dashboard

## ML Pipeline Stages

Data Ingestion
Network log streams collected from security infrastructure.

Feature Engineering
Transform raw log data into behavioral features.

Model Training
Isolation Forest anomaly detection model.

Inference
Prediction API serves anomaly scores.

Monitoring
Model drift detection and alert tuning.

## Launch Plan

Phase 1 — Prototype
• validate anomaly detection model  
• evaluate detection accuracy  

Phase 2 — System Integration
• deploy model as API service  
• integrate feature pipeline  

Phase 3 — Production Deployment
• deploy monitoring and alerting  
• validate model performance on live data

## Key Risks

| Risk | Mitigation |
|-----|------------|
Data drift affecting model accuracy | implement monitoring pipeline |
Feature pipeline failure | add validation checks |
False positives triggering alerts | tune model thresholds |

## Example ML Workflow

A simple anomaly detection example is provided in:

notebooks/anomaly_detection_demo.ipynb

The notebook demonstrates:

• loading sample network logs  
• feature engineering  
• training an Isolation Forest model  
• detecting anomalous network activity

## Program Milestones

| Milestone | Owner | Target |
|----------|------|------|
| Requirements defined | Security Team | Week 2 |
| Data pipeline ready | Data Engineering | Week 4 |
| Model training complete | ML Team | Week 6 |
| API deployment | Platform Engineering | Week 8 |
| Production launch | TPM | Week 9 |

Pipeline overview:

Network Logs  
→ Streaming Layer (Kafka)  
→ Feature Engineering (Python/Spark)  
→ ML Model Service (Isolation Forest)  
→ Prediction API (FastAPI)  
→ Security Dashboard / SIEM  

## Program Artifacts
This repository includes TPM delivery artifacts:

• System architecture design  
• Deployment roadmap  
• Stakeholder map  
• Risk register  
• Launch success metrics  

## Program Timeline

| Phase | Duration | Outcome |
|------|------|------|
| Discovery | 2 weeks | Define requirements |
| Development | 4 weeks | Build ML model |
| Integration | 2 weeks | Connect monitoring systems |
| Launch | 1 week | Production deployment |

## Key Program Risks

| Risk | Impact | Mitigation |
|-----|-----|-----|
| Poor data quality | Reduced model accuracy | Data validation pipeline |
| Model drift | Degrading predictions | Scheduled retraining |
| Alert fatigue | Analysts ignore alerts | Threshold tuning |
| System latency | Slow detection | Scalable infrastructure |

## Production Readiness

The repository includes operational artifacts typically required for launching ML systems:

• Service level objectives (SLOs)  
• Model monitoring plan  
• Incident response playbook  
• Release rollout strategy

## Repository Structure

architecture/  
System design documentation.

program-management/  
Roadmap, risks, stakeholder mapping, execution plan.

data/  
Sample network log dataset.

notebooks/  
Example anomaly detection notebook.

src/  
Feature engineering and model training code.

## Skills Demonstrated

• Technical Program Management  
• Machine Learning System Lifecycle  
• Cross-team coordination  
• System architecture planning  
• Risk management

## Future Improvements

• Deploy model inference service using FastAPI  
• Add automated model retraining pipeline  
• Integrate Prometheus monitoring for model performance  
• Implement real-time streaming pipeline
