
def save_returns(books, return_log):
    for book in books:
        book = book.strip()
        if book:
            return_log.append(book)


def process(day_file, daily_data, return_log, error_log):
    try:
        if day_file not in daily_data:
            raise FileNotFoundError(
                f"No such file: {day_file}"
            )

        books = daily_data[day_file].splitlines()
        save_returns(books, return_log)

    except FileNotFoundError as error:
        error_log.append(
            f"{day_file} | {error}"
        )

    except PermissionError as error:
        error_log.append(
            f"{day_file} | {error}"
        )

    except OSError as error:
        error_log.append(
            f"{day_file} | {error}"
        )


if __name__ == "__main__":

    daily_data = {
        "day1.txt": "Book A\nBook B",
        "day2.txt": "Book C\nBook D",
        "day3.txt": "Book E\nBook F"
    }

    return_log = []
    error_log = []

    for name in (
        "day1.txt",
        "day2.txt",
        "day3.txt",
        "missing.txt"
    ):
        process(
            name,
            daily_data,
            return_log,
            error_log
        )

    print("RETURN LOG")
    for book in return_log:
        print(book)

    if error_log:
        print("\nERROR LOG")
        for error in error_log:
            print(error)
