import unittest
from unittest.mock import mock_open, patch


def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

class TestReadLines(unittest.TestCase):

    

    
    def test_read_lines(self):
        #Mock the open function to simulate reading a file
        expected_lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
        with patch("builtins.open", mock_open(read_data="Line 1\nLine 2\nLine 3\n")) as mock_file:
            self.assertEqual(read_lines("dummy_path"), expected_lines)
            mock_file.assert_called_once_with("dummy_path", 'r')
       
        #Test reading the same file again to ensure consistent behavior with the mock
        with patch("builtins.open", mock_open(read_data="Line 1\nLine 2\nLine 3\n")) as mock_file:
            self.assertEqual(read_lines("dummy_path"), expected_lines)
            mock_file.assert_called_once_with("dummy_path", 'r')
    
    #FileNotFoundError test        
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_lines("non_existent_file.txt")
            
        

if __name__ == "__main__":
    unittest.main()