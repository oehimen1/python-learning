from pathlib import Path

# Absolute path -  start from root of hard disk
# /usr/local/bin

# Relative path - start for current directory
# lessons/converters.py

path = Path()
for file in path.glob('*'):
    print(file)





