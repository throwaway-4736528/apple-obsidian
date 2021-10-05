# apple-obsidian
Scripts to help migrate notes from Apple notes to Obsidian.

>Note that all scripts are provided as-is, and are tested only on my files. Test them on a subset of your notes before using them for real, and of course ensure you have multiple backups. Data loss is not my responsibility :)

## exporting notes from Apple notes
I'm on a Mac and used the very excellent [Exporter](https://apps.apple.com/de/app/exporter/id1099120373) to do the initial export. Notes were exported into folders that mimicked the structure in Apple Notes.

Once that was done though I had a couple of challenges:
1. How to prepend metadata to each note? (I attach metadata to each note in Obsidian that forces me to associate it with a MOC and also link it to at least two other notes to aid future discoverability)
2. How to fix the file attachment links? (I wanted to make the links point to the file stored in the attachments folder in my vault, once I'd moved it there)

So I wrote the Python scripts below.


## prepend-metadata.py
- prepends obsidian metadata to the files in a folder
- for what folder select the folder in finder, then option-right-click to copy the path as Pathname
- for MOC, copy the full MOC as it will be inserted as a string, ie `[[Gardening MOC]]`
- obviously change the metadata in the script to what you want

## search-replace.py
- replaces the apple notes exports links to link back to your vault
- note that it simply removes any path information from the attachment filename string, on the basis that Obsidian knows where to look for attachments based on the configuration under Settings > Files & Links
- If you have multiple attachments with the same name, then this script will likely cause problems
- the script is set to create backups (.bak) of any files it changes, so you can always revert if needed.