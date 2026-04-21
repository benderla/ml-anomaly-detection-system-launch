# ML Anomaly Detection System Launch

This project outlines what it takes to launch an anomaly detection system from concept to production, focusing on execution challenges, tradeoffs, and operational decisions.

This is not just a system design. It reflects the realities of launching ML systems where requirements evolve, data is imperfect, and decisions have real consequences.

This project focuses on operational ownership of ML systems after deployment, not just model performance.

---

## What Makes This Hard

Launching an ML system is not just about building a model.

Key challenges include:

- unclear problem definition (what counts as an anomaly?)
- inconsistent or incomplete data
- lack of labeled training data
- changing requirements from stakeholders
- balancing model accuracy vs operational cost
- deciding how to handle false positives

These challenges require continuous tradeoffs, not just technical implementation.

---

## Execution Approach

This system was approached in phases rather than a single end-to-end build.

### Phase 1: Define the Problem

- identify what constitutes anomalous behavior  
- align with stakeholders on acceptable false positives  
- determine what data is available vs missing  

Challenge:
- definitions of “anomaly” varied across use cases  

---

### Phase 2: Data and Feature Strategy

- assess data quality and gaps  
- identify key features for anomaly detection  
- establish baseline distributions  

Challenge:
- data was inconsistent and required normalization  

---

### Phase 3: Model Development

- implement anomaly detection approach (Isolation Forest)  
- generate anomaly scores  
- tune thresholds based on validation data  

Challenge:
- no clear labeled dataset → required indirect evaluation  

---

### Phase 4: Deployment Strategy

- expose model via API  
- define how predictions are consumed  
- determine latency and scalability requirements  

Challenge:
- balancing real-time vs batch processing  

---

### Phase 5: Monitoring and Iteration

- track input distributions and model outputs  
- detect drift and degradation  
- define response actions  

Challenge:
- monitoring signals are indirect without immediate labels  

---

## Key Tradeoffs

- precision vs recall  
  - higher recall increases false positives  
  - higher precision risks missing anomalies  

- real-time vs batch processing  
  - real-time = faster detection, higher cost  
  - batch = lower cost, delayed response  

- model complexity vs maintainability  
  - complex models may perform better  
  - simpler models are easier to operate and debug  

---

## What I Would Do Differently

- invest earlier in data validation and schema enforcement  
- define success metrics more clearly upfront  
- build monitoring earlier in the lifecycle  
- align stakeholders sooner on acceptable error rates  

These changes would reduce rework and improve system reliability.

---

## Architecture

![System Architecture](diagrams/ml-system-architecture.png)

High-level flow:

Network Logs  
→ Data Ingestion  
→ Feature Engineering  
→ Isolation Forest Model  
→ Inference Service  
→ Alerting / Dashboard  

---

## Launch Plan

Phase 1 — Prototype  
- validate anomaly detection model  
- evaluate detection behavior  

Phase 2 — System Integration  
- deploy model as API service  
- integrate feature pipeline  

Phase 3 — Production Deployment  
- deploy monitoring and alerting  
- validate performance on live data  

---

## Program Milestones

| Milestone | Owner | Target |
|----------|------|------|
| Requirements defined | Security Team | Week 2 |
| Data pipeline ready | Data Engineering | Week 4 |
| Model training complete | ML Team | Week 6 |
| API deployment | Platform Engineering | Week 8 |
| Production launch | TPM | Week 9 |

---

## Key Risks

| Risk | Impact | Mitigation |
|-----|-----|-----|
| Poor data quality | Reduced model accuracy | Data validation pipeline |
| Model drift | Degrading predictions | Monitoring and retraining |
| False positives | Alert fatigue | Threshold tuning |
| System latency | Slow detection | Scalable infrastructure |

---

## Repository Structure

- `architecture/` — system design documentation  
- `program-management/` — roadmap, risks, execution planning  
- `data/` — sample dataset  
- `notebooks/` — anomaly detection demo  
- `src/` — feature engineering and model logic  

---

## Future Improvements

- deploy inference service using FastAPI  
- add automated retraining pipeline  
- integrate real-time monitoring  
- improve data validation and schema enforcement  

---

This project demonstrates how launching ML systems requires balancing technical design with operational decision-making and execution discipline.