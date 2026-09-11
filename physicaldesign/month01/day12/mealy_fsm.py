def mealy_fsm(input_bits):
    """
    Mealy FSM for detecting overlapping 1101.

    States:
        S0 = nothing matched
        S1 = saw 1
        S2 = saw 11
        S3 = saw 110

    Mealy output:
        output = 1 when current_state == S3
                 and current input == 1

    Pattern detected:
        1101
    """

    state = "S0"
    outputs = []

    for bit in input_bits:

        # S0: nothing matched
        if state == "S0":
            if bit == 0:
                state = "S0"
                output = 0
            else:
                state = "S1"
                output = 0

        # S1: saw 1
        elif state == "S1":
            if bit == 0:
                state = "S0"
                output = 0
            else:
                state = "S2"
                output = 0

        # S2: saw 11
        elif state == "S2":
            if bit == 0:
                state = "S3"
                output = 0
            else:
                state = "S2"
                output = 0

        # S3: saw 110
        elif state == "S3":
            if bit == 0:
                state = "S0"
                output = 0
            else:
                # 110 + 1 = 1101
                # Pattern detected.
                output = 1

                # The final 1 can begin another 1101.
                state = "S1"

        else:
            raise ValueError(f"Invalid state: {state}")

        outputs.append(output)

    return outputs