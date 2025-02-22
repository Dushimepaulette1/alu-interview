#!/usr/bin/python3
"""This module prints Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n."""
    if n <= 0:
 	return []
    
 triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
	row = [1]  # Start each row with 1 
        # Compute the inner values by summing adjacent values from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])        
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the computed row to the triangle
    
return triangle
