def is_invalid_id(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def sum_invalid_ids(input_line):
    total = 0
    ranges = input_line.strip().split(",")
    
    for r in ranges:
        if not r:
            continue
        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)
        
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
                
    return total

puzzle_input = ""

print("Result:", sum_invalid_ids(puzzle_input))

