import os
import os.path
from pathlib import Path

arr = []
for current_dir, dirs, files in os.walk("main"):
    sub = ".py"
    for s in files:
        if sub in s:
            if current_dir not in arr:
                arr.append(current_dir)
sort = sorted(arr)
with open('file_with_dir.txt', 'w') as f:
    for i in sort:
        f.write('%s\n' % i)