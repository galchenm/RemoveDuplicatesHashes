import gdown
import glob
import os
import hashlib

def file_hash(filename):
    # Create a hash object
    hash_object = hashlib.sha256()
    # Read the file in binary mode and update hash object
    with open(filename, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in 64k chunks
            if not data:
                break
            hash_object.update(data)
    # Get the hexadecimal representation of the hash
    return hash_object.hexdigest()

outdir = 'files-duplicate'
if not os.path.exists(outdir):
  url = 'https://drive.google.com/drive/folders/1eqTkFXM9xqPr_D51XKdmzourOCeSRnjL'
  gdown.download_folder(url, quiet=True, use_cookies=False)

files = glob.glob(f'{outdir}/*.*')
files.sort()
file_hash = [(hash, file) for file, hash in zip(files, list(map(file_hash, files)))]

files_to_delete = dict(file_hash).values()

for file in files:
  if file in files_to_delete:
    os.remove(file)



