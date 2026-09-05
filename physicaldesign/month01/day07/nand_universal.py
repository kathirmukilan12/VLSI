# nand_universal.py
#
# Day 7 - Proving NAND is a Universal Gate
#
# We will build:
#   NOT using NAND
#   AND using NAND
#   OR  using NAND
#
# Then we verify each construction using truth tables.


# ============================================================
# 1. PRIMITIVE NAND GATE
# ============================================================

def nand(a, b):
    """
    NAND gate.

    NAND(A, B) = NOT(A AND B)

    Truth table:
        A B | NAND
        ----------
        0 0 |  1
        0 1 |  1
        1 0 |  1
        1 1 |  0
    """

    return int(not (a and b))


# ============================================================
# 2. BUILD NOT USING ONLY NAND
# ============================================================

def nand_not(a):
    """
    NOT A using NAND only.

    A NAND A
    = NOT(A AND A)
    = NOT A
    """

    return nand(a, a)


# ============================================================
# 3. BUILD AND USING ONLY NAND
# ============================================================

def nand_and(a, b):
    """
    AND using NAND only.

    Step 1:
        temp = A NAND B
              = NOT(A AND B)

    Step 2:
        temp NAND temp
        = NOT(temp AND temp)
        = NOT(temp)
        = A AND B
    """

    temp = nand(a, b)

    return nand(temp, temp)


# ============================================================
# 4. BUILD OR USING ONLY NAND
# ============================================================

def nand_or(a, b):
    """
    OR using NAND only.

    By De Morgan:

        A OR B
        = NOT(NOT A AND NOT B)

    Using NAND:

        NOT A = A NAND A
        NOT B = B NAND B

    Therefore:

        A OR B
        = (A NAND A) NAND (B NAND B)
    """

    not_a = nand(a, a)
    not_b = nand(b, b)

    return nand(not_a, not_b)


# ============================================================
# 5. ORIGINAL GATES
#
# These are reference implementations.
# They are NOT used inside the NAND-built gates.
# ============================================================

def original_not(a):
    """Reference NOT gate."""

    return int(not a)


def original_and(a, b):
    """Reference AND gate."""

    return int(a and b)


def original_or(a, b):
    """Reference OR gate."""

    return int(a or b)


# ============================================================
# 6. VERIFY NOT
# ============================================================

def verify_not():

    print()
    print("=" * 60)
    print("VERIFY: NOT USING ONLY NAND")
    print("=" * 60)

    print(" A | Original NOT | NAND-built NOT | Result")
    print("-" * 60)

    passed = 0

    for a in [0, 1]:

        expected = original_not(a)
        actual = nand_not(a)

        if expected == actual:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"

        print(
            f" {a} |"
            f"      {expected}       |"
            f"       {actual}       |"
            f" {status}"
        )

    print("-" * 60)
    print(f"NOT verification: {passed}/2 passed")

    return passed == 2


# ============================================================
# 7. VERIFY AND
# ============================================================

def verify_and():

    print()
    print("=" * 60)
    print("VERIFY: AND USING ONLY NAND")
    print("=" * 60)

    print(" A B | Original AND | NAND-built AND | Result")
    print("-" * 60)

    passed = 0

    for a in [0, 1]:

        for b in [0, 1]:

            expected = original_and(a, b)
            actual = nand_and(a, b)

            if expected == actual:
                status = "PASS"
                passed += 1
            else:
                status = "FAIL"

            print(
                f" {a} {b} |"
                f"      {expected}      |"
                f"       {actual}       |"
                f" {status}"
            )

    print("-" * 60)
    print(f"AND verification: {passed}/4 passed")

    return passed == 4


# ============================================================
# 8. VERIFY OR
# ============================================================

def verify_or():

    print()
    print("=" * 60)
    print("VERIFY: OR USING ONLY NAND")
    print("=" * 60)

    print(" A B | Original OR | NAND-built OR | Result")
    print("-" * 60)

    passed = 0

    for a in [0, 1]:

        for b in [0, 1]:

            expected = original_or(a, b)
            actual = nand_or(a, b)

            if expected == actual:
                status = "PASS"
                passed += 1
            else:
                status = "FAIL"

            print(
                f" {a} {b} |"
                f"      {expected}     |"
                f"      {actual}      |"
                f" {status}"
            )

    print("-" * 60)
    print(f"OR verification: {passed}/4 passed")

    return passed == 4


# ============================================================
# 9. MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("NAND UNIVERSAL GATE VERIFICATION")
    print("=" * 60)

    print()
    print("Goal:")
    print("Build NOT, AND and OR using ONLY NAND.")
    print()

    not_passed = verify_not()

    and_passed = verify_and()

    or_passed = verify_or()

    print()
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print(
        f"NAND -> NOT : "
        f"{'PASS' if not_passed else 'FAIL'}"
    )

    print(
        f"NAND -> AND : "
        f"{'PASS' if and_passed else 'FAIL'}"
    )

    print(
        f"NAND -> OR  : "
        f"{'PASS' if or_passed else 'FAIL'}"
    )

    print()

    if not_passed and and_passed and or_passed:

        print("ALL TESTS PASSED")
        print()
        print("Conclusion:")
        print("NAND is a universal gate.")
        print(
            "NOT, AND and OR can all be constructed "
            "using NAND alone."
        )

    else:

        print("SOME TESTS FAILED")
        print("Check the NAND implementations.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()