import os
dir = os.path.abspath(".\\testing\\dst")
dst_root = os.path.abspath(".\\testing\\src")
for root, dirs, files in os.walk(dir):
    for file in files:
        src_path = os.path.join(root, file)
        dst_path = os.path.join(dst_root, file)
        os.rename(src=src_path, dst=dst_path)
        print(f"moved {file} to src")
    else:
        print("no files found")
