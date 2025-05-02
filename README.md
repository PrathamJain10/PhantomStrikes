# PhantomStrikes

> **For educational purposes only.**

PhantomStrikes is a multi-component toolkit for security research, penetration testing, and educational demonstration of web and network vulnerabilities. It includes a maintained fork of Torshammer (Slow POST DoS tool), a collection of phishing site templates, and web server automation scripts. 

## Features
- **Slow POST DoS Testing Tool**: Python-based, Tor-anonymized, multi-threaded (see `src/phantomstrikes.py`).
- **SOCKS Proxy Support**: Via included `src/socks.py`.
- **Terminal Utilities**: For colored and formatted output (`src/terminal.py`).
- **Phishing Site Templates**: Located in `web/.sites/` and `web/.server/www/` for educational demonstration.
- **Automation Scripts**: Shell scripts for setup, deployment, and running web servers (`scripts/`).
- **Docker Support**: For easy deployment (`build/Dockerfile`).

## Directory Structure
```
PhantomStrikes/
│
├── src/                  # Python source code (DoS tool, SOCKS, terminal)
├── scripts/              # Shell scripts for automation and deployment
├── web/                  # Web server files and phishing site templates
│   ├── .server/
│   └── .sites/
├── data/                 # Data and config files (e.g., auth info)
├── build/                # Build and deployment files (Dockerfile)
├── LICENSE.md            # License information
├── README.md             # This file
└── README.old.md         # Legacy README
```

## Usage
### 1. DoS Testing Tool (PhantomStrikes)
- **Requirements:** Python 3, Tor running locally on port 9150
- **Run:**
  ```bash
  cd src
  python phantomstrikes.py -t <target> [-r <threads> -p <port> -T]
  ```
  - `-t` Target host/IP
  - `-r` Number of threads (default: 256)
  - `-p` Port (default: 80)
  - `-T` Enable Tor anonymization

### 2. Web Server & Phishing Templates
- See `scripts/Phantom.sh` and `web/.server/www/README.md` for details.
- **Note:** All templates are for demonstration and awareness only.

### 3. Docker
- Build and run using the provided Dockerfile in `build/`.

## Credits
- **Original Torshammer**: entropy [at] phiral.net
- **SOCKS module**: Dan-Haim, Christopher Gilbert, Mario Vilas, Anorov, and others
- **Phishing Templates**: Various authors (see `web/.server/www/README.md`)
- **Project Maintainers**: Pratham Jain and Team

## License
See `LICENSE.md` and individual files for license details.

## Disclaimer
This project is for **educational and research purposes only**. The authors are not responsible for any misuse. Use responsibly and legally. 