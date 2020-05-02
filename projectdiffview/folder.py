"""Any operations on the two folders."""
import configparser
import filecmp
import os
import typing
from collections import namedtuple
from pathlib import Path

CommonFile = namedtuple("CommonFile", ["template", "working"])

IGNORED = ".keep"


def folder_version(folder: typing.Optional[Path]) -> str:
    """Read the meta data file and update the line edit with the version."""
    if folder:
        meta_file = Path(folder).joinpath(".meta")
        if meta_file.exists():
            parser = configparser.ConfigParser()
            parser.read(meta_file)
            version = parser.get("META", "version")
            return version
    return "Unknown"


def get_empty_folders(root_path: typing.Optional[Path]) -> typing.List[Path]:
    """Walk the folder structure and return any empty folders."""
    empty_dirs = []
    if root_path:
        for (dir_path, dir_names, filenames) in os.walk(root_path):
            if len(dir_names) == 0 and len(filenames) == 0:
                empty_dirs.append(Path(dir_path))
            elif len(filenames) == 1 and IGNORED in filenames:
                empty_dirs.append(Path(dir_path))
    return empty_dirs


def get_unchanged_files(common_files: typing.List) -> typing.List[Path]:
    """Use the common list, compare and see if they have been edited."""
    unchanged = []
    for common_file in common_files:
        if filecmp.cmp(common_file.template, common_file.working, shallow=True):
            if common_file.working.name != ".meta":
                unchanged.append(common_file.working)
    return unchanged


def recursively_compare_folders(dir_cmp: filecmp.dircmp):
    """Compare two folders returning the common and unique for each half."""
    this_folder_common = [
        CommonFile(Path(dir_cmp.left).joinpath(item), Path(dir_cmp.right).joinpath(item))
        for item in dir_cmp.common
    ]
    this_folder_left = [Path(dir_cmp.left).joinpath(item) for item in dir_cmp.left_only]
    this_folder_right = [Path(dir_cmp.right).joinpath(item) for item in dir_cmp.right_only]

    # Recursively grab all files and folders under template only sub-dirs
    for item in this_folder_left:
        if item.is_dir() and item not in this_folder_common:
            this_folder_left.extend(item.rglob("*!(.keep)"))

    # Recursively grab all files and folders under working only sub-dirs
    for item in this_folder_right:
        if item.is_dir() and item not in this_folder_common:
            this_folder_right.extend(item.rglob("*!(.keep)"))

    # Recursively search through all the common sub directories.
    for sub_directory in dir_cmp.subdirs.values():
        common, left, right = recursively_compare_folders(sub_directory)
        this_folder_common += common
        this_folder_left += left
        this_folder_right += right

    return this_folder_common, this_folder_left, this_folder_right
