# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.




average_cpu = int(input("Enter the average cpu usage:"))

new_server = 40 <= average_cpu <= 70

print("You should launch a new server:",new_server)



















