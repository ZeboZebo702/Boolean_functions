def analyze_binary_file(filename):
    # counters initialization 
    total_ones = 0
    rows_with_ones = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # skip rows begin "."
                if line.startswith('.'):
                    continue
                    
                # split columns of inputs and otputs
                # and delete extra spaces
                left, right = line.strip().split()
                
                # counting "1" in the part of outputs
                ones_in_row = right.count('1')
                total_ones += ones_in_row
                
                if ones_in_row > 0:
                    rows_with_ones += 1
        
        return total_ones, rows_with_ones
        
    except FileNotFoundError:
        print(f"File {filename} does not exist")
        return None
    except Exception as e:
        print(f"The error: {str(e)}")
        return None

# Example
filename = "mult_7x7_14.txt"
#filename = "result.txt"
result = analyze_binary_file(filename)

if result:
    total_ones, rows_with_ones = result
    print(f"Common number of conjunctions: {total_ones}")
    print(f"Unique number of conjunctions: {rows_with_ones}")