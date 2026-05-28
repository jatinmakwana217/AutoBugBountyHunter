# AutoBugBountyHunter

**Fully Automatic Bug Bounty Hunting Tool**

Hunts any domain with recon, vulnerability scanning, and generates actual bug reports with solutions.

## Features
- Subdomain enumeration
- Technology detection
- Directory brute-forcing
- Vulnerability scanning (Nuclei templates)
- AI-like report with findings & fixes
- HTML report generation

## Installation on Kali / Termux (no root)
```bash
git clone https://github.com/jatinmakwana217/AutoBugBountyHunter.git
cd AutoBugBountyHunter
bash setup.sh
```

## Usage
```bash
python3 autobug.py --domain example.com --output report.html
```

**Important**: Only use on programs you are authorized for (bug bounty platforms). Educational tool.

Made with ❤️ for bug hunters.