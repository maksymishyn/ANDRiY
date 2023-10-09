def parser(numbers: str) -> list:
    ...


def is_arithmetic_sequence(numbers: list) -> bool:
    ...


def is_geometric_sequence(numbers: list) -> bool:
    ...


def next_arithmetic_item(numbers: list) -> int:
    ...


def next_geometric_item(numbers: list) -> int:
    ...


def get_next_item(numbers: list):
    if len(numbers) > 2:
        if is_arithmetic_sequence(numbers):
            return next_arithmetic_item(numbers)

        if is_geometric_sequence(numbers):
            return next_geometric_item(numbers)

    return None


if __name__ == '__main__':
    numbers = input('numbers>>>')
    numbers = parser(numbers)
    print(get_next_item(numbers))