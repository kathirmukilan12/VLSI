def four_bit_counter(cycles):

    # q = [Q0, Q1, Q2, Q3]
    q = [0, 0, 0, 0]

    print("Cycle  0: 0000 = 0")

    for cycle in range(1, cycles + 1):

        # Calculate NEXT state
        q0_next = q[0] ^ 1
        q1_next = q[1] ^ q[0]
        q2_next = q[2] ^ (q[0] & q[1])
        q3_next = q[3] ^ (q[0] & q[1] & q[2])

        # All flip-flops update together
        q = [q0_next, q1_next, q2_next, q3_next]

        # Display as Q3 Q2 Q1 Q0
        binary = f"{q[3]}{q[2]}{q[1]}{q[0]}"

        decimal = (
            q[3] * 8 +
            q[2] * 4 +
            q[1] * 2 +
            q[0]
        )

        print(f"Cycle {cycle:2}: {binary} = {decimal}")


four_bit_counter(20)