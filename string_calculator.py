import re


def extract_delimiter(input_string):
    delimiter = ',|\n'
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
    return delimiter


def parse_numbers(numbers_str, delimiter):
    return re.split(delimiter, numbers_str)


def check_negatives(numbers):
    negatives = [num for num in numbers if num and int(num) < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(negatives)}")


def string_calculator(input_string):
    if input_string == "":
        return 0

    delimiter = extract_delimiter(input_string)
    numbers_str = input_string

    numbers = parse_numbers(numbers_str, delimiter)
    check_negatives(numbers)
    return sum(int(num) for num in numbers if num and int(num) <= 1000)
