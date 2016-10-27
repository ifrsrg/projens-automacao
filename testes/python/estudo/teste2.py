import sys

# SO JUST DO IT! MAKE YOUR DREAMS COME TRUE! *DO IT* NOTHING IS IMPOSSIBLE!
# DO IT! MAKE YOUR DREAMS COME TRUE! YES YOU CAN *YES YOU CAN*
# SO JUST DO IT! *TRAP*

# date, temp and umid

# >>> "abcd}def}".rfind('}')
# 8

# >>> 'hello'.rindex('l')
# 3
# >>> 'hello'.index('l')
# 2

# Isto serve para sabermos como splitar com ';' nos meios

def main():
    source = open("teste2.txt")
    data = source.readlines()

    for line in data:
        x = line.strip(';')
        date = x[0: (x.index(';'))]
        temp = x[(x.index(';')+1): (x.index(';', x.index(';')+1))]
        umid = x[((x.index(';', x.index(';')+1))+1): (x.rfind(';'))]

    print date
    print temp
    print umid

if __name__ == "__main__":
    main()
