import re
import urllib.parse
import sys  # For command-line arguments and error handling

def find_malformed_urls_in_log(log_file_path):
    """
    Analyzes an access log file to find lines containing malformed URLs.

    Args:
        log_file_path (str): Path to the access log file.

    Returns:
        bool: True if malformed URLs were found, False otherwise.
    """

    malformed_urls_found = False

    try:
        with open(log_file_path, 'r') as log_file:
            for line_number, line in enumerate(log_file, 1):  # Enumerate for line numbers
                # 1. Basic URL Extraction using Regex (adjust regex as needed for log format)
                # This regex looks for strings starting with http:// or https:// followed by non-whitespace chars
                url_matches = re.findall(r'(https?://\S+)', line) # Basic regex for URLs

                if not url_matches:
                    # If no URLs found with the basic regex, let's try to find strings that *look* like URLs
                    # (e.g., starting with '/') -  This might catch relative URLs or paths
                    url_matches = re.findall(r'(\/\S+)', line) # Find paths starting with /

                for url_str in url_matches:
                    # 2. URL Parsing using urllib.parse
                    try:
                        parsed_url = urllib.parse.urlparse(url_str)

                        # 3. Malformed URL Checks (customize these checks based on definition)
                        is_malformed = False

                        if not parsed_url.scheme and url_str.startswith(('http://', 'https://')):
                            is_malformed = True # Scheme was expected but missing after initial match
                        elif not parsed_url.scheme and url_str.startswith('/'):
                            # Could be relative URL, depends on context. For now, flag as potentially malformed in access logs
                            is_malformed = True # Relative URL in access log might be unexpected

                        if is_malformed:
                            print(f"Line {line_number}: Malformed URL found: {url_str.strip()}")
                            malformed_urls_found = True

                    except Exception as e: # Catch parsing errors (though urlparse is generally robust)
                        print(f"Line {line_number}: Error parsing URL: {url_str.strip()} - Error: {e}")
                        malformed_urls_found = True


    except FileNotFoundError:
        print(f"Error: Log file not found: {log_file_path}")
        return False

    if not malformed_urls_found:
        print("No malformed URLs found in the log file.")
        return False # No malformed URLs found

    return True # Malformed URLs were found

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_malformed_urls.py <log_file_path>")
        sys.exit(1)

    log_file = sys.argv[1]
    if find_malformed_urls_in_log(log_file):
        print("\nAnalysis complete. Malformed URLs were detected (see output above).")
    else:
        print("\nAnalysis complete. No malformed URLs detected.")