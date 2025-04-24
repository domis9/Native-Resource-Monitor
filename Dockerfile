#Python image as base
FROM python:3.9-slim-buster
#Sets working directory in container /app
WORKDIR /app
#Copy requirements file to the directory /app
COPY requirements.txt .
#Run installation for packages
RUN pip3 install --no-cache-dir -r requirements.txt
#Copy application code
COPY . .
#Sets environment var for Flask
ENV FLASK_RUN_HOST=0.0.0.0
#Exposes port where Flask wil run
EXPOSE 5000
#Start flask app when container is run
CMD ["flask", "run"]