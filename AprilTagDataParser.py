def main():
    dataLines = loadFile("april_tag_results.txt")
    corners = []
    curLine = 1

    while curLine < len(dataLines):
        curLine += 2
        
        corners.insert(0, [])
        dataStrings = [dataLines[curLine][122:147]]
        curLine += 1
        for i in range(3):
            dataStrings.append(dataLines[curLine][8:34])
            curLine += 1

        for i in range(4):
            spl = dataStrings[i].split(",")
            corners[0].append([float(spl[0].strip()),float(spl[1].strip())])

    for d in corners:
        for data in d:
            print(data, sep=', ', end='')

        print()

def loadFile(file):
    try:
        with open(file) as f:
            data = f.readlines()
            return data
        
    except IOError as e:
        print("{}\nError opening {}. terminating program.".format(e, file), file = sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
