def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci position must be non-negative")
    
    if n <= 1:
        return n
        
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
        
    return curr

def main():
    try:
        n = int(input("Enter position n to compute Fibonacci number: "))
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()