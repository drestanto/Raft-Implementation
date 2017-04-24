import psutil
print(psutil.cpu_percent())
print("Available Memory = "+ str(psutil.virtual_memory().available))

