#!/usr/bin/env python3

import argparse
import subprocess
import json
from datetime import datetime
import os
from rich.console import Console
from rich.table import Table

console = Console()

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8').strip()
    except:
        return ''

def main():
    parser = argparse.ArgumentParser(description='Auto Bug Bounty Hunter')
    parser.add_argument('-d', '--domain', required=True, help='Target domain')
    parser.add_argument('-o', '--output', default='report.html', help='Output report file')
    args = parser.parse_args()

    domain = args.domain
    console.print(f'[bold green]Hunting {domain}...[/bold green]')

    # Subdomain enum (using subfinder if available, else simple)
    console.print('[yellow]Enumerating subdomains...[/yellow]')
    subs = run_command(f'subfinder -d {domain} -silent') if 'subfinder' in run_command('which subfinder') else run_command(f'curl -s "https://crt.sh/?q=%25.{domain}&output=json" | grep -o "[^\"]*\.{domain}" | sort -u')

    # Tech detection
    console.print('[yellow]Detecting technologies...[/yellow]')
    tech = run_command(f'whatweb {domain} --color=never') if 'whatweb' in run_command('which whatweb') else 'Tech detection skipped'

    # Basic nuclei scan if installed
    console.print('[yellow]Scanning for vulns...[/yellow]')
    nuclei_out = run_command(f'nuclei -u https://{domain} -silent') if 'nuclei' in run_command('which nuclei') else 'Install nuclei for full scan'

    # Generate report
    report = f"""
    <html>
    <head><title>Bug Report for {domain}</title></head>
    <body>
    <h1>Bug Bounty Report - {domain}</h1>
    <p>Generated on {datetime.now()}</p>
    <h2>Subdomains Found: {len(subs.splitlines())}</h2>
    <pre>{subs}</pre>
    <h2>Technologies</h2>
    <pre>{tech}</pre>
    <h2>Vulnerabilities</h2>
    <pre>{nuclei_out}</pre>
    <h2>Recommendations</h2>
    <p>1. Fix any open redirects, XSS, etc. found.</p>
    <p>2. Use WAF and input sanitization.</p>
    <p>Report to program with evidence.</p>
    </body>
    </html>
    """

    with open(args.output, 'w') as f:
        f.write(report)

    console.print(f'[bold green]Report generated: {args.output}[/bold green]')
    console.print('Open it in browser for full details.')

if __name__ == '__main__':
    main()
