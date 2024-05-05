import os
import hashlib

def file_hash(filepath):
    """Calculate SHA-256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:  # rb means read in binary
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def remove_duplicates(directory):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filehash = file_hash(filepath)
            if filehash in hashes:
                print(f"Removing duplicate file: {filepath}")
                os.remove(filepath)
            else:
                hashes[filehash] = filepath

if __name__ == "__main__":
    directory_path = "files-duplicate"
    remove_duplicates(directory_path)