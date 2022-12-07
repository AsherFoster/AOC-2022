def find_start_of_packet(line: str, num: int):
    for i in range(num, len(line)):
        chars = set(line[i - num:i])
        if len(chars) == num:
            return i


with open("input.txt") as input:
    for line in input:
        print("start of packet", find_start_of_packet(line[:-1], 4))
        print("start of message", find_start_of_packet(line[:-1], 14))