ARG python-version=3.12
FROM python:${python-version} 
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
EXPOSE 80
