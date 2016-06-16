import sys
import json

def main():
    source = open("teste.txt")
    data = source.readlines()

    for line in data:
        x = line.strip(';')
        date = x[0: (x.index(';'))]
        temp = x[(x.index(';')+1): (x.index(';', x.index(';')+1))]
        umid = x[((x.index(';', x.index(';')+1))+1): (x.rfind(';'))]

    print date
    print temp
    print umid

    date = date[(date.index(':'))+1: (len(date))]
    temp = temp[(temp.index(':'))+1: (len(temp))]
    umid = umid[(umid.index(':'))+1: (len(umid))]

    temp = float(temp)
    umid = float(umid)

    data = {
        "date": date,
        "temp": temp,
        "umid": umid
    }

    with open("data.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
