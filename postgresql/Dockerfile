FROM python:3.14-slim

WORKDIR /app

#RUN apt-get update && apt-get install -y gcc python3-dev

COPY requirements.txt insert-data.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "insert-data.py"]