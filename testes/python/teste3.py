import sys

# Work it;
# Make it;
# Do it;
# Makes us;

# Harder;
# Better;
# Faster;
# Stronger;

# Work it harder;
# Make it better;
# Do it faster;
# Makes us stronger;
# More than ever, our after hour work is never over;

# Isto serve para converter o texto de uma String em um dado.

def main():
    date_str = "date:07/07/2007"
    date = date_str[(date_str.index(':'))+1: (len(date_str))]

    temp_str = "temp:54"
    temp = temp_str[(temp_str.index(':'))+1: (len(temp_str))]

    temp = float(temp)

    umid_str = "umid:12"
    umid = umid_str[(umid_str.index(':'))+1: (len(umid_str))]

    umid = float(umid)

    print date
    print temp
    print umid
    

if __name__ == "__main__":
    main()
