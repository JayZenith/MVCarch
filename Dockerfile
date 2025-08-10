FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# install deps
RUN pip install -r requirements.txt 

#copy application code
COPY . .

# expost port 
EXPOSE 5000

# configured to run run.py when container started 
CMD ["python", "run.py"]