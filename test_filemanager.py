import os
import shutil

def test_mkdir():
    os.mkdir('test_folder')
    assert 'test_folder' in os.listdir()
    os.rmdir('test_folder')

def test_rmdir():
    os.mkdir('test_folder_2')
    assert 'test_folder_2' in os.listdir()
    os.rmdir('test_folder_2')
    assert 'test_folder_2' not in os.listdir()

def test_shutil_copy():
    shutil.copy('main.py', 'test_main_copy.py')
    assert os.path.exists('test_main_copy.py')
    os.remove('test_main_copy.py')

