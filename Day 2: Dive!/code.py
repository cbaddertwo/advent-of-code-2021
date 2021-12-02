def part1():
    file = open ('C:\\Users\\12268\\Desktop\\AdventOfCode\\day 2\\input.txt', 'r')
    content = file.readlines()

    depth = 0
    horPos = 0

    count = 0

    cmdWord = ""

    for line in content:
        
        list = line.split()

        if(list[0] == "forward"):
            horPos = horPos + int(list[1])
        elif (list[0] == "down"):
            depth = depth + int(list[1])
        elif (list[0] == "up"):
            depth = depth - int(list[1])
        count = count + 1
    print("Part 1 Answer: ",depth*horPos)

def part2():
    file = open ('C:\\Users\\12268\\Desktop\\AdventOfCode\\day 2\\input.txt', 'r')
    content = file.readlines()

    depth = 0
    horPos = 0
    aim = 0

    count = 0

    cmdWord = ""

    for line in content:
        
        list = line.split()

        if(list[0] == "forward"):
            horPos = horPos + int(list[1])
            depth = depth + aim*int(list[1])
        elif (list[0] == "down"):
            aim = aim + int(list[1])
        elif (list[0] == "up"):
            aim = aim - int(list[1])
        count = count + 1
    print("Part 2 Answer: ", depth*horPos)

part1()
part2()
