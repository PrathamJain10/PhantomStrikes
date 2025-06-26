# Installation Guide

## Prerequisites

Before installing PhantomStrikes, ensure you have the following prerequisites:

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.7 or higher
- **PHP**: 7.4+ (for web components)
- **Git**: Latest version
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 2GB free space

### Optional Dependencies
- **Tor Browser**: For anonymization features
- **Docker**: For containerized deployment
- **Virtual Environment**: Python venv or conda

## Installation Methods

### Method 1: Quick Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python src/phantomstrikes.py --help
```

### Method 2: Virtual Environment Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Method 3: Docker Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Build Docker image
docker build -t phantomstrikes .

# Run container
docker run -it phantomstrikes
```

### Method 4: Docker Compose (Full Stack)

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Start all services
docker-compose up -d

# Start with Tor support
docker-compose --profile tor up -d

# Start with web server
docker-compose --profile web up -d
```

## Platform-Specific Instructions

### Windows Installation

1. **Install Python 3.9+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Ensure "Add Python to PATH" is checked

2. **Install Git**
   - Download from [git-scm.com](https://git-scm.com/download/win)

3. **Install PHP** (for web components)
   - Download from [windows.php.net](https://windows.php.net/download/)
   - Add PHP to system PATH

4. **Run Installation**
   ```cmd
   git clone https://github.com/yourusername/PhantomStrikes.git
   cd PhantomStrikes
   pip install -r requirements.txt
   ```

### macOS Installation

1. **Install Homebrew** (if not installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Dependencies**
   ```bash
   brew install python@3.9 git php
   ```

3. **Run Installation**
   ```bash
   git clone https://github.com/yourusername/PhantomStrikes.git
   cd PhantomStrikes
   pip3 install -r requirements.txt
   ```

### Linux Installation (Ubuntu/Debian)

1. **Update System**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Dependencies**
   ```bash
   sudo apt install python3 python3-pip python3-venv git php php-cli php-curl php-mbstring php-xml php-zip curl wget unzip -y
   ```

3. **Run Installation**
   ```bash
   git clone https://github.com/yourusername/PhantomStrikes.git
   cd PhantomStrikes
   pip3 install -r requirements.txt
   ```

## Verification

After installation, verify that everything is working:

```bash
# Test Python modules
python -c "import phantomstrikes, socks, terminal; print('All modules imported successfully!')"

# Test main application
python src/phantomstrikes.py --help

# Run tests
python -m pytest tests/ -v

# Test web server (if PHP is installed)
cd web/.server/www
php -S localhost:8080
```

## Troubleshooting

### Common Issues

1. **Python Import Errors**
   ```bash
   # Solution: Install missing dependencies
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Permission Errors**
   ```bash
   # Solution: Use virtual environment or fix permissions
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **PHP Not Found**
   ```bash
   # Solution: Install PHP or use Docker
   # Ubuntu/Debian:
   sudo apt install php php-cli
   # macOS:
   brew install php
   ```

4. **Docker Issues**
   ```bash
   # Solution: Ensure Docker is running
   docker --version
   docker-compose --version
   ```

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/yourusername/PhantomStrikes/issues)
2. Review the [Troubleshooting Guide](../docs/troubleshooting.md)
3. Create a new issue with detailed error information

## Next Steps

After successful installation:

1. Read the [Quick Start Guide](quickstart.md)
2. Review the [Configuration Guide](configuration.md)
3. Explore the [User Guides](user-guides.md)
4. Check out the [Security Best Practices](security.md)

---

**Note**: This toolkit is for educational purposes only. Always use responsibly and legally. 