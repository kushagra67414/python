import time;

# returns a time tuple

print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

for i in range(0,5):
    print(i)
    #Each element will be printed after 1 second
    time.sleep(3)
    