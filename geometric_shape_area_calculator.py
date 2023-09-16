#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('Welcome to the geometric shape area calculator!')
    # User Options
    # Circle = 1
    # Rectangle = 2
    # Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle = 1' + ' ' + 'Rectangle = 2' + ' ' + 'Triangle = 3')
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input('Select a shape by entering 1, 2, or 3: ')
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type(choice) == int)
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input("Enter the radius of the circle: ")
        # TODO: Convert 'radius' to float.
        radius = float(radius)
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = circle_pi * radius ** 2
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input("Enter the length of the rectangle: ")
        width = input("Enter the width of the rectangle: ")
        # TODO: Convert both 'length' and 'width' to float.
        length = float(length)
        width = float(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = length * width
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input("Enter the base length of the triangle: ")
        height = input("Enter the height of the triangle: ")
        # TODO: Convert both 'base' and 'height' to float.
        base = float(base)
        height = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = (.5*base) * height
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print('Invalid choice .')
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    steps = '''
    # Steps for Completing Technical Assignments:

    # 1. Clone the GitHub repository to local machine.
    # 2. Ensure that the repository is successfully cloned.
    # 3. Define variables for various shapes, ensuring they are enclosed in quotes.
    # 4. Utilize the input function to gather user inputs and assign them to variables.
    # 5. Convert user inputs to the appropriate data types (e.g., float, int).
    # 6. Verify if the converted inputs are of the correct data type using conditional checks.
    # 7. Calculate the area for different shapes based on user input.
    # 8. Display the calculated area to the user.
    # 9. Implement error handling for invalid choices
    '''
    print(steps)

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY

