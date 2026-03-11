# ML Anomaly Detection System Launch (TPM Project)

## Overview
This project demonstrates how a Technical Program Manager can lead the deployment of a machine learning anomaly detection system into production.

The system identifies abnormal network activity using an Isolation Forest model and integrates with a security monitoring platform.

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

## System Architecture
See: architecture/system_architecture.md

The system ingests network logs, transforms them into behavioral features, 
applies an Isolation Forest anomaly detection model, and surfaces alerts 
through a monitoring dashboard.

## Architecture

![System Architecture](diagrams/ml-system-architecture.png)

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