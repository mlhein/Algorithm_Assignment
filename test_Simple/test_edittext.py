def replace():
    f = open('resources/positive.txt', 'r+')
    n = f.read().replace(', ', '\n') # do the job!
    f.truncate(0)                    # remove file contents from begin
    f.write(n)                       # write result into file :)
    f.close()

def lineStrip():
    with open('resources/negative.txt') as infile, open('resources/negative.txt', 'w') as outfile:
        for line in infile:
            if not line.strip():
                continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output

replace()
