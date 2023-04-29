request_list = [int(i) for i in input("requests : ").strip().split(' ')]
current_position = int(input("enter current position : "))

done = []
seek_time = []

for request in request_list:
    seek_time.append(abs(current_position - request))
    current_position = request
    done.append(request)

print("################################################")
print("request \t\tseek time\t\t")
for i in range(len(done)):
    print(done[i], '\t\t '.rjust(10), seek_time[i])

print("################################################")
total_seek_time = sum(seek_time)
print('\ntotal seek time = ', total_seek_time)
