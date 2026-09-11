# ============================================================
# day11_tests.py
# Day 11 — Moore FSM Tests
# Pattern: 1101
# ============================================================

from moore_fsm import moore_fsm
from moore_fsm_with_dffs import moore_fsm_with_dffs


# ============================================================
# TEST CASES
# ============================================================

test_cases = [
    [1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1],
]


# ============================================================
# EXPECTED OUTPUTS
# ============================================================

expected_outputs = [
    [0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1],
]


# ============================================================
# RUN TESTS
# ============================================================

print("=" * 60)
print("DAY 11 — MOORE FSM TESTS")
print("=" * 60)


for i, test in enumerate(test_cases):

    original = moore_fsm(test)

    dff_version = moore_fsm_with_dffs(test)

    expected = expected_outputs[i]

    print(f"\nTest {i + 1}")
    print("Input:      ", test)
    print("Expected:   ", expected)
    print("Moore FSM:  ", original)
    print("Moore + DFF:", dff_version)

    print(
        "Original OK:",
        original == expected
    )

    print(
        "DFF OK:     ",
        dff_version == expected
    )

    print(
        "Equivalent: ",
        original == dff_version
    )