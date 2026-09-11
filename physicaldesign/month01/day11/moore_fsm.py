def moore_fsm(input_bits):
    """
    Moore FSM for detecting overlapping 1101.

    States:
        S0 = nothing matched
        S1 = saw 1
        S2 = saw 11
        S3 = saw 110
        S4 = saw 1101

    Moore output:
        output = 1 only when current state is S4.
    """

    state = "S0"
    outputs = []

    for bit in input_bits:

        # Next-state logic
        if state == "S0":
            if bit == 0:
                state = "S0"
            else:
                state = "S1"

        elif state == "S1":
            if bit == 0:
                state = "S0"
            else:
                state = "S2"

        elif state == "S2":
            if bit == 0:
                state = "S3"
            else:
                state = "S2"

        elif state == "S3":
            if bit == 0:
                state = "S0"
            else:
                state = "S4"

        elif state == "S4":
            if bit == 0:
                state = "S0"
            else:
                state = "S2"

        else:
            raise ValueError(f"Invalid state: {state}")

        # Moore output depends ONLY on current state
        output = 1 if state == "S4" else 0

        outputs.append(output)

    return outputs