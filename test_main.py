import unittest

from main import check_row, check_column, check_left_diag, check_right_diag

class TestTicTacToe(unittest.TestCase): 
    def test_check_row(self):
        board1 = [[1,2,3],[2,2,2],[2,1,7]]

        result1 = check_row(0, board1)
        self.assertFalse(result1)

        result2 = check_row(1, board1)
        self.assertTrue(result2)
        
        result3 = check_row(2, board1)
        self.assertFalse(result3)

    def test_check_column(self):
        board1 = [[1,2,3],[2,2,2],[2,2,7]]

        result1 = check_column(0, board1)
        self.assertFalse(result1)

        result2 = check_column(1, board1)
        self.assertTrue(result2)
        
        result3 = check_column(2, board1)
        self.assertFalse(result3)

    def test_check_right_diag(self):
        board1 = [[1,2,3],[2,1,2],[2,2,1]]

        result = check_right_diag(board1)
        self.assertTrue(result)
    
    def test_check_left_diag(self):
        board1 = [[1,2,1],[2,1,2],[1,2,7]]

        result = check_left_diag(board1)
        self.assertTrue(result)

    
if __name__ == "__main__":
    unittest.main()