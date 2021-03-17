# Count from some number start_num by another number count_by until you hit a final number end_num. Use break_num 
# as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

start_num = 0
end_num = 20
count_by = 7

# write a while loop that uses break_num as the ongoing number to 
# check against end_num

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by
    
    result = break_num

print(break_num)
