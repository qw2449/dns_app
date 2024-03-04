
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir Flask

EXPOSE 9090

CMD ["python", "fs.py"]
