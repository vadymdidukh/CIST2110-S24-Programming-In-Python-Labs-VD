# Lab7
# Author: Vadym Didukh


## add in functions from test.py's test statements here to make the pytest work
## Use this file and your test plan to complete the lab

def calculate_rectangle_area(length: int, width: int) -> int:
    """Calculate the area of rectangle. 
    Args: 
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.
    """
    return length * width
    
def calculate_hypotenuse(a: int, b: int) -> float:
    """Calculate the Hypotenuse using the pythagorean theorem 
    Args:
        a (int): a side of triangle
        b (int): b side of triangle
    Returns:
        float: c side of triangle 
        """
    return (a ** 2 + b ** 2) ** 0.5 

def is_even(number: int) -> bool:  
    """return true or false if the number is even"""  
    return number % 2 == 0

def find_maximum(a: int, b: int) -> int:
    """find the maximum of two numbers
    Args:
        a (int): number1
        b (int): number2
    Returns:
        int: maximum of the two numbers 
        """
    return a if a > b else b

def grade_calculator(grade: int) -> str:
    """Return the letter grade for a given score
    Use the following grading scale:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    C: 50-59  

    Args:
        grade (int): grade score

    Returns:
        str: letter grade
    """
    if grade > 100 or grade < 0:
        return "Invalid Score"
    elif grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"



def main():
   #print(calculate_rectangle_area(10,20))
   #print(calculate_hypotenuse(8, 15))
   #print(is_even(11))
   #print(find_maximum(8, 15)) 
   print(grade_calculator(-5))

if __name__ == "__main__":
    main()
    

