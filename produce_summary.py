def melon_deliveries(day, the_file_name):
    print(f"Day {day}")
    the_file = open(the_file_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        print(f"Delivered {count} {melon}s for total of ${amount}")   
    print("")     
    the_file.close()


dayNumber = 1
for x in range(20140519, 20140522):
    name = "um-deliveries-" + str(x) + ".txt"
    melon_deliveries(dayNumber,  name)
    dayNumber += 1
'''
melon_deliveries(1, "um-deliveries-20140519.txt")
melon_deliveries(2, "um-deliveries-20140520.txt")
melon_deliveries(3, "um-deliveries-20140521.txt")
'''
'''
for number = 20140519; until 521
     "um-deliveries" + number

print("Day 1")
the_file = open("um-deliveries-20140519.txt")


    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
'''