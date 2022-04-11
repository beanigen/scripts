#!/usr/bin/env python3
import i3ipc
i3 = i3ipc.Connection()
check = 0

# prints default on script start and prevents itself from infinitely printing default
if check == 0:
    print("default")
    check = 1

# i have no idea how i managed to get this data correctly but it works
def on_mode_changed(self, obj):
    if obj:
        print(str(obj.change))


i3.on("mode", on_mode_changed) 

i3.main()
