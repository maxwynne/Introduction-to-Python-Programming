# Count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num

start_num = 10
end_num = 5
count_by = 5
break_num = 101

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
# check against end_num

if start_num > end_num:
    print("Oops! Looks like your start value is greater than the end value. Please try again")

else:
    while break_num <= end_num:
      break_num += count_by
      
      result = break_num

print(break_num)
