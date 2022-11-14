#!/usr/bin/env python3

"""
Test the remove_original_files() function.
"""

import pytest
from log_compression_tool import remove_original_files
import os
import tempfile
import shutil

def test_files_to_remove():
    log_paths = [
        "tests/data/files_to_compress/testlog3",
        "tests/data/files_to_compress/testfile2.log",
        "tests/data/files_to_compress/testfile1.log",
    ]

    sourcedir = "tests/data/files_to_compress"
    files_copies = []

    expected_files = []
    # create a temporary directory with copies of files for further work.
    with tempfile.TemporaryDirectory() as tmp_directory:
        for log_path in log_paths:
            shutil.copy(log_path, tmp_directory)
            file_copy = log_path.replace(sourcedir, tmp_directory)
            files_copies.append(file_copy)
            remove_original_files(files_copies)
        assert os.listdir(tmp_directory) == expected_files