# PhantomStrikes - Security Research Toolkit
# Dockerfile for containerized deployment

FROM python:3.9-slim

# Set metadata
LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="Advanced Security Research & Penetration Testing Toolkit"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    php \
    php-cli \
    php-curl \
    php-mbstring \
    php-xml \
    php-zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data/auth web/.server/www

# Set permissions
RUN chmod +x scripts/*.sh
RUN chmod +x src/phantomstrikes.py

# Create non-root user for security
RUN useradd -m -u 1000 phantomstrikes && \
    chown -R phantomstrikes:phantomstrikes /app

# Switch to non-root user
USER phantomstrikes

# Expose ports
EXPOSE 8080 9150

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Default command
CMD ["python", "src/phantomstrikes.py", "--help"] 