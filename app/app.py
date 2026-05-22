from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps CI/CD Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #6CDAE7;
                margin: 0;
                padding: 0;
            }

            .container {
                width: 80%;
                margin: 50px auto;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }

            h1 {
                color: #2c3e50;
                text-align: center;
            }

            h2 {
                color: #34495e;
                margin-top: 30px;
            }

            p {
                color: #555;
                line-height: 1.6;
            }

            .highlight {
                color: #2980b9;
                font-weight: bold;
            }

            footer {
                margin-top: 40px;
                text-align: center;
                color: gray;
            }
        </style>
    </head>

    <body>

        <div class="container">
            <h1>DevOps CI/CD Automation Project</h1>

            <p>
                This project demonstrates a complete <span class="highlight">CI/CD pipeline</span>
                using Flask, GitHub, CircleCI, and Ansible.
            </p>

            <h2>What is CircleCI?</h2>
            <p>
                CircleCI is a cloud-based Continuous Integration and Continuous Deployment (CI/CD)
                platform that automatically builds, tests, and deploys applications whenever code
                is pushed to GitHub.
            </p>

            <h2>What is Ansible?</h2>
            <p>
                Ansible is an automation tool used for configuration management and application
                deployment. It automates deployment tasks using playbooks.
            </p>

            <h2>Project Workflow</h2>
            <p>
                Developer pushes code to GitHub → CircleCI triggers pipeline →
                Dependencies are installed → Flask application is tested →
                Ansible automates deployment.
            </p>

            <footer>
                DevOps Project using Flask + CircleCI + Ansible
            </footer>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)