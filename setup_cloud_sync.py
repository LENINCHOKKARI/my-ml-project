#!/usr/bin/env python3
"""
Quick Cloud Integration Setup
Run this to prepare your project for cloud platforms
"""

import os
import subprocess
from pathlib import Path

def setup_git_integration():
    """Initialize Git for cloud sync"""
    
    commands = [
        "git init",
        "git add .",
        'git commit -m "Initial ML project setup from Kiro"'
    ]
    
    print("🔧 Setting up Git integration...")
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {cmd}")
            else:
                print(f"⚠️ {cmd} - {result.stderr}")
        except Exception as e:
            print(f"❌ {cmd} - {e}")

def create_cloud_notebooks():
    """Create template notebooks for each platform"""
    
    # Google Colab template
    colab_template = '''
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# ML Project - Google Colab\\n", "GPU-powered training notebook"]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup\\n",
    "!git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git\\n",
    "%cd YOUR_REPO\\n",
    "!pip install -r requirements.txt\\n",
    "\\n",
    "# Check GPU\\n",
    "import torch\\n",
    "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\\n",
    "print(f'Using device: {device}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
'''
    
    # Save templates
    notebooks_dir = Path("notebooks/cloud_templates")
    notebooks_dir.mkdir(exist_ok=True)
    
    with open(notebooks_dir / "colab_template.ipynb", "w") as f:
        f.write(colab_template)
    
    print("📓 Created cloud notebook templates in notebooks/cloud_templates/")

def create_deployment_configs():
    """Create configuration files for cloud deployment"""
    
    # Docker for cloud deployment
    cloud_dockerfile = '''
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
    
    with open("Dockerfile.cloud", "w") as f:
        f.write(cloud_dockerfile)
    
    print("🐳 Created Dockerfile.cloud for cloud deployment")

def main():
    """Run complete cloud integration setup"""
    
    print("🚀 Setting up cloud integration for your ML project...")
    print()
    
    # Check if we're in the right directory
    if not Path("my_ml_project").exists():
        print("❌ Please run this from the directory containing 'my_ml_project'")
        return
    
    os.chdir("my_ml_project")
    
    setup_git_integration()
    create_cloud_notebooks()
    create_deployment_configs()
    
    print()
    print("✅ Cloud integration setup complete!")
    print()
    print("Next steps:")
    print("1. Create GitHub repository")
    print("2. Push code: git remote add origin <your-repo-url>")
    print("3. git push -u origin main")
    print("4. Use notebooks/cloud_templates/ in cloud platforms")

if __name__ == "__main__":
    main()