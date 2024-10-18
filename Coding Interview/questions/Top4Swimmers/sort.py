def find_top_4_swimmers(swimmers):
    """
    Finds the top 4 swimmers with the fastest times.

    Args:
        swimmers (dict): A dictionary where keys are swimmer names and values are their times.

    Returns:
        list: A list of the top 4 swimmer names.
    """

    sorted_swimmers = sorted(swimmers.items(), key=lambda x: x[1])
    return [name for name, _ in sorted_swimmers[:4]]

if __name__ == "__main__":
    swimmers = {
        "Alice": 25.5,
        "Bob": 26.2,
        "Charlie": 24.8,
        "David": 27.1,
        "Emily": 25.9,
        "Frank": 24.5
    }

    top_4 = find_top_4_swimmers(swimmers)
    print("Top 4 swimmers:", top_4)