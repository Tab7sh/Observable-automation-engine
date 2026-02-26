🛸 OBSERVABLE AUTOMATION ENGINE 🛸
📌 PROJECT OVERVIEW
This repository represents a production-grade DevOps Ecosystem. It integrates a seamless GitHub Actions CI/CD Pipeline with a comprehensive Observability Stack. The engine not only automates the delivery of containerized microservices to Docker Hub but also provides real-time health metrics and proactive failure detection.

🛠 TECH STACK & TOOLS
🤖 CI/CD Automation: GitHub Actions

🐳 Containerization: Docker & Docker Compose

🔥 Metrics Collection: Prometheus

📈 Visualization: Grafana Dashboards

🦉 Resource Monitoring: Google cAdvisor

🐍 Backend: Python Flask with Redis Caching

🏗 INFRASTRUCTURE ARCHITECTURE
1️⃣ Continuous Delivery Pipeline
Every git push triggers a workflow that builds the latest Docker image.

Secured via GitHub Secrets, the image is automatically pushed to the tabish345 Docker Hub registry.

2️⃣ Real-Time Observability
Prometheus scrapes high-resolution metrics from the container environment every 15 seconds.

cAdvisor provides granular visibility into CPU, Memory, and Network throughput for all running services.

3️⃣ Proactive Alerting Logic
A custom Grafana Alerting system is implemented to ensure high availability.

Critical Rule: If the Portfolio service remains "Down" for more than 60 seconds, the system triggers a Firing status, alerting the administrator immediately.

📊 SYSTEM STATUS & PROOF
Live Dashboard: Accessible at localhost:3000.

Alert Status: Currently Normal (Verified via fault-injection testing).

Image Registry: View on Docker Hub.

🚀 HOW TO DEPLOY
Clone the Engine:

Bash
git clone https://github.com/Tab7sh/Observable-automation-engine.git
Launch the Stack:

PowerShell
docker-compose up -d
Verify Observability:
Visit localhost:9090 for Prometheus queries and localhost:8081 for raw container stats.

💡 KEY LEARNING OUTCOMES
Engineered a complete CI/CD/CO (Continuous Observability) lifecycle.

Implemented Infrastructure as Code (IaC) for monitoring and alerting.

Optimized system reliability through Proactive Fault Detection.
