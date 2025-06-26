# Configuration Guide

## 🔧 Configuration Overview

PhantomStrikes can be configured through multiple methods: configuration files, environment variables, and command-line arguments.

## 📁 Configuration Files

### Main Configuration File

Create `config/phantomstrikes.conf`:

```ini
[DEFAULT]
# General settings
default_threads = 256
default_port = 80
tor_enabled = false
log_level = INFO
log_file = logs/phantomstrikes.log

# Network settings
timeout = 30
retry_count = 3
user_agent_rotation = true

# Security settings
rate_limit = 1000
max_connections = 100
privacy_mode = true

# Web server settings
web_port = 8080
web_host = 127.0.0.1
ssl_enabled = false
ssl_cert = certs/server.crt
ssl_key = certs/server.key

# Phishing simulation
template_path = web/.sites/
credential_log = data/auth/credentials.txt
ip_log = data/auth/ip.txt
```

### Environment-Specific Configs

#### Development Configuration (`config/dev.conf`)

```ini
[DEFAULT]
log_level = DEBUG
tor_enabled = false
web_port = 8080
privacy_mode = false
```

#### Production Configuration (`config/prod.conf`)

```ini
[DEFAULT]
log_level = WARNING
tor_enabled = true
web_port = 443
ssl_enabled = true
privacy_mode = true
rate_limit = 500
```

## 🌍 Environment Variables

### Core Variables

```bash
# General settings
export PHANTOMSTRIKES_DEFAULT_THREADS=512
export PHANTOMSTRIKES_DEFAULT_PORT=80
export PHANTOMSTRIKES_TOR_ENABLED=true
export PHANTOMSTRIKES_LOG_LEVEL=INFO

# Network settings
export PHANTOMSTRIKES_TIMEOUT=30
export PHANTOMSTRIKES_RETRY_COUNT=3
export PHANTOMSTRIKES_USER_AGENT_ROTATION=true

# Security settings
export PHANTOMSTRIKES_RATE_LIMIT=1000
export PHANTOMSTRIKES_MAX_CONNECTIONS=100
export PHANTOMSTRIKES_PRIVACY_MODE=true

# Web server settings
export PHANTOMSTRIKES_WEB_PORT=8080
export PHANTOMSTRIKES_WEB_HOST=127.0.0.1
export PHANTOMSTRIKES_SSL_ENABLED=false

# Paths
export PHANTOMSTRIKES_CONFIG_DIR=config/
export PHANTOMSTRIKES_LOG_DIR=logs/
export PHANTOMSTRIKES_DATA_DIR=data/
```

### Platform-Specific Variables

#### Windows

```cmd
set PHANTOMSTRIKES_DEFAULT_THREADS=256
set PHANTOMSTRIKES_TOR_ENABLED=false
set PHANTOMSTRIKES_LOG_LEVEL=INFO
```

#### macOS/Linux

```bash
export PHANTOMSTRIKES_DEFAULT_THREADS=256
export PHANTOMSTRIKES_TOR_ENABLED=false
export PHANTOMSTRIKES_LOG_LEVEL=INFO
```

## 🎛️ Command-Line Configuration

### Basic Options

```bash
# Thread configuration
python src/phantomstrikes.py -t target.com -r 512

# Port configuration
python src/phantomstrikes.py -t target.com -p 443

# Tor configuration
python src/phantomstrikes.py -t target.com -T

# Verbose output
python src/phantomstrikes.py -t target.com -v
```

### Advanced Options

```bash
# Custom user agent
python src/phantomstrikes.py -t target.com --user-agent "Custom Agent"

# Custom timeout
python src/phantomstrikes.py -t target.com --timeout 60

# Rate limiting
python src/phantomstrikes.py -t target.com --rate-limit 500

# Log file
python src/phantomstrikes.py -t target.com --log-file custom.log
```

## 🔐 Security Configuration

### Privacy Settings

```ini
[PRIVACY]
# Tor settings
tor_enabled = true
tor_port = 9050
tor_host = 127.0.0.1

# VPN settings
vpn_enabled = false
vpn_interface = tun0

# Data protection
encrypt_logs = true
clear_logs_on_exit = true
anonymize_ips = true
```

