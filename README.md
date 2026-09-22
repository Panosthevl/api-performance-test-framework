# Advanced API Automation & Performance Testing Framework

A hybrid backend validation framework engineered to ensure functional correctness and infrastructure resilience under load. Built from scratch using **Python (Pytest & Playwright APIRequestContext)** for low-latency functional endpoint verification and **k6 (JavaScript)** for load profiling, fully orchestrated via **GitHub Actions CI/CD workflows**.

## 🚀 Key Architectural Features
* **Functional API Automation:** Utilizes Playwright's headless `APIRequestContext` layer to perform fast HTTP request/response validation (GET, POST, DELETE) with structural JSON schema and response status parsing.
* **Load Profiling & Stress Testing:** Implements Grafana's **k6** engine to simulate concurrent Virtual Users (VUs) using dynamic ramping curves (Up/Peak/Down load phases).
* **Automated Quality Gates:** Configured continuous integration workflows with cross-job dependencies (`needs: api-testing`), automatically blocking load testing jobs if core functional endpoints fail.
* **Performance Thresholds (SLAs):** Enforces strict reliability gates at the pipeline level, failing the build automatically if error rates exceed 2% or 95th-percentile response time (`p95`) surpasses the target service boundary.

## Repository Structure
```text
├── .github/workflows/
│   └── ci-cd-pipeline.yml  
├── api_tests/
│   ├── conftest.py         
│   └── test_reqres_api.py  
└── performance_tests/
    └── load_test.js     
```

##  Local Execution

### 1. Functional API Tests (Python)
Ensure dependencies are installed via `pip install -r requirements.txt`, then run:
```bash
pytest api_tests/
```

### 2. Performance & Load Tests (k6)
Ensure the k6 CLI is available on your machine, then execute the load curve profile:
```bash
k6 run performance_tests/load_test.js
```
