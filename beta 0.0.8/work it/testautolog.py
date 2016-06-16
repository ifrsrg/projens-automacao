import sys
import json

# http://sms.playstation.com/careers/127/senior-gameplay-programmer/

# * "Design, implement, and maintain systems and tools to support gameplay
# (animation, locomotion, navigation, combat, etc.)";
# * "Write clear, maintainable, portable, and highly functional code";
# * "Expertise in C and C++"

# Why we should not lear C/C++ at IFRS?

def main():
    source = open("log.txt")
    log_file = source.readlines()
    num_size = sum(1 for line in log_file)
    data = [x for x in range(num_size)]
    date = [x for x in range(num_size)]
    temp = [x for x in range(num_size)]
    umid = [x for x in range(num_size)]

    for i in range(len(data)):
        data[i] = log_file[i]

    for i in range(len(data)):
        date[i] = (data[i][(data[i].index(':'))+1: data[i].index(';')])
        temp[i] = float(data[i][(data[i].index(':', data[i].index(':')+1)+1): data[i].index(';', data[i].index(';')+1)])
        umid[i] = float(data[i][(len(data[i])-5): (len(data[i])-2)])

    for i in range(len(data)):
        print date[i]
        print temp[i]
        print umid[i]

    final_data = [x for x in range(num_size)]

    for i in range(len(data)):
        final_data[i] = {
            "date": date[i],
            "temp": temp[i],
            "umid": umid[i]
        }

    with open("dumbster.json", "w") as f:
        for i in range(len(final_data)):
            json.dump(final_data[i], f)

if __name__ == "__main__":
    main()
