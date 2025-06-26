# PhantomStrikes 🔥

> **Advanced Security Research & Penetration Testing Toolkit**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)
[![Educational](https://img.shields.io/badge/Purpose-Educational-orange.svg)](https://github.com/yourusername/PhantomStrikes)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Security Features](#security-features)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## 🎯 Overview

PhantomStrikes is a comprehensive security research toolkit designed for educational penetration testing, security awareness training, and vulnerability assessment. This project demonstrates various attack vectors and security concepts to help security professionals understand and defend against real-world threats.

### 🎓 Educational Purpose
- **Security Awareness Training**: Demonstrates common attack vectors
- **Penetration Testing Practice**: Provides tools for ethical security testing
- **Research & Development**: Platform for security research and tool development
- **Defense Strategy Development**: Understanding attacks to build better defenses

## ✨ Features

### 🔧 Core Components

#### 1. **DoS Testing Module**
- **Slow POST DoS Tool**: Multi-threaded denial-of-service testing
- **Tor Anonymization**: Built-in privacy protection
- **Configurable Parameters**: Thread count, target specification, port selection
- **Real-time Monitoring**: Live attack statistics and progress tracking

#### 2. **Phishing Simulation Platform**
- **40+ Site Templates**: Realistic replicas of popular services
- **Mobile Responsive**: Cross-platform compatibility
- **Credential Harvesting**: Educational demonstration of data collection
- **IP Logging**: Visitor tracking and analytics

#### 3. **Web Server Infrastructure**
- **PHP Backend**: Server-side processing and data handling
- **Tunneling Support**: Cloudflare and LocalTunnel integration
- **Automated Deployment**: One-click setup and configuration

#### 4. **Network Security Tools**
- **SOCKS Proxy Support**: Advanced networking capabilities
- **Terminal Interface**: Rich CLI with color-coded output
- **Cross-platform**: Windows, Linux, macOS compatibility

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Git

### 1. Clone and Install
```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Installation
```bash
# Test the main application
python src/phantomstrikes.py --help

# Or use the launcher
python launch.py help
```

### 3. Basic Usage
```bash
# Launch DoS testing tool
python launch.py dos -t 192.168.1.100 -r 256

# Launch web server
python launch.py web -p 8080

# Run tests
python launch.py test
```

## 🏗️ Architecture

```
PhantomStrikes/
├── 📁 src/                    # Core Python modules
│   ├── phantomstrikes.py      # Main DoS testing engine
│   ├── socks.py              # SOCKS proxy implementation
│   └── terminal.py           # Terminal UI utilities
├── 📁 web/                   # Web server components
│   ├── .server/              # Server infrastructure
│   └── .sites/               # Phishing site templates
├── 📁 scripts/               # Automation and deployment
├── 📁 data/                  # Configuration and logs
├── 📁 config/                # Configuration files
├── 📁 tests/                 # Test suite
├── 📁 docs/                  # Documentation
├── 📄 launch.py              # Easy launcher script
├── 📄 requirements.txt       # Python dependencies
├── 📄 setup.py              # Python package setup
├── 📄 Makefile              # Development tasks
├── 📄 Dockerfile            # Container configuration
└── 📄 docker-compose.yml    # Multi-container setup
```

## 🚀 Installation

### Quick Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python src/phantomstrikes.py --help
```

### Virtual Environment Installation

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

### Docker Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Build Docker image
docker build -t phantomstrikes .

# Run container
docker run -it phantomstrikes
```

### Docker Compose (Full Stack)

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

## 📖 Usage

### Using the Launcher (Recommended)

```bash
# Show help
python launch.py help

# Launch DoS testing tool
python launch.py dos -t target.com -r 256

# Launch web server
python launch.py web -p 8080

# Launch phishing simulation
python launch.py phishing

# Run tests
python launch.py test
```

### Direct Usage

#### DoS Testing Module

```bash
# Basic usage
python src/phantomstrikes.py -t <target> -r <threads>

# With Tor anonymization
python src/phantomstrikes.py -t 192.168.1.100 -r 256 -T

# Custom port
python src/phantomstrikes.py -t example.com -p 8080 -r 128
```

**Parameters:**
- `-t, --target`: Target hostname or IP address
- `-r, --threads`: Number of threads (default: 256)
- `-p, --port`: Target port (default: 80)
- `-T, --tor`: Enable Tor anonymization
- `-h, --help`: Show help message

#### Web Server & Phishing Simulation

```bash
# Start the web server
cd scripts
./Phantom.sh

# Or manually start PHP server
cd web/.server/www
php -S localhost:8080
```

### Advanced Configuration

```bash
# Custom configuration
python src/phantomstrikes.py \
  --target example.com \
  --threads 512 \
  --port 443 \
  --tor \
  --timeout 30
```

## 🛠️ Project Structure

### Core Modules (`src/`)

| File | Purpose | Key Features |
|------|---------|--------------|
| `phantomstrikes.py` | Main DoS testing engine | Multi-threading, Tor support, real-time monitoring |
| `socks.py` | SOCKS proxy implementation | SOCKS4/5 support, HTTP tunneling |
| `terminal.py` | Terminal UI utilities | Color output, progress bars, formatting |

### Web Components (`web/`)

| Directory | Purpose | Contents |
|-----------|---------|----------|
| `.server/` | Web server infrastructure | PHP backend, tunneling tools |
| `.sites/` | Phishing templates | 40+ realistic site replicas |

### Automation (`scripts/`)

| Script | Purpose | Features |
|--------|---------|----------|
| `Phantom.sh` | Main automation script | One-click deployment, dependency management |
| `launch.sh` | Quick launcher | Simplified startup process |
| `run-docker.sh` | Docker automation | Containerized deployment |

## 🛡️ Security Features

### Privacy Protection
- **Tor Integration**: Anonymous testing capabilities
- **SOCKS Proxy Support**: Advanced networking privacy
- **No Data Retention**: Educational use only

### Safety Measures
- **Rate Limiting**: Built-in protection against abuse
- **Target Validation**: Input sanitization and verification
- **Educational Focus**: Clear disclaimers and usage guidelines

### Compliance
- **MIT License**: Open source and permissive
- **Educational Purpose**: Clear usage restrictions
- **Responsible Disclosure**: Ethical usage guidelines

## 🔧 Technologies Used

### Backend Technologies
- **Python 3.7+**: Core application logic
- **PHP 7.4+**: Web server backend
- **SOCKS Protocol**: Proxy networking
- **Tor Network**: Anonymization

### Frontend Technologies
- **HTML5/CSS3**: Responsive web interfaces
- **JavaScript**: Dynamic content and interactions
- **Bootstrap**: Mobile-first design framework

### Infrastructure
- **Docker**: Containerized deployment
- **Cloudflare**: Tunneling and CDN
- **LocalTunnel**: Local development tunneling

## 📊 Performance Metrics

### DoS Testing Performance
- **Thread Management**: Up to 1000+ concurrent threads
- **Memory Efficiency**: Optimized for low resource usage
- **Network Throughput**: Configurable bandwidth utilization

### Web Server Performance
- **Response Time**: <100ms average response
- **Concurrent Users**: Support for 100+ simultaneous connections
- **Uptime**: 99.9% availability with proper configuration


## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## ⚠️ Disclaimer

**IMPORTANT: Educational Use Only**

This software is developed and distributed for **educational purposes only**. The authors and contributors are not responsible for any misuse of this software.

## 📚 Additional Documentation

For detailed documentation, see the [docs/](docs/) directory:

- [Installation Guide](docs/installation.md) - Detailed installation instructions
- [Quick Start Guide](docs/quickstart.md) - Get up and running quickly
- [Configuration Guide](docs/configuration.md) - Configure the toolkit
- [Security Best Practices](docs/security.md) - Security guidelines and best practices

---
