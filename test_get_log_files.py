#!/usr/bin/env python3

"""
Test the get_log_files() function.
The result should be a list of non-compressed files in given directory.
"""

import pytest
from log_compression_tool import get_log_files
import os


def test_dir_with_logfiles():
    """
    Testcase: there are only log files in given directory.
    """
    logs_dir = "tests/data/basic"
    expected_log_paths = [
        "tests/data/basic/testlog3",
        "tests/data/basic/testfile2.log",
        "tests/data/basic/testfile1.log",
    ]

    assert get_log_files(logs_dir) == expected_log_paths


def test_dir_with_zipped_files_too():
    """
    Testcase: there are .log files AND .gz files as well
    """
    logs_dir = "tests/data/basic_and_zipped"
    expected_log_paths = [
        "tests/data/basic_and_zipped/testfile2.log",
        "tests/data/basic_and_zipped/testfile1.log",
    ]

    assert get_log_files(logs_dir) == expected_log_paths


def test_dir_with_diff_zipped_files():
    """
    Testcase: there are also compressed files with different extensions
    in the given directory.
    """
    logs_dir = "tests/data/diff_zipped"
    expected_log_paths = [
        "tests/data/diff_zipped/testfile1.log",
    ]

    assert get_log_files(logs_dir) == expected_log_paths


def test_dir_only_with_zipped_files():
    """
    Testcase: there are ONLY already compressed files in given directory.
    """
    logs_dir = "tests/data/only_zipped"
    expected_log_paths = []

    assert get_log_files(logs_dir) == expected_log_paths


def test_dir_with_empty_subdirs():
    """
    Testcase: there are empty subdirectories in given directory.
    """
    logs_dir = "tests/data/empty_subdir"
    expected_log_paths = [
        "tests/data/empty_subdir/testlog3",
        "tests/data/empty_subdir/testfile2.log",
        "tests/data/empty_subdir/testfile1.log",
    ]

    assert get_log_files(logs_dir) == expected_log_paths


def test_dir_with_subdirs():
    """
    Testcase: there are subdirectories with log files in given directory.
    """
    logs_dir = "tests/data/tricky_dir"
    expected_log_paths = [
        "tests/data/tricky_dir/folder_log/testfile2.log",
        "tests/data/tricky_dir/testlog3",
        "tests/data/tricky_dir/testfile1.log",
    ]

    assert get_log_files(logs_dir) == expected_log_paths
