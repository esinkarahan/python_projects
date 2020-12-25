# perform unit tests whether get_winner function is working properly
from tictactoe_2players import new_board, get_winner, render

def report_test_result(expected_winner,actual_winner,ntest):
    if expected_winner == actual_winner:
        print ("PASSED " + str(ntest))
    else:
        print ("FAILED " + str(ntest) + "!")
        print ("Expected:{}".format(expected_winner))
        print ("Actual:{}".format(actual_winner))

if __name__ == "__main__":
    #Test 1: no winners
    test1 = new_board()
    render(test1)
    expected_winner = 0
    actual_winner = get_winner(test1)
    report_test_result(expected_winner, actual_winner, 1)

    #Test 2: horizontal winner
    test2 = [['O','X',None],
             ['O','O','O'],
             [None, None, None]]
    render(test2)
    expected_winner = 'O'
    actual_winner = get_winner(test2)
    report_test_result(expected_winner, actual_winner, 2)

    #Test 3: vertical winner
    test3 = [['X','X',None],
             ['X','X',None],
             ['X', None, None]]
    render(test3)
    expected_winner = 'X'
    actual_winner = get_winner(test3)
    report_test_result(expected_winner, actual_winner, 3)

    #Test 4: diagonal winner
    test4 = [['X','X',None],
             ['X','X',None],
             ['O', None, 'X']]
    render(test4)
    expected_winner = 'X'
    actual_winner = get_winner(test4)
    report_test_result(expected_winner, actual_winner, 4)