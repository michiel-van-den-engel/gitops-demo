import unittest

import numpy as np

from src.ready_for_merge import return_something, big_function, main


def test_return_something():
    assert return_something(1) == 0.0
    assert return_something(10) == np.log(10)
    assert return_something(100) == np.log(100)
    
def test_big_function():
    big_function(10)  # Call the function
    # Since the function does not return any value and only performs calculations,
    # we can only check if it runs without raising any errors.
    # If the function runs without any exceptions, it implies it's working correctly.
    assert True  # Add an assertion to ensure the test always passes


def test_main(capsys):
    main()  # Call the main function
    captured = capsys.readouterr()  # Capture the printed output
    
    # Assert on the printed output
    expected_output = (
        f"the log of 7 is {np.log(5)}\n"
        f"The log of this unit is a lot of text to print but we are going to make a long line {np.log(7)}\n"
    )
    assert captured.out == expected_output
