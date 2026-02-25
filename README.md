🛸 INFRASTRUCTURE AUTOMATION ENGINE 🛸
📌 Project Overview
This repository hosts a fully Automated CI/CD Pipeline designed to eliminate manual deployment overhead. By leveraging GitHub Actions, every code push triggers an automated workflow that builds, tags, and ships Docker images directly to Docker Hub.

🛠 Tech Stack
🤖 Automation: GitHub Actions (CI/CD)

🐳 Containerization: Docker

📦 Registry: Docker Hub

🐍 Backend: Python Flask

⚡ Caching/Database: Redis

🏗 Pipeline Architecture
1️⃣ Continuous Integration (CI)
The pipeline is triggered automatically on every push to the main branch.

GitHub Actions provisions a virtual Ubuntu runner to execute the build process.

2️⃣ Build & Distribution
Secure Authentication: Uses GitHub Secrets to securely login to Docker Hub.

Image Orchestration: Builds the application image and applies the latest tag for production readiness.

Cloud Ship: Pushes the verified image to the tabish345 Docker Hub registry.

3️⃣ Security & Secrets
Zero Leak Policy: Sensitive credentials like DOCKERHUB_TOKEN are managed via encrypted secrets, ensuring no sensitive data is exposed in the source code.

📊 Deployment Proof
✅ Pipeline Status
This badge confirms that the automation engine is successfully validating and building the stack on every commit.

🐳 Docker Hub Integration
The automated image is now available for pull from the official registry.

Registry Link: View tabish345 on Docker Hub

🚀 How to Execute
Clone the Repository:
git clone https://github.com/Tab7sh/Infrastructure-automation-engine.git

Local Launch (Optional):
docker-compose up -d --build

Automated Trigger:
Modify any file and run git push to watch the Infrastructure Automation Engine push to tabish345/dynamic-portfolio!

💡 Key Learning Outcomes
Transitioned from manual container management to a Full Automation Workflow.

Gained expertise in GitHub Actions and Secrets Management.

Implemented a production-grade Cloud-Native Delivery Pipeline.
