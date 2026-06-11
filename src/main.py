from textnode import *
import os
import shutil

"""
    The purpose of this function is to recursively copy the
    contents of the source directory into the destination
    directory
"""


def recursive_copy(source: str, destination: str):
    everything_in_src = list(os.scandir(source))

    for item in everything_in_src:
        if item.is_file():
            shutil.copy(item.path, destination)
        elif item.is_dir():
            new_folder_path = f"{destination}/{item.name}"
            os.mkdir(new_folder_path)
            recursive_copy(f"{source}/{item.name}", new_folder_path)


"""
    The purpose of this function is to recursively delete
    objects in a directory.
"""


def recursive_delete(dest: str):
    # Delete all files in the destination directory
    everything_in_dest = list(os.scandir(dest))

    for item in everything_in_dest:
        if item.is_file():
            os.remove(item)
        elif item.is_dir():
            recursive_delete(item)
            os.rmdir(item)


"""
    The purpose of this function is to copy all the files
    from the source directory to the destination directory.
    All files in the destination directory are deleted
    before copying files from source directory.
"""


def directory_hard_copy(source: str, destination: str):
    # Delete all the files in the destination directory
    recursive_delete(destination)

    # Recursively copy everything from the source directory
    recursive_copy(source, destination)


def main():
    directory_hard_copy("static", "public")


main()
