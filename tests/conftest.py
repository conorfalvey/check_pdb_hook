import os

import pytest


@pytest.fixture
def test_file_comment():
    yield os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test_files', 'test1.py'))


@pytest.fixture
def test_file_exposed():
    yield os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test_files', 'test2.py'))


@pytest.fixture
def test_file_no_instance():
    yield os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test_files', 'test3.py'))
