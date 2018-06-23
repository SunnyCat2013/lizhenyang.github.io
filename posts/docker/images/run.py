with open('images.txt', 'r') as inf:
    lines = inf.readlines()
    print lines[0]
    del lines[0]
    for line in lines:
        line = line.strip().split()
        print 'docker save -o {}:{}.tar {}'.format(line[0], line[1], line[2])


