#!/usr/bin/env python3
"""
PhantomStrikes - Advanced Security Research & Penetration Testing Toolkit
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="phantomstrikes",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced Security Research & Penetration Testing Toolkit",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/PhantomStrikes",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/PhantomStrikes/issues",
        "Documentation": "https://github.com/yourusername/PhantomStrikes/docs",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Software Development :: Testing",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "phantomstrikes=phantomstrikes:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="security, penetration-testing, dos, phishing, research, toolkit",
) 