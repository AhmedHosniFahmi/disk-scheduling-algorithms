def get_min_distance_req(current, req_list: list):
    values = [i-current for i in req_list]
    abs_values = [abs(i) for i in values]
    min_value = min(abs_values)

    if values[abs_values.index(min_value)] < 0:
        return req_list.index(current - min_value)
    else:
        return req_list.index(min_value+current)


request_list = [int(i) for i in input("requests : ").strip().split(' ')]
current_position = int(input("enter current position : "))

done = []
seek_time = []

while request_list:
    req = request_list[get_min_distance_req(current_position, request_list)]
    seek_time.append(abs(req - current_position))
    current_position = req
    done.append(req)
    request_list.remove(req)


print("################################################")
print("request \t\tseek time\t\t")
for i in range(len(done)):
    print(done[i], '\t\t '.rjust(10), seek_time[i])

print("################################################")
total_seek_time = sum(seek_time)
print('\ntotal seek time = ', total_seek_time)
