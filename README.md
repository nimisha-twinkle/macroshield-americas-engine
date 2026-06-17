# MacroShield Américas — Synthetic AI Engine

Privacy-preserving synthetic AI engine for infrastructure risk simulation and human-in-the-loop emergency response workflows built for the USAII Global AI Hackathon 2026.

---

## Overview

MacroShield Américas is a graduate-level socio-technical safety platform designed to simulate infrastructure anomalies without exposing real-world civilian data.

The platform uses:
- Synthetic telemetry generation
- Machine learning clustering
- Human-in-the-loop authorization
- Responsible AI safeguards

to model crisis-response workflows while maintaining strict privacy compliance.

---

## Core Features

- Generative synthetic crisis telemetry engine
- KMeans clustering-based anomaly detection
- Nominal vs Critical risk classification
- P1/P2 mitigation recommendation system
- Human-in-the-loop deployment constraint gate
- Zero live PII ingestion

---

## AI Architecture

### Layer 1 — Synthetic Generation Backend
Generates anonymized synthetic telemetry logs representing infrastructure stress conditions.

### Layer 2 — ML Processing Layer
Uses unsupervised KMeans clustering to isolate critical anomaly nodes from nominal operational patterns.

### Layer 3 — State-Driven Dashboard Layer
Maps anomaly severity and mitigation recommendations onto a reactive operational dashboard interface.

---

## Responsible AI Principles

MacroShield Américas does not ingest real civilian data, live tracking metrics, or personally identifiable information (PII).

All operational analysis occurs within a synthetic simulation environment with explicit human approval requirements before any deployment action.

---

## Human-in-the-Loop Constraint

The platform acts strictly as an advisory system.

No mitigation workflow can execute unless a human operator manually authorizes deployment through the Module 04 approval gateway.

---

## Installation

```bash
pip install -r requirements.txt