#!/usr/bin/python3
""" file log parsing """
import sys
import re
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regex pattern to match the input format
pattern = r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

def print_stats():
    """Print total file size and status code counts"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """Handle CTRL+C interr"""
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    match = re.match(pattern, line)
    
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        
        # Update metrics
        if status_code in status_counts:
            status_counts[status_code] += 1
            total_size += file_size
            line_count += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

# Print final stats if there are any processed lines
if line_count > 0:
    print_stats()
