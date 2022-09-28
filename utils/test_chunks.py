"""
This is a quick script for compiling the chunks generated
with the tape.py chunk_command
"""
import os
import json

path = "updator-v0.0.1-dev"

metadata = json.load(open(f"{path}/metadata.json","r"))

print(metadata)

tape_file = f"{metadata['app']}.tape"
f = open(tape_file, "wb")
for chunk_file in sorted(os.listdir(path)):
    if "chunk" not in chunk_file:
        continue
    print(f"Unpacking {chunk_file} into {tape_file}")
    f.write(open(f"{path}/{chunk_file}", "rb").read())
f.close()