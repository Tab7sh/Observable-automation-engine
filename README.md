🚀 Dockerized Resume Portfolio

📌 Overview

This project demonstrates the fundamentals of containerization by deploying a static personal resume portfolio using Docker and Nginx (Alpine).

The goal was to package a simple HTML portfolio into a lightweight Docker image that can run consistently across any environment.

🛠 Tech Stack

Docker – Containerization

Nginx (Alpine) – Lightweight web server

HTML5 – Static frontend

📂 Project Structure
.
├── Dockerfile
└── index.html
🏗 How It Works

The Dockerfile uses the official nginx:alpine base image

Copies index.html into the Nginx web root directory

Exposes port 80 inside the container

Runs Nginx in the foreground

🚀 Run Locally
1️⃣ Clone Repository
git clone https://github.com/Tab7sh/dockerized-resume-portfolio.git
cd dockerized-resume-portfolio
2️⃣ Build Docker Image
docker build -t portfolio-app .
3️⃣ Run Container
docker run -d -p 8080:80 portfolio-app

Open in your browser:

http://localhost:8080
📊 Key Learning Outcomes

Understanding Docker image creation

Writing a basic Dockerfile

Port mapping (host:container)

Running and managing containers

Deploying static sites with Nginx

🎯 Purpose of This Project

This project was created to strengthen my understanding of:

Docker fundamentals

Container networking

Lightweight production-ready deployments
