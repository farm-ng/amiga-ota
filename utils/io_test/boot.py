import os
import storage
import supervisor
import usb_hid, usb_midi

# On some boards, we need to give up HID to accomodate MIDI.
usb_hid.disable()
usb_midi.disable()
supervisor.disable_autoreload()

NO_USB = False
for x in os.listdir():
    if x == "NO_USB":
        NO_USB = True
if NO_USB:
    print("Disabling usb storage. Remove NO_USB file to re-enable")
    storage.disable_usb_drive()
    storage.remount("/", False)
else:
    storage.remount("/", True)
    storage.enable_usb_drive()

# storage.enable_usb_drive()
# storage.remount("/", False)
