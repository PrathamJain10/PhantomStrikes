# PhantomStrikes - Project Structure

## 📁 Complete Directory Structure

```
PhantomStrikes/
├── 📁 src/                          # Core Python source code
│   ├── phantomstrikes.py            # Main DoS testing engine
│   ├── socks.py                     # SOCKS proxy implementation
│   └── terminal.py                  # Terminal UI utilities
│
├── 📁 web/                          # Web server components
│   ├── 📁 .server/                  # Server infrastructure
│   │   ├── 📁 www/                  # Web server files
│   │   │   ├── index.php            # Main entry point
│   │   │   ├── login.php            # Credential processing
│   │   │   ├── ip.php               # IP logging
│   │   │   ├── login.html           # Login form
│   │   │   ├── mobile.html          # Mobile interface
│   │   │   ├── script.js            # JavaScript functionality
│   │   │   ├── style.css            # Styling
│   │   │   └── README.md            # Web server documentation
│   │   ├── cloudflared              # Cloudflare tunneling binary
│   │   └── loclx                    # LocalTunnel binary
│   │
│   └── 📁 .sites/                   # Phishing site templates (40+ sites)
│       ├── 📁 facebook/             # Facebook phishing template
│       ├── 📁 instagram/            # Instagram phishing template
│       ├── 📁 google/               # Google phishing template
│       ├── 📁 microsoft/            # Microsoft phishing template
│       ├── 📁 paypal/               # PayPal phishing template
│       ├── 📁 netflix/              # Netflix phishing template
│       ├── 📁 spotify/              # Spotify phishing template
│       ├── 📁 twitter/              # Twitter phishing template
│       ├── 📁 linkedin/             # LinkedIn phishing template
│       ├── 📁 github/               # GitHub phishing template
│       ├── 📁 steam/                # Steam phishing template
│       ├── 📁 xbox/                 # Xbox phishing template
│       ├── 📁 playstation/          # PlayStation phishing template
│       ├── 📁 discord/              # Discord phishing template
│       ├── 📁 snapchat/             # Snapchat phishing template
│       ├── 📁 tiktok/               # TikTok phishing template
│       ├── 📁 reddit/               # Reddit phishing template
│       ├── 📁 pinterest/            # Pinterest phishing template
│       ├── 📁 ebay/                 # eBay phishing template
│       ├── 📁 dropbox/              # Dropbox phishing template
│       ├── 📁 adobe/                # Adobe phishing template
│       ├── 📁 protonmail/           # ProtonMail phishing template
│       ├── 📁 yahoo/                # Yahoo phishing template
│       ├── 📁 yandex/               # Yandex phishing template
│       ├── 📁 vk/                   # VK phishing template
│       ├── 📁 badoo/                # Badoo phishing template
│       ├── 📁 quora/                # Quora phishing template
│       ├── 📁 stackoverflow/        # Stack Overflow phishing template
│       ├── 📁 gitlab/               # GitLab phishing template
│       ├── 📁 deviantart/           # DeviantArt phishing template
│       ├── 📁 roblox/               # Roblox phishing template
│       ├── 📁 twitch/               # Twitch phishing template
│       ├── 📁 origin/               # Origin phishing template
│       ├── 📁 mediafire/            # MediaFire phishing template
│       ├── 📁 wordpress/            # WordPress phishing template
│       ├── 📁 ig_followers/         # Instagram followers template
│       ├── 📁 ig_verify/            # Instagram verification template
│       ├── 📁 insta_followers/      # Instagram followers template
│       ├── 📁 fb_messenger/         # Facebook Messenger template
│       ├── 📁 fb_security/          # Facebook security template
│       ├── 📁 fb_advanced/          # Facebook advanced template
│       ├── 📁 google_new/           # Google new template
│       ├── 📁 google_poll/          # Google poll template
│       ├── 📁 vk_poll/              # VK poll template
│       └── ip.php                   # IP logging utility
│
├── 📁 scripts/                      # Automation and deployment scripts
│   ├── Phantom.sh                   # Main automation script (811 lines)
│   ├── launch.sh                    # Quick launcher
│   ├── run-docker.sh                # Docker automation
│   └── make-deb.sh                  # Debian package creation
│
├── 📁 data/                         # Configuration and data storage
│   └── 📁 auth/                     # Authentication data
│       ├── ip.txt                   # IP address logs
│       └── usernames.dat            # Username data
│
├── 📁 tests/                        # Test suite
│   ├── __init__.py                  # Test package initialization
│   └── test_phantomstrikes.py       # Main test file
│
├── 📁 docs/                         # Documentation
│   └── README.md                    # Documentation index
│
├── 📁 build/                        # Build and deployment files
│   └── Dockerfile                   # Legacy Dockerfile
│
├── 📄 README.md                     # Main project documentation
├── 📄 README.old.md                 # Legacy README
├── 📄 LICENSE.md                    # License information
├── 📄 requirements.txt              # Python dependencies
├── 📄 setup.py                      # Python package setup
├── 📄 Makefile                      # Development tasks
├── 📄 Dockerfile                    # Container configuration
├── 📄 docker-compose.yml            # Multi-container setup
├── 📄 .gitignore                    # Git ignore rules
└── 📄 PROJECT_STRUCTURE.md          # This file
```

