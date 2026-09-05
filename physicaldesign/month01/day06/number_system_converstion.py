# Day 6 - Number Systems
# Binary / Decimal / Hexadecimal conversions
def dec_to_bin(n):
    """Convert decimal integer to binary without using bin()."""
    if n == 0:
        return "0"
    if n < 0:
        return "-" + dec_to_bin(-n)
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n // 2
    bits.reverse()
    return "".join(bits)
def bin_to_dec(s):
    """Convert binary string to decimal without using int(s, 2)."""
    s = s.strip()
    if not s:
        raise ValueError("Binary string cannot be empty.")
    negative = False
    if s[0] == "-":
        negative = True
        s = s[1:]
    if not s:
        raise ValueError("Invalid binary number.")
    result = 0
    for bit in s:
        if bit not in "01":
            raise ValueError(f"Invalid binary digit: {bit}")
        result = result * 2 + int(bit)
    return -result if negative else result
def hex_to_bin(s):
    """Convert hexadecimal string to binary."""
    s = s.strip().upper()
    if s.startswith("0X"):
        s = s[2:]
    hex_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    result = ""
    for digit in s:
        if digit not in hex_map:
            raise ValueError(f"Invalid hexadecimal digit: {digit}")
        result += hex_map[digit]
    return result
if __name__ == "__main__":
    print("DECIMAL → BINARY")
    print("-----------------")
    numbers = [7, 12, 19, 25, 31, 42, 50, 64, 100, 127]
    for number in numbers:
        print(f"{number:3} → {dec_to_bin(number)}")
    print()
    print("BINARY → DECIMAL")
    print("-----------------")
    binary_numbers = [
        "111",
        "1100",
        "10011",
        "11001",
        "11111",
        "101010",
        "110010",
        "1000000",
        "1100100",
        "1111111",
    ]
    for binary in binary_numbers:
        print(f"{binary:8} → {bin_to_dec(binary)}")
    print()
    print("HEX → BINARY")
    print("------------")
    hex_values = ["A", "F", "2B", "7C", "D5"]
    for value in hex_values:
        print(f"{value:3} → {hex_to_bin(value)}")