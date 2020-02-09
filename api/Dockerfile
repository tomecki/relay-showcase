FROM python:3.8.1

WORKDIR /app_config
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 7000
VOLUME "/app"
WORKDIR "/app"
CMD ["uvicorn", "run:app", "--port", "7000", "--host", "0.0.0.0", "--reload"]