import os

import pytest


@pytest.fixture
def test_file_comment():
    yield os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files', '1_test.py')


@pytest.fixture
def test_file_exposed():
    yield os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files', '2_test.py')


@pytest.fixture
def test_file_no_instance():
    yield os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files', '3_test.py')
