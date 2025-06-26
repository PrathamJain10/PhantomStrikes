#!/usr/bin/env python3
"""
PhantomStrikes Launcher
Simple launcher script for the PhantomStrikes security research toolkit
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def print_banner():
    """Print the PhantomStrikes banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🔥 PhantomStrikes 🔥                     ║
    ║              Advanced Security Research Toolkit              ║
    ║                                                              ║
    ║  For Educational Purposes Only - Use Responsibly            ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required")
        return False
    
    # Check if src directory exists
    src_dir = Path("src")
    if not src_dir.exists():
        print("❌ src/ directory not found")
        return False
    
    # Check if main files exist
    main_files = ["src/phantomstrikes.py", "src/socks.py", "src/terminal.py"]
    missing_files = []
    
    for file_path in main_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ Basic dependencies are available")
    print("💡 For full functionality, run: pip install -r requirements.txt")
    return True

def launch_dos_tool(args):
    """Launch the DoS testing tool"""
    print("🚀 Launching DoS Testing Tool...")
    
    cmd = [sys.executable, "src/phantomstrikes.py"]
    
    if args.target:
        cmd.extend(["-t", args.target])
    if args.threads:
        cmd.extend(["-r", str(args.threads)])
    if args.port:
        cmd.extend(["-p", str(args.port)])
    if args.tor:
        cmd.append("-T")
    if args.show_help:
        cmd.append("-h")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running DoS tool: {e}")
    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user")

def launch_web_server(args):
    """Launch the web server"""
    print("🌐 Launching Web Server...")
    
    web_dir = Path("web/.server/www")
    if not web_dir.exists():
        print("❌ Web server directory not found")
        return
    
    port = args.port or 8080
    host = args.host or "127.0.0.1"
    
    print(f"📡 Starting server on {host}:{port}")
    print("🔗 Access the server at: http://localhost:8080")
    
    try:
        os.chdir(web_dir)
        subprocess.run([
            sys.executable, "-m", "http.server", str(port), 
            "--bind", host
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running web server: {e}")
    except KeyboardInterrupt:
        print("\n⏹️  Web server stopped")

def launch_phishing_simulation(args):
    """Launch the phishing simulation"""
    print("🎣 Launching Phishing Simulation...")
    
    script_path = Path("scripts/Phantom.sh")
    if not script_path.exists():
        print("❌ Phantom.sh script not found")
        return
    
    try:
        subprocess.run(["bash", str(script_path)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running phishing simulation: {e}")
    except KeyboardInterrupt:
        print("\n⏹️  Phishing simulation stopped")

def run_tests():
    """Run the test suite"""
    print("🧪 Running tests...")
    
    try:
        subprocess.run([
            sys.executable, "-m", "pytest", "tests/", "-v"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")

def show_help():
    """Show help information"""
    help_text = """
    🎯 Available Commands:
    
    dos          - Launch DoS testing tool
    web          - Launch web server
    phishing     - Launch phishing simulation
    test         - Run test suite
    help         - Show this help
    
    📋 Examples:
    
    # Launch DoS tool
    python launch.py dos -t 192.168.1.100 -r 256
    
    # Launch web server
    python launch.py web -p 8080
    
    # Launch phishing simulation
    python launch.py phishing
    
    # Run tests
    python launch.py test
    
    🔧 Options:
    
    DoS Tool Options:
    -t, --target    Target hostname or IP
    -r, --threads   Number of threads (default: 256)
    -p, --port      Target port (default: 80)
    -T, --tor       Enable Tor anonymization
    
    Web Server Options:
    -p, --port      Port to bind (default: 8080)
    -h, --host      Host to bind (default: 127.0.0.1)
    
    ⚠️  Important:
    - This toolkit is for educational purposes only
    - Always obtain proper authorization before testing
    - Use responsibly and legally
    """
    print(help_text)

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(
        description="PhantomStrikes Security Research Toolkit Launcher",
        add_help=False
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # DoS tool parser
    dos_parser = subparsers.add_parser('dos', help='Launch DoS testing tool')
    dos_parser.add_argument('-t', '--target', help='Target hostname or IP')
    dos_parser.add_argument('-r', '--threads', type=int, help='Number of threads')
    dos_parser.add_argument('-p', '--port', type=int, help='Target port')
    dos_parser.add_argument('-T', '--tor', action='store_true', help='Enable Tor')
    dos_parser.add_argument('--show-help', action='store_true', help='Show DoS tool help')
    
    # Web server parser
    web_parser = subparsers.add_parser('web', help='Launch web server')
    web_parser.add_argument('-p', '--port', type=int, default=8080, help='Port to bind')
    web_parser.add_argument('--host', default='127.0.0.1', help='Host to bind')
    
    # Phishing simulation parser
    subparsers.add_parser('phishing', help='Launch phishing simulation')
    
    # Test parser
    subparsers.add_parser('test', help='Run test suite')
    
    # Help parser
    subparsers.add_parser('help', help='Show help information')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Handle commands
    if args.command == 'dos':
        launch_dos_tool(args)
    elif args.command == 'web':
        launch_web_server(args)
    elif args.command == 'phishing':
        launch_phishing_simulation(args)
    elif args.command == 'test':
        run_tests()
    elif args.command == 'help' or not args.command:
        show_help()
    else:
        print(f"❌ Unknown command: {args.command}")
        show_help()

if __name__ == "__main__":
    main() 