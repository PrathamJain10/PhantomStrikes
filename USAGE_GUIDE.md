# PhantomStrikes - Usage Guide

## 🎯 Quick Start

### 1. **Installation**
```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Install dependencies
pip install -r requirements.txt
```

### 2. **Verify Installation**
```bash
# Test the launcher
python launch.py help

# Test the main tool
python launch.py dos --show-help
```

### 3. **Basic Usage**
```bash
# Launch DoS testing tool
python launch.py dos -t 192.168.1.100 -r 256

# Launch web server
python launch.py web -p 8080

# Run tests
python launch.py test
```

## 🚀 Available Commands

### **Launcher Commands**
| Command | Description | Example |
|---------|-------------|---------|
| `help` | Show help information | `python launch.py help` |
| `dos` | Launch DoS testing tool | `python launch.py dos -t target.com` |
| `web` | Launch web server | `python launch.py web -p 8080` |
| `phishing` | Launch phishing simulation | `python launch.py phishing` |
| `test` | Run test suite | `python launch.py test` |

### **DoS Tool Options**
| Option | Description | Default |
|--------|-------------|---------|
| `-t, --target` | Target hostname or IP | Required |
| `-r, --threads` | Number of threads | 256 |
| `-p, --port` | Target port | 80 |
| `-T, --tor` | Enable Tor anonymization | False |
| `--show-help` | Show DoS tool help | False |

### **Web Server Options**
| Option | Description | Default |
|--------|-------------|---------|
| `-p, --port` | Port to bind | 8080 |
| `--host` | Host to bind | 127.0.0.1 |

## 📁 Project Structure

```
PhantomStrikes/
├── 📁 src/                    # Core Python modules
│   ├── phantomstrikes.py      # Main DoS testing engine
│   ├── socks.py              # SOCKS proxy implementation
│   └── terminal.py           # Terminal UI utilities
├── 📁 web/                   # Web server components
│   ├── .server/              # Server infrastructure
│   └── .sites/               # Phishing site templates (40+)
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

## 🔧 Configuration

### **Configuration File**
The main configuration file is located at `config/phantomstrikes.conf`:

```ini
[DEFAULT]
default_threads = 256
default_port = 80
tor_enabled = false
log_level = INFO
privacy_mode = true
```

### **Environment Variables**
```bash
export PHANTOMSTRIKES_DEFAULT_THREADS=512
export PHANTOMSTRIKES_TOR_ENABLED=true
export PHANTOMSTRIKES_LOG_LEVEL=INFO
```

## 🛡️ Security Features

### **Privacy Protection**
- **Tor Integration**: Anonymous testing capabilities
- **SOCKS Proxy Support**: Advanced networking privacy
- **No Data Retention**: Educational use only

### **Safety Measures**
- **Rate Limiting**: Built-in protection against abuse
- **Target Validation**: Input sanitization and verification
- **Educational Focus**: Clear disclaimers and usage guidelines

## 📊 Performance

### **DoS Testing Performance**
- **Thread Management**: Up to 1000+ concurrent threads
- **Memory Efficiency**: Optimized for low resource usage
- **Network Throughput**: Configurable bandwidth utilization

### **Web Server Performance**
- **Response Time**: <100ms average response
- **Concurrent Users**: Support for 100+ simultaneous connections
- **Uptime**: 99.9% availability with proper configuration

## 🎯 Use Cases

### **Educational Purposes**
- **Security Awareness Training**: Demonstrates common attack vectors
- **Penetration Testing Practice**: Provides tools for ethical security testing
- **Research & Development**: Platform for security research and tool development
- **Defense Strategy Development**: Understanding attacks to build better defenses

### **Professional Use**
- **Security Research**: Academic and professional security testing
- **Penetration Testing**: Authorized security assessments
- **Educational Training**: Security awareness and training programs
- **Defense Development**: Understanding attacks to build better defenses

## 🚨 Important Notes

### **Legal Compliance**
- **Educational Use Only**: This toolkit is for learning and research
- **Authorization Required**: Only test systems you own or have permission to test
- **Legal Responsibility**: Users are responsible for compliance with laws
- **No Warranty**: Use at your own risk

### **Ethical Guidelines**
- **Always obtain proper authorization** before testing
- **Respect privacy and confidentiality**
- **Report vulnerabilities responsibly**
- **Follow responsible disclosure**

## 📚 Documentation

### **Available Documentation**
- [Installation Guide](docs/installation.md) - Detailed installation instructions
- [Quick Start Guide](docs/quickstart.md) - Get up and running quickly
- [Configuration Guide](docs/configuration.md) - Configure the toolkit
- [Security Best Practices](docs/security.md) - Security guidelines and best practices

### **Additional Resources**
- [Project Structure](PROJECT_STRUCTURE.md) - Detailed project structure
- [GitHub Repository](https://github.com/yourusername/PhantomStrikes) - Source code
- [Issues](https://github.com/yourusername/PhantomStrikes/issues) - Bug reports and feature requests

## 🔄 Development Workflow

### **Using Makefile**
```bash
# Install dependencies
make install

# Run tests
make test

# Format code
make format

# Run linting
make lint

# Build package
make build

# Clean build artifacts
make clean
```

### **Using Docker**
```bash
# Build image
docker build -t phantomstrikes .

# Run container
docker run -it phantomstrikes

# Use Docker Compose
docker-compose up -d
```

## 📞 Support

### **Getting Help**
- **Documentation**: Check the [docs/](docs/) directory
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Join our community discussions

### **Contact Information**
- **Project Maintainer**: [Your Name](mailto:your.email@example.com)
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)

---

**Remember**: This toolkit is for educational purposes only. Always use responsibly and legally! 