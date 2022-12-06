# Day 6 - Advent of Code 2022
# The elves have provided a malfuntioning comms device.
#  Find the start of packet marker, set of 4 unique charachers,
#  in the message buffer (Parrt 1).  Next find the start of
#  message marker, set of 14 unique charachters, in the
#  message buffer (Part 2)


from collections import Counter


def read_input(f_name:str) -> str:

    with open(f_name) as f:
        return f.read().strip()


def find_marker(message:str, m_len:int) -> int:
    '''Find the start of message marker and return it's position'''

    i = m_len

    while i < len(message):
        counts = Counter(message[i-m_len:i])
        if max(counts.values()) == 1:
            return i
        i += 1

    # No marker found
    return 0


if __name__ == '__main__':

    message = read_input('input')

    # Start of Pcket Marker is 4 unique characters
    print(f'Start of packet:  {find_marker(message, 4)}')

    # Start of Message Marker is 14 unique characters
    print(f'Start of message:  {find_marker(message, 14)}')
