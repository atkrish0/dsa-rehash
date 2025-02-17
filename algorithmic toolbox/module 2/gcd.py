def gcd(a, b):
    """
    Compute the Greatest Common Divisor using Euclidean algorithm.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: Greatest common divisor of a and b
        
    Raises:
        ValueError: If either number is negative
    """
    if a < 0 or b < 0:
        raise ValueError("Numbers must be non-negative")
        
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        # Get input from user
        a, b = map(int, input("Enter two non-negative integers separated by space: ").split())
        result = gcd(a, b)
        print(f"GCD({a}, {b}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()