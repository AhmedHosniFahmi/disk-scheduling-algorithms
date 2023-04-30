def get_new_arranged_list(curr_pos: int, direct: str, req_list: list, start: int, last: int) -> list:
    smaller_than_current = []
    greater_than_current = []
    for req in req_list:
        if curr_pos > req:
            smaller_than_current.append(req)
        else:
            greater_than_current.append(req)
    if direct == '-':
        return sorted(smaller_than_current, reverse=True) + [start] + sorted(greater_than_current)
    else:
        return sorted(greater_than_current) + [last] + sorted(smaller_than_current, reverse=True)


lis = []
num_of_queues = int(input("enter number of queues : "))

for i in range(num_of_queues):
    lis.append(int(j) for j in input(f"requests for queue ({i+1}): ").strip().split(' '))

current_position = int(input("enter current position : "))

direction = str(input("(-) or (+) direction : ")).strip()

number_of_cylinders = int(input("num of cylinders : "))

done = []
seek_time = []

for queue in lis:
    request_list = get_new_arranged_list(current_position, direction, queue, 0, number_of_cylinders - 1)
    for request in request_list:
        seek_time.append(abs(current_position - request))
        current_position = request
        done.append(request)

print("################################################")
print("request \t\tseek time\t\t")
for i in range(len(done)):
    print(done[i], '\t\t '.rjust(15), seek_time[i])

print("################################################")
total_seek_time = sum(seek_time)
print('\ntotal seek time = ', total_seek_time)
