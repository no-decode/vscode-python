# Function that accepts any number of arguments
def avg(first, *rest):
    return (first+sum(rest))/(1+len(rest))
print(avg(1,2,3,5))
def recv(maxsize, *, block):
 'Receives a message'
 pass
recv(1024, block=False)