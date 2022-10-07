from os import listdir, mkdir, remove
from random import getrandbits
from time import sleep

"""
This version: Save directly into root
"""
chunk_size = 2048
chunk_count = 50
tape_name = "random"
tape_file = f"{tape_name}.tape"

# Check for writeable filesystem
if "NO_USB" not in listdir():
    while True:
        print("\n--\n")
        print("Read only filesystem. Add file 'NO_USB' and reboot")
        sleep(3)
else:
    try:
        with open("foo.foo", "wb"):
            pass
        remove("foo.foo")
    except:
        while True:
            print("\n--\n")
            print("Reboot to USB off with:")
            print("import microcontroller")
            print("microcontroller.reset()")
            sleep(3)

sleep(2)
j = 1
while True:
    print(f"Starting test {j}")

    # Prepare filesystem for clean test
    for chunk_file in sorted([x for x in listdir() if "_chunk" in x]):
        # Remove tape files too
        print("removing:", chunk_file)
        remove(chunk_file)
    if tape_file in listdir():
        # Remove tape files too
        print("removing:", tape_file)
        remove(tape_file)
    # os.sync()

    print("\n-- file_system pre --\n", listdir(), "\n--\n")

    # Create chunks
    for i in range(chunk_count):
        path = f"{tape_name}_chunk{i:03d}.tape"
        print(f"Creating: {path}")
        with open(path, "wb") as f:
            f.write(bytes(getrandbits(8) for _ in range(chunk_size)))
    # os.sync()

    for i in range(chunk_count):
        name = f"{tape_name}_chunk{i:03d}.tape"
        assert name in listdir(), f"{name} does not exist"

    # Compile chunks
    with open(tape_file, "wb") as f:
        for chunk_file in sorted([x for x in listdir() if "_chunk" in x]):
            print(f"Unpacking {chunk_file} into {tape_file}")
            f.write(open(chunk_file, "rb").read())
    # os.sync()

    print("\n-- file_system post --\n", listdir(), "\n--\n")

    assert tape_file in listdir(), f"{tape_file} does not exist in filesystem"

    print("\n\n")
    print("PASSED")
    print("\n\n")
    j += 1
    sleep(1)
