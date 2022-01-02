from __future__ import annotations

__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


from typing import NamedTuple
from math import prod


class Packet(NamedTuple):
    version: int
    type_id: int
    n: int = -1
    packets: tuple[Packet, ...] = tuple()


def packet_decoder_part_1(input_file_path: str) -> int:
    hex_string = get_transmission(input_file_path)
    binary_string = convert_to_binary(hex_string)
    packet, _ = decode(binary_string, 0)

    return get_version_sum(packet)


def packet_decoder_part_2(input_file_path: str) -> int:
    hex_string = get_transmission(input_file_path)
    binary_string = convert_to_binary(hex_string)
    packet, _ = decode(binary_string, 0)

    return compute(packet)


def get_transmission(input_file_path: str) -> str:
    with open(input_file_path) as file:
        binary_string = [line.strip() for line in file.readlines()][0]
    return binary_string


def convert_to_binary(hd_string: str) -> str:
    conversion = {
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

    binary = ""
    for char in hd_string:
        binary += conversion[char]

    return binary


def decode(binary_string: str, index: int) -> tuple[Packet, int]:
    def read_bits(n, index) -> tuple[int, int]:
        value = int(binary_string[index : index + n], 2)
        index += n
        return value, index

    def decode_literal(index):
        n = 0
        block, index = read_bits(5, index)

        # Keep everything in the block but the leftmost bit
        n = block & 0b01111

        # Loop until the next block of bits doesn't start with a 0
        while block & 0b10000:
            block, index = read_bits(5, index)

            # Shift n over by 4 bits
            n <<= 4
            n += block & 0b01111

        return Packet(version, type_id, n=n), index

    def decode_operator_mode_0(index):
        length_subpackets, index = read_bits(15, index)
        start = index
        index += length_subpackets

        sub_packets = []
        while start < index:
            packet, start = decode(binary_string, start)
            sub_packets.append(packet)

        return Packet(version, type_id, packets=tuple(sub_packets)), index

    def decode_operator_mode_1(index):
        num_sub_packets, index = read_bits(11, index)
        sub_packets = []
        for _ in range(num_sub_packets):
            sub_packet, index = decode(binary_string, index)
            sub_packets.append(sub_packet)

        return Packet(version, type_id, packets=tuple(sub_packets)), index

    # First three bits are packet version, next three bits are typeID
    version, index = read_bits(3, index)
    type_id, index = read_bits(3, index)

    # Literal
    if type_id == 4:
        return decode_literal(index)

    # Operator
    else:
        length_type_id, index = read_bits(1, index)

        if length_type_id == 0:
            return decode_operator_mode_0(index)

        return decode_operator_mode_1(index)


def get_version_sum(packet: Packet) -> int:
    packets_stack = [packet]
    sum = 0
    while packets_stack:
        p = packets_stack.pop()
        sum += p.version
        packets_stack.extend(p.packets)

    return sum


def compute(packet: Packet) -> int:
    match packet.type_id:
        case 0:
            return sum(compute(sub_packet) for sub_packet in packet.packets)
        case 1:
            return prod(compute(sub_packet) for sub_packet in packet.packets)
        case 2:
            return min(compute(sub_packet) for sub_packet in packet.packets)
        case 3:
            return max(compute(sub_packet) for sub_packet in packet.packets)
        case 4:
            return packet.n
        case 5:
            return compute(packet.packets[0]) > compute(packet.packets[1])
        case 6:
            return compute(packet.packets[0]) < compute(packet.packets[1])
        case 7:
            return compute(packet.packets[0]) == compute(packet.packets[1])


if __name__ == "__main__":

    packet = decode(convert_to_binary("8A004A801A8002F478"), 0)[0]
    assert get_version_sum(packet) == 16
    packet = decode(convert_to_binary("620080001611562C8802118E34"), 0)[0]
    assert get_version_sum(packet) == 12
    packet = decode(convert_to_binary("C0015000016115A2E0802F182340"), 0)[0]
    assert get_version_sum(packet) == 23
    packet = decode(convert_to_binary("A0016C880162017C3686B18A3D4780"), 0)[0]
    assert get_version_sum(packet) == 31

    assert compute(decode(convert_to_binary("C200B40A82"), 0)[0]) == 3
    assert compute(decode(convert_to_binary("04005AC33890"), 0)[0]) == 54
    assert compute(decode(convert_to_binary("880086C3E88112"), 0)[0]) == 7
    assert compute(decode(convert_to_binary("CE00C43D881120"), 0)[0]) == 9

    print(f'Version sum = {packet_decoder_part_1("input.txt")}')
    print(f'Expression = {packet_decoder_part_2("input.txt")}')
