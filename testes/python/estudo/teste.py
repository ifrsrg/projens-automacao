import sys

# open ("FILE_NAME", 'ACTION')

# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newlines mode (deprecated)


def main():
    source = open("teste.txt")
    techs = source.readlines()

    for line in techs:
        x = line.strip(';')
        jobs = x[0: (x.index(';'))]
        gates = x[((x.index(';'))+1): (x.rfind(';'))]
        source.close()

    print jobs
    print gates

if __name__ == "__main__":
    main()
