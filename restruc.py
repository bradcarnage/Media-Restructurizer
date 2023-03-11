import os
import re
# source media storage directory (Flood UI via Transmission)
mediadir = f'/mnt/bigstore/MediaStorage/'
# destination media library directory (JellyFin scannable)
strucdir = f'/mnt/bigstore/MediaLibrary/'

# fix mediadir variable if user forgot trailing filesep
if not mediadir.endswith(os.path.sep):
    mediadir = mediadir+os.path.sep
if not strucdir.endswith(os.path.sep):
    strucdir = strucdir+os.path.sep
regex_topdir = re.compile(str(mediadir+r'.*?'+os.path.sep+r'(.*?)'+os.path.sep))
regex_episode = re.compile(r'^.*S0*(\d+).*?E0*(\d+).*\.(.*?)$', flags=re.IGNORECASE)

def mkdir(directory):
    os.makedirs(directory,exist_ok=True)

# this entire function was written by ChatGPT
def clean_dir(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.islink(item_path) and not os.path.exists(item_path):
            # Remove broken symlink
            os.remove(item_path)
            print(f'Removed {item_path}')
        elif os.path.isdir(item_path):
            # Recursively clean subdirectory
            clean_dir(item_path)
            # Remove empty subdirectory
            if not os.listdir(item_path):
                os.rmdir(item_path)
                print(f'Removed {item_path}')

mkdir(strucdir)
for subdir in ['Movies', 'Shows']:
    mediafolder = mediadir+subdir
    mediastruc = strucdir+subdir
    mkdir(mediastruc)
    clean_dir(mediafolder)
    clean_dir(mediastruc)
    for root, dirs, files in os.walk(mediafolder):
        for filename in files:
            match = regex_episode.match(filename)
            if match:
                sourcefile = os.path.join(root, filename)
                showname = regex_topdir.match(sourcefile).group(1)
                season = match.group(1)
                episode = match.group(2)
                ext = match.group(3)
                if ext != 'part':
                    # print(f"File: {sourcefile}, ShowName: {showname}, Season: {season}, Episode: {episode}, Ext {ext}")
                    destfolder = f'{mediastruc}{os.path.sep}{showname}{os.path.sep}Season {season}{os.path.sep}'.replace(os.path.sep+os.path.sep, os.path.sep)
                    destfile = f'Episode {episode}.{ext}'
                    if not os.path.islink(destfolder+destfile):
                        print(f'Mkdir {destfolder} and copy in {destfile}')
                        mkdir(destfolder)
                        os.symlink(sourcefile, destfolder+destfile)
print(f'all OK')


# Replace "path/to/directory" with the directory you want to clean
