# Quick Start Guide

Get up and running with PhantomStrikes in under 5 minutes!

## 🚀 Quick Setup

### Step 1: Clone and Install

```bash
# Clone the repository
git clone https://github.com/yourusername/PhantomStrikes.git
cd PhantomStrikes

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Verify Installation

```bash
# Test the main application
python src/phantomstrikes.py --help
```

You should see the help output with available options.

## 🎯 Basic Usage

### DoS Testing Module

```bash
# Basic DoS test (replace with your target)
python src/phantomstrikes.py -t 192.168.1.100 -r 128

# With Tor anonymization
python src/phantomstrikes.py -t example.com -r 256 -T

# Custom port and threads
python src/phantomstrikes.py -t target.com -p 8080 -r 512
```

### Web Server & Phishing Simulation

```bash
# Start the web server
cd scripts
./Phantom.sh

# Or manually start PHP server
cd web/.server/www
php -S localhost:8080
```

## 📋 Common Commands

| Command | Description | Example |
|---------|-------------|---------|
| `--help` | Show help | `python src/phantomstrikes.py --help` |
| `-t` | Target host | `-t 192.168.1.100` |
| `-r` | Number of threads | `-r 256` |
| `-p` | Target port | `-p 80` |
| `-T` | Enable Tor | `-T` |

## 🔧 Configuration

### Basic Configuration

Create a simple configuration file:

```bash
# Create config directory
mkdir -p config

# Create basic config
cat > config/phantomstrikes.conf << EOF
[DEFAULT]
default_threads = 256
default_port = 80
tor_enabled = false
log_level = INFO
EOF
```

### Environment Variables

```bash
# Set environment variables
export PHANTOMSTRIKES_TOR_ENABLED=true
export PHANTOMSTRIKES_DEFAULT_THREADS=512
export PHANTOMSTRIKES_LOG_LEVEL=DEBUG
```

## 🛡️ Security Considerations

### Before Running

1. **Ensure Legal Compliance**
   - Only test systems you own or have permission to test
   - Check local laws and regulations
   - Obtain written authorization if required

2. **Network Safety**
   - Use isolated test environments
   - Avoid testing production systems
   - Monitor network impact

3. **Privacy Protection**
   - Enable Tor for anonymous testing
   - Use VPN if available
   - Clear logs after testing

## 📊 Monitoring and Logs

### View Real-time Output

```bash
# Run with verbose output
python src/phantomstrikes.py -t target.com -r 128 -v

# Monitor logs
tail -f logs/phantomstrikes.log
```

### Check Performance

```bash
# Monitor system resources
htop  # or top on some systems

# Check network usage
iftop  # or nethogs
```

## 🚨 Emergency Stop

To stop all operations immediately:

```bash
# Press Ctrl+C in the terminal
# Or kill the process
pkill -f phantomstrikes
```

## 📈 Next Steps

After getting familiar with basic usage:

1. **Read the Full Documentation**
   - [DoS Testing Guide](dos-testing.md)
   - [Phishing Simulation Guide](phishing-simulation.md)
   - [Web Server Setup](web-server.md)

2. **Explore Advanced Features**
   - Custom user agents
   - Proxy configurations
   - Advanced tunneling

3. **Join the Community**
   - [GitHub Discussions](https://github.com/yourusername/PhantomStrikes/discussions)
   - [Issue Tracker](https://github.com/yourusername/PhantomStrikes/issues)

## ❓ Need Help?

### Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | `pip install -r requirements.txt` |
| Permission denied | Use virtual environment |
| Tor not working | Check Tor installation |
| PHP errors | Install PHP or use Docker |

### Getting Support

1. **Check Documentation**: Review relevant guides
2. **Search Issues**: Look for similar problems
3. **Create Issue**: Provide detailed error information

## ⚠️ Important Notes

- **Educational Use Only**: This toolkit is for learning and research
- **Legal Compliance**: Always follow applicable laws
- **Responsible Usage**: Use ethically and responsibly
- **No Warranty**: Use at your own risk

---

**Ready to start?** Run `python src/phantomstrikes.py --help` to see all available options! 