# Malformed URL Detector

A Python utility tool that analyzes server access logs to identify and report malformed URLs.

## Overview

This tool scans through access log files to detect potentially malformed URLs that could indicate security issues, misconfigured applications, or attempted exploits. It utilizes regular expressions and URL parsing to identify URLs that don't conform to expected patterns.

## Features

- Detects URLs with invalid schemes, missing components, or unusual patterns
- Works with standard web server log formats (Apache, Nginx, etc.)
- Provides line numbers for easy reference to problematic entries
- Simple command-line interface for quick analysis

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Installation

Clone this repository:

```bash
git clone https://github.com/dcgmechanics/Malformed-URL-Detector.git
cd malformed-url-detector
```

Make the script executable (Linux/Mac):

```bash
chmod +x install.sh
./install.sh
```

Or run the Windows installation script:

```bash
install.bat
```

## Usage

```bash
python malformed_urls.py <path_to_log_file>
```

### Example

```bash
python malformed_urls.py /var/log/apache2/access.log
```

### Sample Output

```
Line 125: Malformed URL found: http://example.com/%Invalid%Path
Line 347: Malformed URL found: https://example.com/?q=test%
Line 982: Error parsing URL: http:///malformed.url - Error: Invalid URL
```

## Use Cases

- Security auditing of web servers
- Troubleshooting application URL issues
- Identifying potential web scraping or crawling issues
- Detecting malicious scanning attempts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Inspired by common web server security auditing practices
- Developed to simplify the process of identifying potential security issues in web applications 