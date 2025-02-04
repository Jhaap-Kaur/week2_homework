import sys, glob, os

# Get the directory name
# sys.platform is a string containing a platform identifier. For windows the value is 'win32'
# os.environ is a mapping object where keys and values are strings that represent the process environment.
# os.environ ['HOME'] is the pathname of the home directory.
# os = operating system
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# use the wildcard to match files in home directory that are txt files
# os.path.join joins one or more path segments. The return value is the concatenation of path and all member of paths.
# concatenating means obtaining a new string that contains both original strings
pattern = os.path.join(hdir,'*')

# added this as it shows you the file length
files_Count = len(pattern)
print(files_Count)

# Use the glob.glob() function to obtain the list of filenames that are files & folders.
file_list = glob.glob(pattern)

 # Iterate over the file list
for file_name in file_list:
    # Use os.path.getsize to find each file's size
    file_size = os.path.getsize(file_name)

    # Add a test to only display files that are not zero length
    # using if statement to test if files are 0 or above in size
    if file_size > 0:
        # Remove the leading directory name(s) from each filename before you print it
        # returns the base name of pathname path.
        base_name = os.path.basename(file_name)
        # string used to display files and bytes
        # we have used an f-string, placeholder in curly brackets to format the value
        print(f"File: {os.path.basename(file_name)} - Size: {file_size} bytes")


