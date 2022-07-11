import hashlib
import os
import sys


def hash_file(file_path):
    h = hashlib.sha1()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def main():
    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
    else:
        root_dir = os.getcwd()

    length = len(root_dir)

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            print(f"{hash_file(os.path.join(subdir, file))} {os.path.join(subdir[length + 1:], file)}")


if __name__ == "__main__":
    main()


