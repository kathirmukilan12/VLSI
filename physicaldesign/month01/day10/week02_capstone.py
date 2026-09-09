# Week 2 Capstone
# JK Flip-Flop + 2-Bit Counter


# ============================================================
# 1. JK FLIP-FLOP
# ============================================================

def jk_next_state(J, K, current_Q):

    if J == 0 and K == 0:
        # HOLD
        return current_Q

    elif J == 1 and K == 0:
        # SET
        return 1

    elif J == 0 and K == 1:
        # RESET
        return 0

    elif J == 1 and K == 1:
        # TOGGLE
        return 1 - current_Q


def jk_flip_flop(clock, j_values, k_values, initial_Q=0):

    Q = initial_Q
    output = []

    previous_clock = 0

    for clk, J, K in zip(clock, j_values, k_values):

        # Rising edge: 0 -> 1
        if previous_clock == 0 and clk == 1:
            Q = jk_next_state(J, K, Q)

        output.append(Q)

        previous_clock = clk

    return output


# ============================================================
# 2. TEST JK FLIP-FLOP
# ============================================================

print("=" * 60)
print("JK FLIP-FLOP TEST")
print("=" * 60)

print("J K | Operation | Current Q | Next Q")
print("-" * 60)

test_cases = [
    (0, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 1, 0),
    (1, 1, 1),
]

for J, K, current_Q in test_cases:

    next_Q = jk_next_state(J, K, current_Q)

    if J == 0 and K == 0:
        operation = "HOLD"
    elif J == 1 and K == 0:
        operation = "SET"
    elif J == 0 and K == 1:
        operation = "RESET"
    else:
        operation = "TOGGLE"

    print(
        f"{J} {K} | "
        f"{operation:8} | "
        f"    {current_Q}     |   {next_Q}"
    )


# ============================================================
# 3. 2-BIT COUNTER USING JK FLIP-FLOPS
# ============================================================

print()
print("=" * 60)
print("2-BIT JK COUNTER")
print("=" * 60)

# Clock waveform:
# Each 0 -> 1 transition is one rising edge.
clock = [0, 1] * 10

Q0 = 0
Q1 = 0

print("Cycle | Q1 Q0 | Decimal")
print("-" * 30)

print(f"  0   |  {Q1}  {Q0}  |    0")

for cycle in range(1, 11):

    # Save OLD state.
    old_Q0 = Q0
    old_Q1 = Q1

    # --------------------------------------------------------
    # Q0:
    # J=1, K=1 -> always toggle
    # --------------------------------------------------------

    Q0 = jk_next_state(1, 1, old_Q0)

    # --------------------------------------------------------
    # Q1:
    # J=K=old_Q0
    #
    # If old Q0 = 0:
    #     J=0 K=0 -> HOLD
    #
    # If old Q0 = 1:
    #     J=1 K=1 -> TOGGLE
    # --------------------------------------------------------

    Q1 = jk_next_state(old_Q0, old_Q0, old_Q1)

    decimal_value = (Q1 << 1) | Q0

    print(
        f" {cycle:2}   |  {Q1}  {Q0}  |    {decimal_value}"
    )