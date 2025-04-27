grid = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

def is_plus_possible(row, col):
    """Check if a plus sign can be formed centered at (row, col)"""
   
    return (col > 0) and (col < 3) and (row < 2)

def get_plus_numbers(row, col):
    """Get the 5 numbers that form the plus sign"""
    return [
        grid[row][col],       
        grid[row+1][col-1],  
        grid[row+1][col],     
        grid[row+1][col+1],   
        grid[row+2][col]      
    ]


print("Finding all possible plus signs in the grid:")
for row in range(4):
    for col in range(4):
        if is_plus_possible(row, col):
            numbers = get_plus_numbers(row, col)
            total = sum(numbers)
            
            print(f"\nPlus centered at {grid[row][col]} (position: row {row}, column {col})")
            print(f"Numbers: Center={numbers[0]}, Left={numbers[1]}, Middle={numbers[2]}, Right={numbers[3]}, Bottom={numbers[4]}")
            print(f"Total sum: {total}")