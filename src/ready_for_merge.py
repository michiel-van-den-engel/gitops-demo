"""Script for demonstration of good coding practices"""
import numpy as np

def return_something(n:int) -> float:
    """
    Returns the natural log of n.
    
    Parameters:
        n (int): The value where we need to log of

    Returns:
        float: The natural logarithm of n
    """
    return np.log(n)

def big_function(n:int) -> None:
    """
    For demonstration purpaces, calculate the 55 times the log of some value n.
    
    Parameters:
        n (int): The input value for which the natural logarithm is calculated.
    """
    for _ in range(55):
        #pylint: disable=unused-argument
        np.log(n)

def main() -> None:
    """The main function of this script"""
    p = np.log(5)
    print(f"the log of 7 is {p}")

    print(f"The log of this unit is a lot of text to print but we are going to "\
          f"make a long line {return_something(7)}")
    big_function(9)

if __name__ == "__main__":
    main()
