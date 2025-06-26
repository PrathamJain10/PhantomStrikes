# PhantomStrikes - Security Research Toolkit
# Makefile for common development tasks

.PHONY: help install test clean docs lint format build docker

# Default target
help:
	@echo "PhantomStrikes - Security Research Toolkit"
	@echo "=========================================="
	@echo ""
	@echo "Available commands:"
	@echo "  install    - Install dependencies"
	@echo "  test       - Run tests"
	@echo "  lint       - Run linting checks"
	@echo "  format     - Format code with black"
	@echo "  docs       - Build documentation"
	@echo "  clean      - Clean build artifacts"
	@echo "  build      - Build package"
	@echo "  docker     - Build Docker image"
	@echo "  run        - Run PhantomStrikes"
	@echo "  help       - Show this help message"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	pip install -e .

# Run tests
test:
	@echo "Running tests..."
	python -m pytest tests/ -v --cov=src

# Run linting
lint:
	@echo "Running linting checks..."
	flake8 src/ tests/
	pylint src/

# Format code
format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/

# Build documentation
docs:
	@echo "Building documentation..."
	cd docs && make html

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Build package
build: clean
	@echo "Building package..."
	python setup.py sdist bdist_wheel

# Build Docker image
docker:
	@echo "Building Docker image..."
	docker build -t phantomstrikes .

# Run PhantomStrikes
run:
	@echo "Running PhantomStrikes..."
	python src/phantomstrikes.py --help

# Development setup
dev-setup: install
	@echo "Setting up development environment..."
	pip install -r requirements.txt
	pre-commit install

# Security check
security:
	@echo "Running security checks..."
	bandit -r src/
	safety check

# Full development workflow
dev: format lint test security
	@echo "Development workflow completed!"

# Release preparation
release: clean test build
	@echo "Release preparation completed!" 