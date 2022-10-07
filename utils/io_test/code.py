from os import listdir, mkdir, remove
from random import getrandbits
from time import sleep

chunk_size = 128
chunk_count = 10
chunk_dir = ""
tape_name = "random"

# test

# Check for writeable filesystem
if "NO_USB" not in listdir():
    while True:
        print("\n--\n")
        print("Read only filesystem. Add file 'NO_USB' and reboot")
        sleep(3)
else:
    try:
        open("foo.foo", "wb")
        remove("foo.foo")
    except:
        while True:
            print("\n--\n")
            print("Reboot to USB off with:")
            print("import microcontroller")
            print("microcontroller.reset()")
            sleep(3)

sleep(2)
i = 1
# while True:
print(f"Starting test {i}")
# Prepare filesystem for clean test
if chunk_dir in listdir():
    for chunk_file in sorted(listdir(chunk_dir)):
        print("removing:", f"{chunk_dir}/{chunk_file}")
        remove(f"{chunk_dir}/{chunk_file}")
else:
    print(f"Making {chunk_dir}")
    mkdir(chunk_dir)
assert chunk_dir in listdir(), f"{chunk_dir} does not exist in filesystem"

# Create chunks
for i in range(chunk_count):
    # path = f"{chunk_dir}/{tape_name}_chunk{i:03d}.tape"
    path = f"{tape_name}_chunk{i:03d}.tape"
    print(f"Creating: {path}")
    f = open(path, "wb")
    f.write(bytes(getrandbits(8) for _ in range(chunk_size)))
    f.close()

print("\n-- chunk_dir --\n", listdir(chunk_dir), "\n-- chunk_dir --\n")

# remove("NO_USB")
# import microcontroller

# microcontroller.reset()
# assert False

for i in range(chunk_count):
    name = f"{tape_name}_chunk{i:03d}.tape"
    assert name in listdir(chunk_dir), f"{name} does not exist in {chunk_dir}"

# Compile chunks
tape_file = f"{tape_name}.tape"
f = open(tape_file, "wb")
for chunk_file in sorted([x for x in listdir() if "_chunk" in x]):
    print(f"Unpacking {chunk_file} into {tape_file}")
    f.write(open(f"{chunk_dir}/{chunk_file}", "rb").read())
    # f.write(open(f"{chunk_dir}/{chunk_file}", "rb").read())
f.close()

print("\n-- file_system --\n", listdir(), "\n-- file_system --\n")

assert tape_file in listdir(), f"{tape_file} does not exist in filesystem"

print("\n\n")
print("PASSED")
print("\n\n")
i += 1
sleep(1)
