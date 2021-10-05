# search and replace text in files
import glob
import fileinput
import urllib.parse

#%%
# Set the folder
folder = input('What folder:')

# get the list of files in the folder https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
files = folder + "/*.md"
# All files ending with .md
filenames = glob.glob(files)

searchstring1 = "](images/"
searchstring2 = "](attachments/"


#%%

for filename in filenames:
    print('processing file: '+filename)
    for line in fileinput.input(filename, inplace=True, backup='.bak'):
        if searchstring1 in line:
            original_str = line.split(searchstring1,-1)[1]
            original_str = original_str.split(")")[0] #remove trailing ")"
            original_str = urllib.parse.unquote(original_str)
            replace_str = '![['+original_str+']]'
            print(replace_str, end='')
        elif searchstring2 in line:
            original_str = line.split(searchstring2,-1)[1]
            original_str = original_str.split(")")[0] #remove trailing ")"
            original_str = urllib.parse.unquote(original_str)
            replace_str = '![['+original_str+']]'
            print(replace_str, end='')
        else:
            print(line, end='')

fileinput.close()