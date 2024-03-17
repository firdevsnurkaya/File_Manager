import unittest
import os
import shutil
from file_manager import create_directory, list_files, delete_file, rename_file

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_directory = "test_dir"
        os.makedirs(self.test_directory, exist_ok=True)
        with open(os.path.join(self.test_directory, "test_file.txt"), "w") as file:
            file.write("Test content")

    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)

    def test_create_directory(self):
        new_directory = "new_dir"
        create_directory(new_directory)
        self.assertTrue(os.path.exists(new_directory))
        
    def test_list_files(self):
        files = list_files(self.test_directory)
        self.assertIn("test_file.txt", files)
        
    def test_delete_file(self):
        file_path = os.path.join(self.test_directory, "test_file.txt")
        delete_file(file_path)
        self.assertFalse(os.path.exists(file_path))
        
    def test_rename_file(self):
        old_name = os.path.join(self.test_directory, "test_file.txt")
        new_name = os.path.join(self.test_directory, "renamed_file.txt")
        rename_file(old_name, new_name)
        self.assertTrue(os.path.exists(new_name))
        self.assertFalse(os.path.exists(old_name))

if __name__ == "__main__":
    unittest.main()
