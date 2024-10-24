def xor_list(values):
    return [str(int(values[i]) ^ int(values[i + 1])) for i in range(len(values) - 1)]

def process_column(column):
    result = []
    current = column[:]  # Копируем исходный столбец
    
    result.append(current[0])
    
    while len(current) > 1:
        current = xor_list(current)
        result.append(current[0])
    
    return result

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def process_file(filename, output_filename):
    header = []
    data_rows = []
    footer = []
    
    with open(filename, 'r') as file:
        current_section = header
        for line in file:
            line = line.strip()
            if line.startswith('.') and not line.startswith('.i'):
                if line.startswith('.o') or line.startswith('.p'):
                    current_section = header
                else:
                    current_section = footer
                current_section.append(line)
            elif not line.startswith('.'):
                left, right = line.split()
                data_rows.append((left, list(right)))

    left_parts = [row[0] for row in data_rows]
    right_parts = [row[1] for row in data_rows]

    transposed_right = transpose_matrix(right_parts)

    processed_columns = []
    for column in transposed_right:
        processed_column = process_column(column)
        processed_columns.append(processed_column)

    processed_right = transpose_matrix(processed_columns)

    with open(output_filename, 'w') as file:
        # Записываем заголовок
        for line in header:
            file.write(line + '\n')
        
        for i in range(len(left_parts)):
            right_part = ''.join(processed_right[i])
            file.write(f"{left_parts[i]} {right_part}\n")
        
        for line in footer:
            file.write(line + '\n')

# Example
input_filename = "mult_7x7_14.txt"
output_filename = "mult_7x7_14_RM"
process_file(input_filename, output_filename)