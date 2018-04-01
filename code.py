'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

input_size = int(raw_input())
output_list = []
input_list = map(int,raw_input().split(" "))
for i in range(input_size):

        x_value = -1
        y_value = -1
        if i > 0:
            for x in range(i-1,-1,-1):
                if input_list[x] > input_list[i]:
                    x_value = x+1
                    break
        for y in range(i+1,input_size):
            if input_list[y] > input_list[i]:
                y_value = y+1
                break
            
        output_list.append(x_value+y_value)
        
print " ".join([str(x) for x in output_list])

        