### Access Control

```ini
[ACCESS]
# User permissions
allowed_users = phantomstrikes,admin
restricted_commands = format,delete

# Network restrictions
allowed_networks = 192.168.1.0/24,10.0.0.0/8
blocked_networks = 0.0.0.0/0

# Time restrictions
allowed_hours = 9-17
allowed_days = monday-friday
```

## 🌐 Network Configuration

### Proxy Settings

```ini
[PROXY]
# SOCKS proxy
socks_enabled = true
socks_host = 127.0.0.1
socks_port = 1080
socks_type = SOCKS5

# HTTP proxy
http_enabled = false
http_host = proxy.company.com
http_port = 8080
http_auth = false
http_username = 
http_password = 
```

### SSL/TLS Configuration

```ini
[SSL]
# SSL settings
ssl_enabled = true
ssl_verify = true
ssl_cert_file = certs/client.crt
ssl_key_file = certs/client.key
ssl_ca_file = certs/ca.crt

# Cipher suites
ssl_ciphers = ECDHE-RSA-AES256-GCM-SHA384
ssl_protocols = TLSv1.2,TLSv1.3
```

## 📊 Logging Configuration

### Log Levels

```ini
[LOGGING]
# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
log_level = INFO
log_file = logs/phantomstrikes.log
log_format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
log_rotation = true
log_max_size = 10MB
log_backup_count = 5

# Console logging
console_enabled = true
console_level = INFO
console_format = %(levelname)s - %(message)s
```

### Log Categories

```ini
[LOGGING_CATEGORIES]
# Enable/disable specific log categories
network_logging = true
security_logging = true
performance_logging = true
debug_logging = false
```

## 🎯 Performance Configuration

### Threading Settings

```ini
[PERFORMANCE]
# Thread configuration
max_threads = 1000
thread_timeout = 30
thread_pool_size = 100

# Memory management
max_memory = 2GB
garbage_collection = true
gc_interval = 300

# Network optimization
connection_pool_size = 50
keep_alive = true
keep_alive_timeout = 60
```

### Resource Limits

```ini
[RESOURCES]
# CPU limits
max_cpu_percent = 80
cpu_affinity = 0,1,2,3

# Memory limits
max_memory_percent = 70
memory_warning_threshold = 80

# Network limits
max_bandwidth = 100MB
bandwidth_throttle = true
```

## 🔄 Configuration Management

### Configuration Validation

```bash
# Validate configuration
python -c "
import configparser
config = configparser.ConfigParser()
config.read('config/phantomstrikes.conf')
print('Configuration is valid')
"
```

### Configuration Backup

```bash
# Backup configuration
cp config/phantomstrikes.conf config/phantomstrikes.conf.backup

# Restore configuration
cp config/phantomstrikes.conf.backup config/phantomstrikes.conf
```

### Configuration Templates

Create template files for different environments:

```bash
# Development template
cp config/phantomstrikes.conf config/dev.template

# Production template
cp config/phantomstrikes.conf config/prod.template

# Testing template
cp config/phantomstrikes.conf config/test.template
```

## 🚀 Quick Configuration Examples

### Minimal Configuration

```ini
[DEFAULT]
default_threads = 256
tor_enabled = false
log_level = INFO
```

### Secure Configuration

```ini
[DEFAULT]
default_threads = 128
tor_enabled = true
log_level = WARNING
privacy_mode = true
rate_limit = 500
```

### High-Performance Configuration

```ini
[DEFAULT]
default_threads = 1000
tor_enabled = false
log_level = ERROR
max_connections = 200
connection_pool_size = 100
```

## 📋 Configuration Checklist

- [ ] Set appropriate thread limits
- [ ] Configure logging levels
- [ ] Enable privacy protection
- [ ] Set up network restrictions
- [ ] Configure SSL/TLS if needed
- [ ] Set up proxy settings
- [ ] Configure performance limits
- [ ] Test configuration
- [ ] Backup configuration files

---

**Note**: Always test your configuration in a safe environment before using in production. 