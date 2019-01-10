def melon_deliveries(day, the_file_name):
"""Displays amount of melons, melon type and melon price"""
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


"""Loops through three days and function calls melon_deliveries"""
day_num = 1
for x in range(20140519, 20140522):
    name = "um-deliveries-" + str(x) + ".txt"
    melon_deliveries(day_num,  name)
    day_num += 1
