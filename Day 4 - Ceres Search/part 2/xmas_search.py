import time


def is_x_mas(i: int, j: int, lines: list[str]) -> bool:
    def is_within_bounds(i: int, j: int) -> bool:
        return 0 <= i < len(lines) and 0 <= j < len(lines[0])

    def get_diagonal(delta_i: int, delta_j: int) -> str:
        positions = [(i + k * delta_i, j + k * delta_j) for k in range(-1, 2)]
        if all(is_within_bounds(x, y) for x, y in positions):
            return "".join(lines[x][y] for x, y in positions)
        return ""

    directions = [
        (1, 1),  # From top-left to bottom-right
        (-1, 1),  # From bottom-left to top-right
    ]

    diagonals = [get_diagonal(di, dj) for di, dj in directions]

    count = diagonals.count("MAS")
    count += diagonals.count("SAM")

    return count == 2


def find_number_of_x_mas(letters_grid: str) -> int:
    if not isinstance(letters_grid, str):
        raise TypeError("letters_grid must be a string")

    if not letters_grid.strip():
        return 0

    lines = letters_grid.splitlines()

    count = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "A":
                if is_x_mas(i, j, lines):
                    count += 1

    return count


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        letters_grid = f.read()
        print("Number of XMAS:", find_number_of_x_mas(letters_grid))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
