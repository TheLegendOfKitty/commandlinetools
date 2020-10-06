import os
import sys
try:
    if not len(sys.argv) > 2:
        #print(sys.argv)
        print("You must specify all the proper arguments!\nExample usage:\nisfile C:\ 123.txt")
    else:
        path = sys.argv[1]
        filetolook = sys.argv[2]
        #if '.txt' in file:
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                #if file.split("\\")[-1:] == sys.argv[2]:
                splitted = file.split("\\")
                #print(splitted)
                if splitted[0] == filetolook:
                    #print(splitted)
                    files.append(os.path.join(r, file))

        if len(files) == 0:
            print(f"No files found!")
        else:
            for f in files:
                print(f"File found: {f}")
            print(f"{len(files)} files matching {filetolook} found.")
except KeyboardInterrupt:
    print("Terminated.")
