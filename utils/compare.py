"""
This is a quick script for testing if the uploaded tapefile chunks
match the tapefile chunks downloaded by the updator app in amiga-fw
"""
import json

dir1 = "/mnt/e/chunks"
dir2 = "dashboard-v0.0.8-dev"

chunk_size = 256

metadata = json.load(open(f"{dir2}/metadata.json", "r"))
print(metadata)

for i in range(int(metadata["chunk_count"])):

    file_name = f"{metadata['app']}.tape-chunk_{i:03d}"
    print("\n", file_name)
    file1 = open(f"{dir1}/{file_name}", "rb")
    file2 = open(f"{dir2}/{file_name}", "rb")
    # file2 = open("../amiga-fw/src/updator.tape", "rb")

    a = file1.read(chunk_size)
    b = file2.read(chunk_size)
    i = 0
    while a or b:
        a = file1.read(chunk_size)
        b = file2.read(chunk_size)

        if a != b:
            print(f"\nChunk {i}\n")
            print(a)
            print("\nvs\n")
            print(b)
            break

        i += 1
