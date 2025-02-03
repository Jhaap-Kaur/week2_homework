# sys module: Access system-specific parameters, command-line arguments, and system functions.
# glob: Search for files and directories using wildcards(for file pattern matching).
# os: Work with files, directories, and interact with the OS.
import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    home_drive = os.environ["HOMEDRIVE"]  # Get the drive letter
    home_path = os.environ["HOMEPATH"]  # Get the home folder path
    home_dir = os.path.join(home_drive, home_path)  # Combine drive and path to get full home directory
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern and to join it to the home directory
pattern = os.path.join(home_dir,'*')
print(pattern)

files_count = len(pattern)
print(files_count)

# get the list of files and the glob module used to get all files that match the pattern specified in pattern.
file_list = glob.glob(pattern)

# The loop variable file represents each file or folder in the file_list on each iteration.
# for loop and if the file_list is in the pattern,glob-Get all the matching files
for file in file_list:
  file_size= os.path.getsize(file) # get the file size in bytes
  if file_size > 0:
      print(f"File: {os.path.basename(file)} - Size: {file_size} bytes")
      # print(file,file_size,"bytes")
      # print(os.path.basename(file) ,file_size ,"bytes")





