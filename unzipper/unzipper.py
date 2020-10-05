import sys
import zipfile
if not len(sys.argv) > 2:
    print("Error: must specify a directory to extract to!\nUsage: unzipper [file_to_extract] [dir_to_extract_to]")
    sys.exit(1)
file_to_extract = sys.argv[1]
dir_to_extract = sys.argv[2]

try:
    with zipfile.ZipFile(file_to_extract, 'r') as unzipper:
        print('Unzipping!')
        unzipper.extractall(dir_to_extract)
except FileNotFoundError:
    print("Please enter a valid file/directory to extract to!")
    sys.exit(1)
