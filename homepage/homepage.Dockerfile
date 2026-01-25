FROM python:3.11-slim
WORKDIR /app
COPY homepage.py .
EXPOSE 8081
CMD ["python", "homepage.py"]
