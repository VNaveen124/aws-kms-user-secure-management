# aws-kms-user-secure-management
🔧 Tech Stack
Backend: Python (Flask/FastAPI)

Database: MySQL (RDS or local)

Encryption: AWS KMS

Infrastructure as Code: Terraform

CI/CD: GitHub Actions

Cloud: AWS (KMS + RDS + EC2)


🧱 Project Structure
css
Copy
Edit
secure-user-management/
├── app/
│   ├── main.py
│   ├── kms_utils.py
│   └── requirements.txt
├── db/
│   └── init.sql
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── .github/workflows/
│   └── ci-cd.yml
├── .env.example
└── README.md
