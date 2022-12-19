#First Come
def queue(iters: int):
    queuelst = []
    for i in range(iters):
        arrival_time = float(input("arrival "))
        burst_time = float(input("burst "))
        queuelst.append(f'{arrival_time} , {burst_time}')
        i += 1
    return queuelst

x = int(input('p'))
y = queue(x)
print(y)
