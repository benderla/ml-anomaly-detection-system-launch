# ML Anomaly Detection System Launch (TPM Project)

## Overview
This project demonstrates how a Technical Program Manager can lead the deployment of a machine learning anomaly detection system into production.

The system identifies abnormal network activity using an Isolation Forest model and integrates with a security monitoring platform.

## Objectives
• Deploy a real-time anomaly detection pipeline  
• Integrate ML predictions with security monitoring tools  
• Establish program governance, risks, and launch metrics  

## System Overview

This project demonstrates how a Technical Program Manager could lead the deployment of a machine learning anomaly detection system into production.

The system processes network log data, extracts behavioral features, and applies an Isolation Forest model to detect anomalous activity.

Predictions are served through an API and integrated into a security monitoring dashboard for investigation by analysts.

## System Architecture
See: architecture/system_architecture.md

## Architecture

![System Architecture](diagrams/ml-system-architecture.png)

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

## Key Program Risks

| Risk | Impact | Mitigation |
|-----|-----|-----|
| Poor data quality | Reduced model accuracy | Data validation pipeline |
| Model drift | Degrading predictions | Scheduled retraining |
| Alert fatigue | Analysts ignore alerts | Threshold tuning |
| System latency | Slow detection | Scalable infrastructure |

## Program Timeline

| Phase | Duration | Outcome |
|------|------|------|
| Discovery | 2 weeks | Define requirements |
| Development | 4 weeks | Build ML model |
| Integration | 2 weeks | Connect monitoring systems |
| Launch | 1 week | Production deployment |

## Skills Demonstrated

• Technical Program Management  
• Machine Learning System Lifecycle  
• Cross-team coordination  
• System architecture planning  
• Risk management