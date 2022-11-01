# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

def decode(stng):
    decoded = ""
    currentNo = ""
    for letter in stng:
        if letter.isnumeric():
            currentNo+=letter
        else:
            for x in range(int(currentNo)):
                decoded+=letter
            currentNo=""


    return decoded

def encode(stng):
    encoded = ""
    cLetter = stng[0]
    cNo = 0
    for letter in stng:
        if(cLetter==letter):
            cNo+=1
        else:
            encoded +=str(cNo)
            encoded +=cLetter
            cLetter = letter
            cNo=1
    encoded +=str(cNo)
    encoded +=cLetter
    return encoded

def main():
    stng = "AAAABBBCCDAA"
    stng = encode(stng)
    print(stng)
    stng = decode(stng)
    print(stng)
    pass

if __name__ == "__main__":
    main()