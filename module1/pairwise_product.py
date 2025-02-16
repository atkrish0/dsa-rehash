def max_pairwise_product(numbers):
    n = len(numbers)
    if n < 2:
        raise ValueError("The input list must contain at least two numbers.")
    
    # Find the indices of the two largest numbers
    index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i
    
    index2 = 1 if index1 == 0 else 0
    for i in range(n):
        if i != index1 and numbers[i] > numbers[index2]:
            index2 = i
    
    return numbers[index1] * numbers[index2]

if __name__ == "__main__":
    input_numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Max pairwise product:", max_pairwise_product(input_numbers))