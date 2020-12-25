# do unit tests to check whether next state is switched correctly
from game_of_life import next_board_state

def report_test_result(expected_next_state,actual_next_state,ntest):
    if expected_next_state == actual_next_state:
        print ("PASSED " + str(ntest))
    else:
        print ("FAILED " + str(ntest) + "!")
        print ("Expected:")
        print (expected_next_state)
        print ("Actual:")
        print (actual_next_state)


if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)
    report_test_result(expected_next_state1, actual_next_state1, 1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)
    report_test_result(expected_next_state2, actual_next_state2, 2)

    # TEST 3
    # alive cells with more than 3 neighbours should die due to overpopulation
    init_state3 = [
        [0,1,1],
        [1,1,1],
        [0,0,0]
    ]
    expected_next_state3 = [
        [1,0,1],
        [1,0,1],
        [0,1,0]
    ]
    actual_next_state3 = next_board_state(init_state3)
    report_test_result(expected_next_state3, actual_next_state3, 3)

    # TEST 4
    # any live cell with less than 2 neighbours should die: underpopulation
    init_state4 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected_next_state4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    actual_next_state4 = next_board_state(init_state4)
    report_test_result(expected_next_state4, actual_next_state4, 4)
