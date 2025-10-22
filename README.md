
#Cyber security 
 
**COMPANY**:CODTECH SOLUTIONS

**NANE** : AFSAL.N

**INTERN ID**:COD123

**DOMAIN**:CYBER SECURITY 

**DURATION**: 1 month

**MENTOR**:NEELA SANTHOSH 

# Penetration Testing Toolkit

**A modular, Python-based toolkit** for basic penetration testing tasks — built as an internship task example.
Includes simple modules for:

* Port scanning (`port_scanner`)
* Banner grabbing (`banner_grabber`)
* Web login brute-forcing (simple form brute-forcer) (`brute_forcer`)

> ⚠️ **Legal & Ethical Notice:** Use this toolkit **only** on systems and networks you own or have explicit, written permission to test. Unauthorized scanning, brute-forcing, or attacking systems is illegal and unethical. The author / maintainers are not responsible for misuse.

---

## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Project structure](#project-structure)
* [Usage](#usage)

  * [Port scanner](#port-scanner)
  * [Banner grabber](#banner-grabber)
  * [Brute-forcer](#brute-forcer)
* [Examples](#examples)
* [Extending the toolkit](#extending-the-toolkit)
* [Safety & responsible use](#safety--responsible-use)
* [License](#license)

---

## Requirements

* Python 3.8+
* `requests` library (for the brute-forcer)

A sample `requirements.txt`:

```
requests>=2.28.0
```

---

## Installation

1. Clone or copy the repository to your machine:

```bash
git clone <repo-url> pen_test_toolkit
cd pen_test_toolkit
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project structure

```
pen_test_toolkit/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── port_scanner.py
│   ├── brute_forcer.py
│   └── banner_grabber.py
├── requirements.txt
└── README.md
```

---

## Usage

Run the toolkit via `main.py` and specify a module and target.

General syntax:

```bash
python main.py -m <module> -t <target> [options]
```

Available modules:

* `scanner` — run the port scanner
* `banner`  — run the banner grabber
* `brute`   — run the brute-forcer (web login form)

### Port scanner

Scans ports 1–1024 (default in sample). Example:

```bash
python main.py -m scanner -t 192.168.1.10
```

**Notes:**

* The included scanner is simple and synchronous; it’s intended for learning and demonstration, not large-scale scanning.
* To scan custom port ranges or speed up scanning, modify `modules/port_scanner.py` (add multithreading/async, set port range, timeouts).

### Banner grabber

Grab a service banner (e.g., HTTP, FTP, SSH) on a specific port:

```bash
python main.py -m banner -t 192.168.1.10 -p 22
```

**Notes:**

* Some services close connections immediately or require protocol-specific handshakes; the simple approach may not always return a banner.

### Brute-forcer (web form)

A minimal example that posts `username` and `password` fields to a target URL.

```bash
python main.py -m brute -t http://example.com/login -u admin -w /path/to/wordlist.txt
```

**Notes & caveats:**

* This brute-forcer tries passwords from a wordlist and posts `username`/`password` as form fields. It **does not** detect complex protections (CSRF, rate limits, captchas, IP banning).
* You must supply a correct login form endpoint and a compatible set of POST parameters. The brute-forcer is intentionally basic for educational purposes.

---

## Examples

* Port scan a local VM:

```bash
python main.py -m scanner -t 10.0.2.15
```

* Grab HTTP banner:

```bash
python main.py -m banner -t 10.0.2.15 -p 80
```

* Attempt brute-force (educational lab with permission):

```bash
python main.py -m brute -t http://lab.local/login -u testuser -w wordlists/common.txt
```

---

## Extending the toolkit

This toolkit is modular — add files under `modules/` and import them in `main.py`. Ideas to expand:

* Add multithreaded/async port scanner (use `concurrent.futures` or `asyncio`)
* Add service-specific checks (HTTP, SSH, FTP, SMB)
* Add vulnerability checks (e.g., default credentials, known CVE checks)
* Improve brute-forcer to handle JSON APIs, CSRF tokens, session cookies, backoff and rate-limiting, and proper detection of successful login
* Add logging, output reports (CSV/JSON), and CI-friendly tests

---

## Safety & responsible use

* Always have **explicit permission** before testing.
* Avoid running brute-forcing on production systems or any system without prior consent.
* Respect rate limits and avoid causing denial-of-service.
* Keep a log of tests and results; notify owners of discovered critical vulnerabilities responsibly (follow a coordinated disclosure policy).

---

## Troubleshooting

* Socket timeouts: increase the timeout in the module for slow networks.
* `requests` exceptions in brute-forcer: ensure the URL is correct and reachable; consider adding `verify=False` if testing self-signed HTTPS (only in labs).
* Permission errors: run with appropriate privileges if needed (scanning privileged ports <1024 on some systems).

---

## Contributing

This repository is educational. If you want to contribute:

* Open an issue describing the feature or bug.
* Submit a pull request with tests and documentation.
* Keep contributions legal and ethical — no features intended for clandestine malicious use

