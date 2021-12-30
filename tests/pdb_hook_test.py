from pdb_hook_test.check_pdb_hook import check_pdb_hook
from pdb_hook_test.check_pdb_hook import main


def test_no_strict_pass(test_file_comment):
    assert check_pdb_hook([test_file_comment]) == 0


def test_no_strict_fail(test_file_exposed):
    assert check_pdb_hook([test_file_exposed]) == 1


def test_strict_pass(test_file_no_instance):
    assert check_pdb_hook([test_file_no_instance], strict=True) == 0


def test_strict_fail(test_file_comment):
    assert check_pdb_hook([test_file_comment], strict=True) == 1


def test_integration(test_file_comment, test_file_exposed, test_file_no_instance):
    assert main(argv=[]) == 0
    assert main(argv=[test_file_comment]) == 0
    assert main(argv=[test_file_exposed]) == 1
    assert main(argv=[test_file_no_instance, '--strict']) == 0
    assert main(argv=[test_file_comment, '--strict']) == 1
