import unittest

from main import check_row, check_column

class TestTicTacToe(unittest.TestCase): 
    def test_check_row(self):
        board1 = [[1,2,3],[2,2,2],[2,6,7]]
        
        result1 = check_row(0, board1)

        result1 = check_row(1, board1)
        self.assertTrue(result1)
        
        result1 = check_row(2, board1)
        self.assertFalse(result1)

if __name__ == "__main__":
    unittest.main()