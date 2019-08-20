import sys

print(sys.argv)

if len(sys.argv) != 2:
    print("usage: file.py <filename>", file=sys.stderr)
    sys.exit(1)

filepath = sys.argv[1]

try:
    with open(filepath) as f:
        for line in f:
            # print(line)
            
            # now want to parse each line
            # split before and after comment symbol
            comment_split = line.split("#")

            # convert pre-comment portion from binary to dec value
            # strip() removes extra white space that may be present
            num = comment_split[0].strip() 

            # ignore blanks
            if num == "":
                continue

            x = int(num, 2) # base 2
            # print(x)
            print(f"{x:08b}: {x}")



except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)

