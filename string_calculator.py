import re


def extract_delimiter(input_string):
    if input_string.startswith("//"):
        parts = input_string.split('\n', 1)
        delimiter_part = parts[0][2:]
        numbers_str = parts[1]
        delimiter = delimiter_part[1:-1] if delimiter_part.startswith('[') and delimiter_part.endswith(']') else delimiter_part
        delimiter = re.escape(delimiter)
        return f"{delimiter}|\n|,", numbers_str
    return ',|\n', input_string


def parse_numbers(numbers_str, delimiter):
    return [num for num in re.split(delimiter, numbers_str) if num]


def filter_numbers(numbers):
    return [int(num) for num in numbers if int(num) <= 1000]


def find_negatives(numbers):
    return [str(num) for num in numbers if num < 0]


def string_calculator(input_string):
    if not input_string:
        return 0
    delimiter, numbers_str = extract_delimiter(input_string)
    numbers = parse_numbers(numbers_str, delimiter)
    int_numbers = filter_numbers(numbers)
    negatives = find_negatives(int_numbers)
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(negatives)}")
    return sum(int_numbers)
