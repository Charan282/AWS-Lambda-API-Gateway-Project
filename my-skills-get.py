import json
def lambda_handler(event, context):
    body = """ Programming Languages: Python, R, Matlab, HTML, CSS, JavaScript
            Big Data and Distributed Computing : Databricks, Apache Spark, Delta Lake
            DevOps Tools:  Jenkins, Docker, Kubernetes, Terraform, Ansible
            Data Science: Machine Learning, Pandas, NumPy, Sklearn, Pytorch, Tensorflow
            Data Visualization Tools: PowerBI, Tableau
            Cloud Technologies: Amazon Web Services (AWS), Azure
            Database Management:  MySQL, PostgreSQL, SQL
            Operating Systems: Windows, Linux
            Software Tools: Microsoft Office, Google Workspace
            Version Control:  Git, GitHub
            Methodologies: DevOps Practices (CI/CD, IaC, Automation)"""
    statusCode = 200
    return {
        'statusCode': statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
