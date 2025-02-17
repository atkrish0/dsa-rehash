def fibonacci(n):
    """
    Compute the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The position of Fibonacci number to compute (n >= 0)
    
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci position must be non-negative")
    
    # Base cases
    if n <= 1:
        return n
    
    # Initialize array to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1
    
    # Compute subsequent numbers
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
        
    return fib[n]

def main():
    try:
        n = int(input("Enter position n to compute Fibonacci number: "))
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()