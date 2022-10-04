"""
This is a quick script for compiling the chunks generated
with the tape.py chunk_command
"""
import os
import json


# path = "/mnt/e/chunks"
# tape_file = "dashboard_test.tape"

path = "dashboard-v0.0.8-dev"

metadata = json.load(open(f"{path}/metadata.json", "r"))
print(metadata)
tape_file = f"{metadata['app']}.tape"


f = open(tape_file, "wb")
for chunk_file in sorted(os.listdir(path)):
    if "chunk" not in chunk_file:
        continue
    print(f"Unpacking {chunk_file} into {tape_file}")
    f.write(open(f"{path}/{chunk_file}", "rb").read())
f.close()

"""
Then run:
cd ../amiga-fw/
export PYTHONPATH=$(pwd)/src:$(pwd)/regression
python3 -m farm_ng.utils.tape read \
--input $<tape_file> --dest /tmp --dry_run
"""
