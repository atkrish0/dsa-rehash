def minimize_waiting_time(treatment_times):
    # Sort treatment times in ascending order
    treatment_times.sort()
    
    n = len(treatment_times)
    total_waiting_time = 0
    
    # Calculate waiting time
    for i in range(n):
        # Each patient waits for all patients treated before them
        # So we multiply treatment time by the number of remaining patients
        waiting_patients = n - (i + 1)
        total_waiting_time += treatment_times[i] * waiting_patients
            
    return total_waiting_time

def main():
    try:
        n = int(input("Enter number of patients: "))
        if n <= 0:
            raise ValueError("Number of patients must be positive")
        
        treatment_times = list(map(int, input("Enter treatment times separated by space: ").split()))
        if len(treatment_times) != n:
            raise ValueError(f"Expected {n} treatment times, got {len(treatment_times)}")
            
        result = minimize_waiting_time(treatment_times)
        print(f"Minimum total waiting time: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()