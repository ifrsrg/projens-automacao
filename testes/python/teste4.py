import sys

#London bridge has fallen down... Has fallen down... Fallen down...
#London bridge has... Fallen down! My fair lady...
#Take the keys and lock then up! Yes! Go on, do it! Yes... Lock then up!
#Take the keys and lock then up! My fair lady...
#Everything is quite alright, sleepy tight, nighty night...
#Everything is quite alright... For my... Fair lady...

def main():
    source = open("teste4.txt")
    data = source.readlines()

    for line in data:
        with open("exploter.txt", "w") as f:
            f.write(data[0])

    source2 = open("exploter.txt")
    data2 = source2.readlines()

    for line in data2:
        x = line.strip(';')
        date = x[0: (x.index(';'))]
        temp = x[(x.index(';')+1): (x.index(';', x.index(';')+1))]
        umid = x[((x.index(';', x.index(';')+1))+1): (x.rfind(';'))]

    print date
    print temp
    print umid


if __name__ == "__main__":
    main()
