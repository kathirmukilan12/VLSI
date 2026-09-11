# ============================================================
# day12_tests.py
# Day 12 — Mealy FSM Tests
# Pattern: 1101
# ============================================================

from mealy_fsm import mealy_fsm
from mealy_fsm_with_dffs import mealy_fsm_with_dffs


# ============================================================
# TEST CASES
# Same 3 inputs used on Day 11
# ============================================================

test_cases = [
    [1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1],
]


# ============================================================
# PREDICTIONS
# ============================================================
#
# IMPORTANT:
# These predictions are made BEFORE running the FSM.
#
# Test 1:
# 1101 detected at bit 4
#
# Test 2:
# 1101 detected at bit 6
#
# Test 3:
# 1101 detected at bits 4 and 7
#
# ============================================================

predicted_outputs = [
    [0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1],
]


# ============================================================
# BLOCK 1 — SHOW PREDICTIONS
# ============================================================

print("=" * 60)
print("DAY 12 — PREDICTIONS")
print("=" * 60)


for i, test in enumerate(test_cases):

    print(f"\nTest {i + 1}")
    print("Input:     ", test)
    print("Prediction:", predicted_outputs[i])


# ============================================================
# BLOCK 2 — RUN AFTER PREDICTION
# ============================================================

print("\n")
print("=" * 60)
print("DAY 12 — ACTUAL RESULTS")
print("=" * 60)


for i, test in enumerate(test_cases):

    # --------------------------------------------------------
    # Run Moore
    # --------------------------------------------------------

    # --------------------------------------------------------
    # Run basic Mealy
    # --------------------------------------------------------

    mealy_output = mealy_fsm(test)

    # --------------------------------------------------------
    # Run Mealy composed from DFFs
    # --------------------------------------------------------

    mealy_dff_output = mealy_fsm_with_dffs(test)

    # --------------------------------------------------------
    # Expected prediction
    # --------------------------------------------------------

    prediction = predicted_outputs[i]

    print(f"\nTest {i + 1}")

    print("Input:        ", test)
    print("Prediction:   ", prediction)
    print("Mealy:        ", mealy_output)
    print("Mealy + DFF:  ", mealy_dff_output)

    # --------------------------------------------------------
    # Prediction vs actual
    # --------------------------------------------------------

    print(
        "Prediction OK:",
        prediction == mealy_output
    )

    # --------------------------------------------------------
    # Moore vs Mealy
    # --------------------------------------------------------

    # --------------------------------------------------------
    # Mealy vs DFF implementation
    # --------------------------------------------------------

    print(
        "Mealy == DFF:  ",
        mealy_output == mealy_dff_output
    )