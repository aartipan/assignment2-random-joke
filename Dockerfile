FROM python:3.11
WORKDIR /app
COPY requirements.txt .
COPY app.py .
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]