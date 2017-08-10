import random

symbols = ["A", "a", "B", "b", "C", "c", "D", "d", "E",
        "e", "F", "f", "G", "g", "H", "h", "I", "i", "J",
        "j", "K", "k", "L", "l", "M", "m", "N", "n", "O",
        "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T",
        "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y",
        "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8",
        "9", "0"]

def getMsgID():
    msgID = ""
    for i in range(0, 3):
        msgID += random.choice(symbols)
    return msgID

if __name__ == "__main__":
    print(getMsgID())
