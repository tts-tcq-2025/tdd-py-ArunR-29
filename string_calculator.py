import re


def string_calculator(input_string):
    if input_string == "":
        return 0

    delimiter = ',|\n'
    numbers_str = input_string

    # Custom delimiter logic
    if input_string.startswith("//"):
        parts = input_string.split('\n', 1)
        delimiter_part = parts[0][2:]
        numbers_str = parts[1]
        # Delimiter of any length: //[delimiter]\n
        if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
            delimiter = re.escape(delimiter_part[1:-1])
        else:
            delimiter = re.escape(delimiter_part)
        delimiter = f"{delimiter}|\n|,"

    numbers = re.split(delimiter, numbers_str)
    negatives = [num for num in numbers if num and int(num) < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(negatives)}")
    return sum(int(num) for num in numbers if num and int(num) <= 1000)