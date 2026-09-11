# ============================================================
# moore_fsm_with_dffs.py
# Day 11 — Moore FSM using D Flip-Flops
# Pattern: 1101
# ============================================================


# ============================================================
# STATE ENCODING
# ============================================================
#
# We have 5 logical states:
#
# S0 = nothing matched
# S1 = saw 1
# S2 = saw 11
# S3 = saw 110
# S4 = saw 1101
#
# Each state is encoded using 3 D flip-flops.
#
# Q2 Q1 Q0
# ------------------------------------------------
# S0 = 110
# S1 = 011
# S2 = 101
# S3 = 000
# S4 = 111
#
# ============================================================

STATE_TO_BITS = {
    "S0": (1, 1, 0),
    "S1": (0, 1, 1),
    "S2": (1, 0, 1),
    "S3": (0, 0, 0),
    "S4": (1, 1, 1),
}


# Reverse lookup:
# physical Q bits → logical FSM state

BITS_TO_STATE = {
    bits: state
    for state, bits in STATE_TO_BITS.items()
}


# ============================================================
# NEXT-STATE LOGIC
# ============================================================

def next_state_logic(state, bit):

    if state == "S0":

        if bit == 0:
            return "S0"
        else:
            return "S1"

    elif state == "S1":

        if bit == 0:
            return "S0"
        else:
            return "S2"

    elif state == "S2":

        if bit == 0:
            return "S3"
        else:
            return "S2"

    elif state == "S3":

        if bit == 0:
            return "S0"
        else:
            return "S4"

    elif state == "S4":

        if bit == 0:
            return "S0"
        else:
            return "S2"

    raise ValueError(f"Invalid state: {state}")


# ============================================================
# MOORE OUTPUT LOGIC
# ============================================================
#
# Moore output depends ONLY on the current state.
#
# S4 = pattern 1101 detected
#
# Therefore:
#
# S4 → output 1
# All other states → output 0
#
# ============================================================

def moore_output_logic(state):

    if state == "S4":
        return 1

    return 0


# ============================================================
# MOORE FSM USING D FLIP-FLOPS
# ============================================================

def moore_fsm_with_dffs(input_bits):

    # --------------------------------------------------------
    # Initial state
    # --------------------------------------------------------
    #
    # Q outputs of the D flip-flops initially represent S0.
    #
    q = STATE_TO_BITS["S0"]

    outputs = []

    for bit in input_bits:

        # ----------------------------------------------------
        # 1. Read CURRENT Q values
        # ----------------------------------------------------
        #
        # The physical Q bits represent the current state.
        #

        current_state = BITS_TO_STATE[q]

        # ----------------------------------------------------
        # 2. Calculate NEXT STATE
        # ----------------------------------------------------
        #
        # This is combinational logic.
        #

        next_state = next_state_logic(
            current_state,
            bit
        )

        # ----------------------------------------------------
        # 3. Calculate D inputs
        # ----------------------------------------------------
        #
        # Encode the next state into DFF inputs.
        #

        d = STATE_TO_BITS[next_state]

        # ----------------------------------------------------
        # 4. CLOCK EDGE
        # ----------------------------------------------------
        #
        # D flip-flops capture D.
        #
        # In real hardware:
        #
        #       D ──→ DFF ──→ Q
        #              ↑
        #             CLK
        #
        # ----------------------------------------------------

        q = d

        # ----------------------------------------------------
        # 5. Moore OUTPUT
        # ----------------------------------------------------
        #
        # Output depends ONLY on the CURRENT state.
        #
        # After the clock edge, q represents next_state.
        #

        current_state = BITS_TO_STATE[q]

        output = moore_output_logic(
            current_state
        )

        outputs.append(output)

    return outputs


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    test_cases = [
        [1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1],
    ]

    for test in test_cases:

        result = moore_fsm_with_dffs(test)

        print("Input: ", test)
        print("Output:", result)
        print()