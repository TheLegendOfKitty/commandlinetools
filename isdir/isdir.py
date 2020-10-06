import os
import sys
try:
    if not len(sys.argv) > 2:
        #print(sys.argv)
        print("You must specify all the proper arguments!\nExample usage:\nisdir C:\ Users")
    else:
        path = sys.argv[1]
        folder_to_look_for = sys.argv[2]
        folders = []
        for x in os.walk(path):
            if x[0].split("\\")[-1:][0] == folder_to_look_for:
                folders.append(x[0])
            #print(x[0].split("\\")[-1:][0])
    #print([x[0] for x in os.walk("C:\\")])
        if len(folders) == 0:
            print(f"No directories found!")
        else:
            for f in folders:
                print(f"Directory found: {f}")
            print(f"{len(folders)} directories matching {folder_to_look_for} found.")
except KeyboardInterrupt:
    print("Terminated.")
