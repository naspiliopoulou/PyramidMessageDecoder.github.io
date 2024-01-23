def decode(message_file):
    pyramid = []

    # Read the encoded message file
    with open(message_file, 'r') as file:
        for line in file:
            parts = line.split()
            number = int(parts[0])
            word = parts[1]
            pyramid.append((number, word))

    # Sort the pyramid based on the numbers in ascending order
    pyramid.sort(key=lambda x: x[0])

    # Extract the words corresponding to the sorted numbers
    decoded_message = ' '.join(word for _, word in pyramid)

    return decoded_message

# Example usage:
decoded_message = decode('coding_qual_input.txt')
print(decoded_message)