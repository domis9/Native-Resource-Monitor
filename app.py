#monitoring cpu and memory metrics
#created a python app using Flask, dockerized/deployed it as an image, push an image to ECR(boto3) repo
#use EKS to deploy container in the form of a kubernetes cluster

import psutil
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = ""
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High cpu or memory usage detected"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
