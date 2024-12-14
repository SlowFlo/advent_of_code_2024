import time


def find_number_of_xmas(letters_grid: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        letters_grid = f.read()
        print("Number of XMAS:", find_number_of_xmas(letters_grid))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
