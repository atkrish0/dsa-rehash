def gcd(a, b):
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

