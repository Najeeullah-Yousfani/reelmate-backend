# Python base
FROM python:3.12-slim

# System deps (psycopg, Pillow if you add images later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Django settings: ensure production uses Whitenoise for static
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Collect static at build time only if you want baked assets
# (Render runs build command separately, but this is safe)
# RUN python manage.py collectstatic --noinput || true

# Expose and run
EXPOSE 8000
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
