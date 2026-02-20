FROM python:3.11-slim

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend
COPY backend/ ./backend/

# Copy frontend
COPY frontend/ ./frontend/

# Environment
ENV NEXUS_TOKEN=nexus-secret-2026
ENV DATABASE_URL=sqlite:///./nexus.db

# Expose port
EXPOSE 3334

# Run
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "3334"]
