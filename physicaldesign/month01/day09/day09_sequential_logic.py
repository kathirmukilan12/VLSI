def sr_latch(S, R, current_Q):
    if S == 1 and R == 1:
        raise ValueError("Invalid SR latch state")

    if S == 1:
        return 1

    if R == 1:
        return 0

    return current_Q

q = 0

q = sr_latch(1, 0, q)
print(q)   # 1

q = sr_latch(0, 0, q)
print(q)   # 1

q = sr_latch(0, 1, q)
print(q)   # 0

#sr_latch(1, 1, 0)

def d_latch(D, Enable, current_Q):
    if Enable == 1:
        return D

    return current_Q

q = 0

q = d_latch(1, 1, q)
print(q)   # 1

q = d_latch(0, 0, q)
print(q)   # Still 1

def d_flip_flop(clock, d_values):
    q = 0
    output = []

    previous_clock = 0

    for clk, d in zip(clock, d_values):

        if previous_clock == 0 and clk == 1:
            q = d

        output.append(q)

        previous_clock = clk

    return output
a=d_flip_flop([0, 1, 0, 1, 0], [0, 1, 1, 0, 1])
print(a)  