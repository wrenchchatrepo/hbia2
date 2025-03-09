"""
Setup script for the mcp-credentials package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp-credentials",
    version="0.1.0",
    author="Dion Edge",
    author_email="dion@wrench.chat",
    description="Secure Credential Management System for MCP servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wrenchchatrepo/mcp-credentials",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mcp-credentials=mcp_credentials.cli:main",
            "mcp-credentials-server=mcp_credentials.server:main",
        ],
    },
) 