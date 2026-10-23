from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Serving a styled HTML page directly from Python
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TYCSE DevOps Pipeline</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; text-align: center; padding: 50px; }
            .container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); display: inline-block; max-width: 600px; }
            h1 { color: #0056b3; margin-bottom: 10px; }
            .badge { background-color: #28a745; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold; font-size: 0.9em; }
            .details { text-align: left; margin-top: 20px; line-height: 1.6; }
            hr { border: 0; height: 1px; background: #ddd; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Pipeline Automated Deployment</h1>
            <span class="badge">Status: Online & Running</span>
            
            <div class="details">
                <p><strong>Assignment:</strong> TYCSE Cloud Computing and DevOps (CCA 2)</p>
                <p><strong>Student:</strong> Tejas Jadhav</p>
                <p><strong>Roll Number:</strong> 63 | <strong>PRN:</strong> 1272250848</p>
                <hr>
                <p>✅ Code pulled from GitHub</p>
                <p>✅ Docker Image Built & Pushed to Registry</p>
                <p>✅ Deployed successfully on Minikube Kubernetes</p>
            </div>
            
            <p style="margin-top: 20px; font-size: 0.8em; color: #777;">Version 1.0 (Ready for GitHub update demo)</p>
        </div>
    </body>
    </html>
    """
    return html_content

@app.route('/health')
def health_check():
    # A standard DevOps health check endpoint
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "student": "Tejas Jadhav",
        "app_version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)