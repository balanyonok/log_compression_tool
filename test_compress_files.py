#!/usr/bin/env python3

"""
Test the compress_files() function.
The result should be files with .gz extension in the same directory
"""

import pytest
from log_compression_tool import compress_files
import os
import tempfile
import shutil

def test_files_to_compress():
    """
    Testcase: there are files to be compressed in given directory.
    """
    log_paths = [
        "tests/data/files_to_compress/testlog3",
        "tests/data/files_to_compress/testfile2.log",
        "tests/data/files_to_compress/testfile1.log",
    ]

    sourcedir = "tests/data/files_to_compress"
    files_copies = []

    expected_files = [
        "testlog3",
        "testlog3.gz",
        "testfile2.log",
        "testfile2.log.gz",
        "testfile1.log",
        "testfile1.log.gz",
    ]
    # create a temporary directory with copies of files for further work
    with tempfile.TemporaryDirectory() as tmp_directory:
        for log_path in log_paths:
            shutil.copy(log_path, tmp_directory)
            file_copy = log_path.replace(sourcedir, tmp_directory)
            files_copies.append(file_copy)
            compress_files(files_copies)
        assert list(sorted(os.listdir(tmp_directory))) == list(sorted(expected_files))


@pytest.mark.skip(reason="TODO")
def test_no_files_to_compress():
    """
    Testcase: there aren't any files to be compressed.
    """
    pass