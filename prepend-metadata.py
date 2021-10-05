# prepend a metadata block to .md file

# Set the folder
folder = input('What folder:')

# get the list of files in the folder https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
import glob

files = folder + "/*.md"
# All files ending with .md
filenames = glob.glob(files)

# get the MOC reference
moc_link = input('MOC link:')

# create the string
metadata = '''
- metadata
    - when: 
    - project: 
    - area: 
    - resource: ''' + moc_link + '''
    - author: 
    - source: 
    - links: 
        - 
    - knowledge discovery:
        - specific: 
        - related: 
        - tags: 

---
 
'''

# prepend the string to the file
for filename in filenames:
    print('processing file > '+filename)
    with open(filename, 'r') as original: data = original.read()
    with open(filename, 'w') as modified: modified.write(metadata + data)
