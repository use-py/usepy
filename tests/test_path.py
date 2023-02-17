import pathlib
import pytest

from usepy import usePath


@pytest.fixture
def test_file():
    return usePath.mk_dirs('tests/test_dir')


def test_get_current_path():
    assert usePath.get_current_path() == pathlib.Path().absolute()


def test_mk_dirs(test_file):
    assert usePath.exists(test_file)
    usePath.mk_dirs('tests/test_dir/path')
    assert usePath.exists('tests/test_dir/path')


def test_rename():
    usePath.mk_dirs('tests/test_dir/rename')
    usePath.rename('tests/test_dir/rename', 'tests/test_dir/rename2')
    assert usePath.exists('tests/test_dir/rename2')
