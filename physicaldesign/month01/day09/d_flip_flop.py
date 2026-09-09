def d_flip_flop(clock, d_values):
    q = 0
    output = []

    previous_clock = 0

    for clk, d in zip(clock, d_values):

        # Rising edge: 0 -> 1
        if previous_clock == 0 and clk == 1:
            q = d

        output.append(q)

        previous_clock = clk

    return output


# -------------------------
# Test
# -------------------------

clock = [0, 1, 1, 1, 0, 0, 1, 1]
d      = [0, 1, 0, 1, 1, 0, 0, 1]

q = d_flip_flop(clock, d)

print("CLK:", clock)
print("D:  ", d)
print("Q:  ", q)