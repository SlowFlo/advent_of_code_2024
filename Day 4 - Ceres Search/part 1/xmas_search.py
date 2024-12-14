import time


def lines_to_columns(text: str) -> str:
    lignes = text.splitlines()
    # We group each Nth letter of each line together
    colonnes = zip(*lignes)
    return "\n".join("".join(colonne) for colonne in colonnes)


def lines_to_diagonals(text: str) -> str:
    lines = text.splitlines()
    height = len(lines)
    width = len(lines[0])

    diagonals = [[] for _ in range(height + width - 1)]

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            diagonals[i + j].append(char)

    result = "\n".join("".join(reversed(diagonal)) for diagonal in diagonals)
    return result


def count_xmas_in_lines(grid: str) -> int:
    return grid.count("XMAS") + grid[::-1].count("XMAS")


def find_number_of_xmas(letters_grid: str) -> int:
    if not isinstance(letters_grid, str):
        raise TypeError("letters_grid must be a string")

    if not letters_grid.strip():
        return 0

    transposed_grid = lines_to_columns(letters_grid)
    diagonals = lines_to_diagonals(letters_grid)
    reversed_lines = "\n".join([line[::-1] for line in letters_grid.splitlines()])
    reversed_diagonals = lines_to_diagonals(reversed_lines)

    return (
        count_xmas_in_lines(letters_grid)
        + count_xmas_in_lines(diagonals)
        + count_xmas_in_lines(transposed_grid)
        + count_xmas_in_lines(reversed_diagonals)
    )


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        letters_grid = f.read()
        print("Number of XMAS:", find_number_of_xmas(letters_grid))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