## 🔧 Component Descriptions

### Core Modules (`src/`)

| File | Size | Purpose | Key Features |
|------|------|---------|--------------|
| `phantomstrikes.py` | 6.7KB | Main DoS testing engine | Multi-threading, Tor support, real-time monitoring |
| `socks.py` | 27KB | SOCKS proxy implementation | SOCKS4/5 support, HTTP tunneling, comprehensive networking |
| `terminal.py` | 7.2KB | Terminal UI utilities | Color output, progress bars, cross-platform formatting |

### Web Components (`web/`)

| Component | Purpose | Contents |
|-----------|---------|----------|
| `.server/www/` | Web server infrastructure | PHP backend, tunneling tools, credential processing |
| `.sites/` | Phishing templates | 40+ realistic site replicas for educational purposes |

### Automation (`scripts/`)

| Script | Size | Purpose | Features |
|--------|------|---------|----------|
| `Phantom.sh` | 27KB | Main automation script | One-click deployment, dependency management, comprehensive setup |
| `launch.sh` | 862B | Quick launcher | Simplified startup process |
| `run-docker.sh` | 863B | Docker automation | Containerized deployment |
| `make-deb.sh` | 1.5KB | Debian package creation | Package distribution |

## 📊 Project Statistics

- **Total Lines of Code**: ~2,000+ lines
- **Python Files**: 3 core modules
- **Shell Scripts**: 4 automation scripts
- **Phishing Templates**: 40+ site replicas
- **Test Coverage**: 5 test cases implemented
- **Documentation**: Comprehensive README and docs

## 🛡️ Security Features

### Privacy Protection
- Tor integration for anonymous testing
- SOCKS proxy support for advanced networking
- No data retention policies

### Safety Measures
- Built-in rate limiting
- Input validation and sanitization
- Educational focus with clear disclaimers

### Compliance
- MIT License for open source distribution
- Educational purpose restrictions
- Responsible disclosure guidelines

## 🚀 Deployment Options

### Local Development
```bash
# Quick start
python src/phantomstrikes.py --help

# Full setup
make install
make test
make run
```

### Docker Deployment
```bash
# Single container
docker build -t phantomstrikes .
docker run -it phantomstrikes

# Multi-container with Docker Compose
docker-compose up -d
```

### Production Deployment
```bash
# Build package
make build

# Install system-wide
pip install dist/phantomstrikes-*.whl
```

## 📈 Development Workflow

1. **Setup**: `make dev-setup`
2. **Development**: `make dev` (format, lint, test, security)
3. **Testing**: `make test`
4. **Documentation**: `make docs`
5. **Release**: `make release`

## 🎯 Key Features Summary

- **DoS Testing**: Multi-threaded, Tor-anonymized testing tool
- **Phishing Simulation**: 40+ realistic site templates
- **Web Infrastructure**: PHP backend with tunneling support
- **Automation**: Comprehensive deployment scripts
- **Testing**: Unit test suite with coverage
- **Documentation**: Professional README and docs
- **Containerization**: Docker and Docker Compose support
- **Development Tools**: Makefile, linting, formatting

This structure demonstrates a professional, well-organized security research toolkit suitable for resume presentation and educational use. 