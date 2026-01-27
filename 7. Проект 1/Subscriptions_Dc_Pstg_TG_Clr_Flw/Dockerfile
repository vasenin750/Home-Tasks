FROM python:3.11-alpine

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    postgresql-client \
    netcat-openbsd \
    libffi-dev \
    curl \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

RUN mkdir -p /app/staticfiles

CMD ["/app/entrypoint.sh"]