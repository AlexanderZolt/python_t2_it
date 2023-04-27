import sys
try:
    with open(sys.argv[1], 'r') as f: print(f.read())
except FileNotFoundError: print("File not found")
finally: sys.exit(1)