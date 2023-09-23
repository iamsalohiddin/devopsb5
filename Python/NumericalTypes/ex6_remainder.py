# A DevOps team needs to perform 
# a system update on 212 servers. However, 
# they can only update 8 servers per day due to 
# resource restrictions.
# They want to find out how many full 
# days it will take to complete the updates
# and if there will be servers left over on
# the end of final full day.

num_servers = 212
servers_per_day = 8

print('It will take',num_servers//servers_per_day,'full days to update system')
print(num_servers%servers_per_day,'servers will be left at the end of final full day')























