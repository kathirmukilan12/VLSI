STATE_TO_BITS = {
    "S0": (1, 1, 0),
    "S1": (0, 1, 1),
    "S2": (1, 0, 1),
    "S3": (0, 0, 0),
}

BITS_TO_STATE = {
    bits: state
    for state, bits in STATE_TO_BITS.items()
}


def next_state_logic(state, bit):
    """
    Combinational next-state logic.
    """

    if state == "S0":
        return "S0" if bit == 0 else "S1"

    elif state == "S1":
        return "S0" if bit == 0 else "S2"

    elif state == "S2":
        return "S3" if bit == 0 else "S2"

    elif state == "S3":
        return "S0" if bit == 0 else "S1"

    raise ValueError(f"Invalid state: {state}")


def mealy_output_logic(state, bit):
    """
    Combinational Mealy output logic.

    Output depends directly on:
        current state + current input
    """

    if state == "S3" and bit == 1:
        return 1

    return 0


def mealy_fsm_with_dffs(input_bits):
    """
    Mealy FSM explicitly modeled using D flip-flops.

    q represents the Q outputs of the DFFs.

    Important:
        - output is combinational
        - q/state is updated at the clock edge
    """

    # Initial Q values = encoded S0
    q = STATE_TO_BITS["S0"]

    outputs = []

    for bit in input_bits:

        # ------------------------------------------------
        # CURRENT STATE
        # ------------------------------------------------

        current_state = BITS_TO_STATE[q]

        # ------------------------------------------------
        # COMBINATIONAL LOGIC
        # ------------------------------------------------

        # Mealy output:
        # current_state + current input
        output = mealy_output_logic(
            current_state,
            bit
        )

        # Next-state logic
        next_state = next_state_logic(
            current_state,
            bit
        )

        # ------------------------------------------------
        # D INPUTS
        # ------------------------------------------------

        d = STATE_TO_BITS[next_state]

        # ------------------------------------------------
        # CLOCK EDGE
        # ------------------------------------------------
        #
        # D flip-flops capture D.
        #
        q = d

        # Store output for this input cycle
        outputs.append(output)

    return outputs