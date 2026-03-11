# ML Anomaly Detection System Launch (TPM Project)

## Overview
This project demonstrates how a Technical Program Manager can lead the deployment of a machine learning anomaly detection system into production.

The system identifies abnormal network activity using an Isolation Forest model and integrates with a security monitoring platform.

## Objectives
• Deploy a real-time anomaly detection pipeline  
• Integrate ML predictions with security monitoring tools  
• Establish program governance, risks, and launch metrics  

## System Architecture
See: architecture/system_architecture.md

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

## Skills Demonstrated

• Technical Program Management  
• Machine Learning System Lifecycle  
• Cross-team coordination  
• System architecture planning  
• Risk management