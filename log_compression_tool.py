#!/usr/bin/env python3
"""
Compress the files in log directory to free up some space
"""

import gzip
import shutil
import os
import sys


def main(logs_dir):
    log_paths = get_log_files(logs_dir)
    compress_files(log_paths)


def get_log_files(logs_dir):
    """Return a list of files from given directory that aren't compressed yet"""
    filenames = os.listdir(logs_dir)
    log_paths = []
    for filename in filenames:
        filepath = os.path.join(logs_dir,filename)
        if os.path.isfile(filepath):
            # we don't need already compressed files
            if not filename.endswith(".gz"):
               log_path = os.path.join(logs_dir, filename)
               log_paths.append(log_path)
    return log_paths


def compress_files(log_paths):
    """
    Compress files in given list using gzip module.

    Original file is not removed, compressed copy is saved in the same directory
    with ".gz" suffix.
    For example, the directory will contain both `file.log` and `file.log.gz`.
    """
    for log_path in log_paths:
        with open(log_path, 'rb') as f_in:
            gz_log_path = log_path + ".gz"
            with gzip.open(gz_log_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


if __name__ == "__main__":
    logs_dir = sys.argv[0]
    main(logs_dir)
