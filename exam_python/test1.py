def swap_case(input_str):
    result_str = ""
    for char in input_str:
        if char.islower():
            result_str += char.upper()
        elif char.isupper():
            result_str += char.lower()
        else:
            result_str += char
    return result_str

if __name__ == "__main__":
    input_str = input().strip()
    output_str = swap_case(input_str)
    print(output_str)

