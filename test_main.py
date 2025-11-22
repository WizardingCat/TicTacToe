import unittest

from main import check_row, check_column, check_left_diag, check_right_diag, check_board

class TestTicTacToe(unittest.TestCase): 
    board  = [["O","O","O","X"],
              ["","O","",""],
              ["X","X","O",""],
              ["X","","O","O"],]
    def test_check_row(self):

        result1 = check_row(0, self.board1)
        self.assertFalse(result1)

        result2 = check_row(1, self.board1)
        self.assertTrue(result2)
        
        result3 = check_row(2, self.board1)
        self.assertFalse(result3)

    def test_check_column(self):

        result1 = check_column(0, self.board1)
        self.assertFalse(result1)

        result2 = check_column(1, self.board1)
        self.assertTrue(result2)
        
        result3 = check_column(2, self.board1)
        self.assertFalse(result3)

    def test_check_right_diag(self):

        result = check_right_diag(self.board1)
        self.assertTrue(result)
    
    def test_check_left_diag(self):

        result = check_left_diag(self.self.board1)
        self.assertTrue(result)

    def test_check_board(self):

        result = check_board(self.board)
        self.assertTrue(result)


    
if __name__ == "__main__":
    unittest.main()