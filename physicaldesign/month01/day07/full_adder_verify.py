# full_adder_verify.py
#
# Day 7 - Full Adder Verification
#
# A full adder has:
#
# Inputs:
#   A
#   B
#   CARRY_IN
#
# Outputs:
#   SUM
#   CARRY_OUT
#
# The full adder is constructed using:
#   - Half Adder 1
#   - Half Adder 2
#   - OR gate
#
# Finally, the implementation is compared against
# a known-correct reference truth table.


# ============================================================
# 1. HALF ADDER
# ============================================================

def half_adder(a, b):
    """
    Half Adder

    Inputs:
        A
        B

    Outputs:
        SUM
        CARRY

    Equations:

        SUM   = A XOR B
        CARRY = A AND B
    """

    sum_bit = a ^ b
    carry = a & b

    return sum_bit, carry


# ============================================================
# 2. FULL ADDER
# ============================================================

def full_adder(a, b, carry_in):
    """
    Full Adder built from two Half Adders.

    Half Adder 1:
        A + B

        produces:
            SUM1
            CARRY1

    Half Adder 2:
        SUM1 + CARRY_IN

        produces:
            SUM
            CARRY2

    Final:
        CARRY_OUT = CARRY1 OR CARRY2
    """

    # First half adder
    sum1, carry1 = half_adder(a, b)

    # Second half adder
    sum_bit, carry2 = half_adder(
        sum1,
        carry_in
    )

    # Combine the two carry outputs
    carry_out = carry1 | carry2

    return sum_bit, carry_out


# ============================================================
# 3. REFERENCE TRUTH TABLE
# ============================================================

REFERENCE_TABLE = {

    # A, B, Carry_In : (Sum, Carry_Out)

    (0, 0, 0): (0, 0),

    (0, 0, 1): (1, 0),

    (0, 1, 0): (1, 0),

    (0, 1, 1): (0, 1),

    (1, 0, 0): (1, 0),

    (1, 0, 1): (0, 1),

    (1, 1, 0): (0, 1),

    (1, 1, 1): (1, 1),
}


# ============================================================
# 4. PRINT REFERENCE TABLE
# ============================================================

def print_reference_table():

    print()
    print("=" * 60)
    print("REFERENCE FULL ADDER TRUTH TABLE")
    print("=" * 60)

    print(
        " A B Cin | SUM | COUT"
    )

    print("-" * 60)

    for inputs, outputs in REFERENCE_TABLE.items():

        a, b, carry_in = inputs
        sum_bit, carry_out = outputs

        print(
            f" {a} {b}  {carry_in}  |"
            f"  {sum_bit}  |"
            f"  {carry_out}"
        )


# ============================================================
# 5. VERIFY FULL ADDER
# ============================================================

def verify_full_adder():

    print()
    print("=" * 60)
    print("FULL ADDER VERIFICATION")
    print("=" * 60)

    print(
        " A B Cin | Expected | Actual | Result"
    )

    print("-" * 60)

    passed = 0
    failed = 0

    for inputs, expected in REFERENCE_TABLE.items():

        a, b, carry_in = inputs

        # Run our implementation
        actual = full_adder(
            a,
            b,
            carry_in
        )

        if actual == expected:

            status = "PASS"
            passed += 1

        else:

            status = "FAIL"
            failed += 1

        print(
            f" {a} {b}  {carry_in}  |"
            f"   {expected}   |"
            f"  {actual}   |"
            f" {status}"
        )

    print("-" * 60)

    print(
        f"Passed: {passed}/8"
    )

    print(
        f"Failed: {failed}/8"
    )

    return failed == 0


# ============================================================
# 6. DETAILED INTERNAL VERIFICATION
# ============================================================

def show_full_adder_steps():

    print()
    print("=" * 60)
    print("FULL ADDER INTERNAL OPERATION")
    print("=" * 60)

    print(
        " A B Cin | SUM1 C1 | SUM C2 | COUT"
    )

    print("-" * 60)

    for a in [0, 1]:

        for b in [0, 1]:

            for carry_in in [0, 1]:

                # First half adder
                sum1, carry1 = half_adder(a, b)

                # Second half adder
                sum_bit, carry2 = half_adder(
                    sum1,
                    carry_in
                )

                # Final carry
                carry_out = carry1 | carry2

                print(
                    f" {a} {b}  {carry_in}  |"
                    f"   {sum1}   {carry1}  |"
                    f"  {sum_bit}  {carry2}  |"
                    f"  {carry_out}"
                )


# ============================================================
# 7. MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("FULL ADDER - RIGOROUS VERIFICATION")
    print("=" * 60)

    print()
    print("Circuit:")
    print()
    print("        A ─────┐")
    print("               │")
    print("        B ─────┤ Half Adder 1")
    print("               │")
    print("               ├── SUM1 ─────┐")
    print("               │             │")
    print("               └── CARRY1    │")
    print("                             │")
    print("        Cin ─────────────────┤ Half Adder 2")
    print("                             │")
    print("                             ├── SUM")
    print("                             │")
    print("                             └── CARRY2")
    print()
    print("        CARRY1 OR CARRY2 → CARRY_OUT")
    print()

    # Show reference
    print_reference_table()

    # Show internal circuit behavior
    show_full_adder_steps()

    # Verify implementation
    result = verify_full_adder()

    print()
    print("=" * 60)
    print("FINAL VERIFICATION RESULT")
    print("=" * 60)

    if result:

        print("FULL ADDER VERIFIED")
        print("8/8 test cases passed.")
        print()
        print(
            "The composed full-adder produces exactly "
            "the expected truth table."
        )

    else:

        print("FULL ADDER VERIFICATION FAILED")
        print(
            "At least one implementation result "
            "does not match the reference."
        )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()