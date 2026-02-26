🛸 OBSERVABLE AUTOMATION ENGINE 🛸
📌 PROJECT OVERVIEW
This repository represents a production-ready DevOps Ecosystem. It integrates a seamless GitHub Actions CI/CD Pipeline with a comprehensive Observability Stack and Global Cloud Edge Hosting. The engine automates the delivery of containerized services while providing real-time health metrics and proactive failure detection.

🌐 LIVE CLOUD DEPLOYMENT
The production frontend of this project is globally accessible via AWS S3 for 99.9% uptime and low-latency delivery.
🔗 Live Link: http://tabish-devops-portfolio-2026.s3-website.eu-north-1.amazonaws.com

🛠 TECH STACK & TOOLS
🤖 Automation: GitHub Actions (CI/CD)

📈 Observability: Prometheus & Grafana

🦉 Resource Tracking: Google cAdvisor

☁️ Infrastructure: AWS S3 (Static Website Hosting)

🐳 Containerization: Docker & Docker Compose

🏗 INFRASTRUCTURE ARCHITECTURE
1️⃣ Continuous Delivery (CI/CD)
Every code push triggers an automated build and push to the Docker Hub registry.

Secured via GitHub Secrets to ensure safe credential management.

2️⃣ Real-Time Observability
Prometheus scrapes metrics from the container environment every 15 seconds.

cAdvisor provides granular visibility into CPU, RAM, and Network utilization for all running services.

3️⃣ Proactive Alerting Logic
A custom Grafana Alerting system is implemented to monitor service health.

Critical Rule: If the Portfolio service count drops below 1 for more than 60 seconds, the system triggers a Firing alert.

4️⃣ Cloud Edge Hosting
The static frontend is deployed to an AWS S3 Bucket configured with public read access and static website hosting properties.

📊 SYSTEM STATUS PROOF
Live Monitoring: Dashboard active at localhost:3000.

Alert Status: Currently Normal (Successfully verified via fault-injection testing).

Prometheus Health: Scraping targets are 100% active.

🚀 HOW TO DEPLOY LOCALLY
Clone the Repository:

Bash
git clone https://github.com/Tab7sh/Observable-Automation-Engine.git
Launch the Stack:

PowerShell
docker-compose up -d
Access Monitoring:

Grafana: http://localhost:3000

cAdvisor: http://localhost:8081

💡 KEY LEARNING OUTCOMES
Engineered a complete CI/CD/CO (Continuous Observability) lifecycle.

Implemented Infrastructure as Code (IaC) for monitoring and cloud hosting.

Optimized system reliability through Proactive Fault Detection and Cloud Distribution.
