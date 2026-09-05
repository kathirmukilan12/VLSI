# Day 6 - De Morgan Verification
#
# Purpose:
# Verify Boolean transformations by comparing
# their complete truth tables.
from boolean_truth_table import generate_truth_table
def get_results(expression):
    """
    Generate only the result column
    from a Boolean expression.
    """
    variables, rows = generate_truth_table(expression)
    results = []
    for row in rows:
        results.append(row["RESULT"])
    return variables, results
def verify_equivalence(original, transformed):
    original_variables, original_results = get_results(original)
    transformed_variables, transformed_results = get_results(
        transformed
    )
    # Both expressions must contain the same variables
    if original_variables != transformed_variables:
        return False
    # Compare complete truth tables
    return original_results == transformed_results
def print_verification(number, original, transformed):
    result = verify_equivalence(
        original,
        transformed
    )
    print(f"\nTest {number}")
    print("=" * 60)
    print("Original   :", original)
    print("Transformed:", transformed)
    if result:
        print("Verification: PASS")
        print("Reason: Both truth tables are identical.")
    else:
        print("Verification: FAIL")
        print("Reason: Truth tables are different.")
if __name__ == "__main__":
    tests = [
        (
            "NOT (A AND B)",
            "(NOT A) OR (NOT B)"
        ),
        (
            "NOT (A OR B)",
            "(NOT A) AND (NOT B)"
        ),
        (
            "NOT (A AND (B OR C))",
            "(NOT A) OR ((NOT B) AND (NOT C))"
        ),
        (
            "NOT ((A OR B) AND C)",
            "((NOT A) AND (NOT B)) OR (NOT C)"
        ),
        (
            "NOT ((A AND B) OR (C AND D))",
            "((NOT A) OR (NOT B)) AND ((NOT C) OR (NOT D))"
        ),
    ]
    print("=" * 60)
    print("DE MORGAN'S LAW - TRUTH TABLE VERIFICATION")
    print("=" * 60)
    passed = 0
    for number, (original, transformed) in enumerate(
        tests,
        start=1
    ):
        print_verification(
            number,
            original,
            transformed
        )
        if verify_equivalence(
            original,
            transformed
        ):
            passed += 1
    print("\n" + "=" * 60)
    print(
        f"FINAL RESULT: {passed}/{len(tests)} tests passed"
    )
    if passed == len(tests):
        print("ALL VERIFICATIONS PASSED")
    else:
        print("SOME VERIFICATIONS FAILED")