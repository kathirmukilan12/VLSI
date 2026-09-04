#python week01_capstone.py components.txt
import sys


def analyze_components(filename):
    x_values = []
    y_values = []
    x_buckets = {}

    try:
        with open(filename, "r") as f:
            for line_number, line in enumerate(f, start=1):
                parts = line.strip().split()

                # Ignore empty lines
                if not parts:
                    continue

                # Each line must contain: name x y
                if len(parts) != 3:
                    print(f"Warning: Line {line_number} is malformed. Skipping.")
                    continue

                name = parts[0]
                x = int(parts[1])
                y = int(parts[2])

                x_values.append(x)
                y_values.append(y)

                # Round x to nearest 10
                bucket = round(x / 10) * 10

                if bucket not in x_buckets:
                    x_buckets[bucket] = 0

                x_buckets[bucket] += 1

        # Empty file / no valid component data
        if len(x_values) == 0:
            print(f"Error: File '{filename}' contains no valid component data.")
            return

        # Manual X min/max
        min_x = x_values[0]
        max_x = x_values[0]
        total_x = 0

        for x in x_values:
            if x < min_x:
                min_x = x

            if x > max_x:
                max_x = x

            total_x += x

        # Manual Y min/max
        min_y = y_values[0]
        max_y = y_values[0]
        total_y = 0

        for y in y_values:
            if y < min_y:
                min_y = y

            if y > max_y:
                max_y = y

            total_y += y

        average_x = total_x / len(x_values)
        average_y = total_y / len(y_values)

        print("\n===== Component Analysis =====")
        print(f"File: {filename}")
        print(f"Number of components: {len(x_values)}")

        print("\nX Position:")
        print(f"Minimum X: {min_x}")
        print(f"Maximum X: {max_x}")
        print(f"Average X: {average_x}")

        print("\nY Position:")
        print(f"Minimum Y: {min_y}")
        print(f"Maximum Y: {max_y}")
        print(f"Average Y: {average_y}")

        print("\nX Position Buckets:")
        for bucket in sorted(x_buckets):
            print(f"{bucket}: {x_buckets[bucket]} component(s)")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except (IndexError, ValueError):
        print(f"Error: Invalid data found in '{filename}'.")


# -------------------------
# Main program
# -------------------------

if len(sys.argv) != 2:
    print("Usage: python week01_capstone.py <components_file>")
    sys.exit(1)

filename = sys.argv[1]

analyze_components(filename)
