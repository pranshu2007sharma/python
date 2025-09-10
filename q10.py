import math

class Point:
    # Constructor to initialize the coordinates
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Method to print the coordinates of the point
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # Method to calculate the distance between two points
    def distance(self, other):
        # Calculate Euclidean distance between self and another point
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Example usage
point1 = Point(3, 4)
point2 = Point(6, 8)

# Print the points
print("Point 1:", point1)
print("Point 2:", point2)

# Calculate the distance between the two points
dist = point1.distance(point2)
print(f"Distance between {point1} and {point2} is: {dist}")
