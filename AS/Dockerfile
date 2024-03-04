
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY authoritative_server.py .

COPY dns_records.json . || true

EXPOSE 53533/udp

CMD ["python", "as.py"]
