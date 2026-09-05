# kmap_grid.py
#
# Day 8 - K-map Grid Printer
#
# Purpose:
#   Convert a 16-entry truth table into a 4-variable
#   K-map layout using Gray-code ordering.
#
# Important:
#   This program ONLY prints the K-map.
#   It does NOT perform minimization.


# Gray-code ordering
# Binary order would be:
# 00, 01, 10, 11
#
# K-map order is:
# 00, 01, 11, 10

GRAY = [0, 1, 3, 2]


def print_kmap(values):
    """
    Print a 4-variable K-map.

    values:
        A list containing exactly 16 output values.

    The input values must be in normal binary order:

        0000 -> index 0
        0001 -> index 1
        0010 -> index 2
        ...
        1111 -> index 15

    K-map output uses Gray-code ordering:

             CD
          00 01 11 10
        +---+---+---+---+
    00  |   |   |   |   |
        +---+---+---+---+
    01  |   |   |   |   |
        +---+---+---+---+
    11  |   |   |   |   |
        +---+---+---+---+
    10  |   |   |   |   |
        +---+---+---+---+
    """

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if len(values) != 16:
        raise ValueError(
            "A 4-variable K-map requires exactly 16 values."
        )

    # Make sure values are only 0 or 1
    for value in values:
        if value not in [0, 1]:
            raise ValueError(
                "Truth-table values must be 0 or 1."
            )

    # --------------------------------------------------------
    # Print heading
    # --------------------------------------------------------

    print()
    print("4-Variable K-Map")
    print()

    print("          CD")
    print("       00  01  11  10")
    print("     +---+---+---+---+")

    # --------------------------------------------------------
    # Build the K-map
    # --------------------------------------------------------

    for ab in GRAY:

        row = []

        for cd in GRAY:

            # Convert:
            #
            # AB = row
            # CD = column
            #
            # into the original 4-bit binary index.
            #
            # Example:
            #
            # AB = 01
            # CD = 11
            #
            # gives:
            #
            # A B C D
            # 0 1 1 1
            #
            # binary = 0111
            # index  = 7

            index = (ab << 2) | cd

            row.append(values[index])

        print(
            f"{format(ab, '02b')}  | "
            f" {row[0]} | {row[1]} | {row[2]} | {row[3]} |"
        )

        print("     +---+---+---+---+")


# ============================================================
# Example
# ============================================================

if __name__ == "__main__":

    # Example truth table.
    #
    # These are the outputs for:
    #
    # A B C D
    #
    # 0000 -> 0
    # 0001 -> 0
    # 0010 -> 0
    # 0011 -> 1
    # 0100 -> 0
    # 0101 -> 1
    # 0110 -> 0
    # 0111 -> 1
    # 1000 -> 0
    # 1001 -> 0
    # 1010 -> 0
    # 1011 -> 1
    # 1100 -> 0
    # 1101 -> 1
    # 1110 -> 0
    # 1111 -> 1

    values = [
        0, 0, 0, 1,
        0, 1, 0, 1,
        0, 0, 0, 1,
        0, 1, 0, 1
    ]

    print_kmap(values)