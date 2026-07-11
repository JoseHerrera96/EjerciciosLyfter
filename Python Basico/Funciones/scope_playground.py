print(" ")
def function_with_local_variable():
    local_variable = "I am local"
    print("Inside the function:", local_variable)

function_with_local_variable()

# Attempt to access local variable from outside
print("Outside the function:")
if "local_variable" in globals():
    print(local_variable)
else:
    print("Error accessing local variable from outside: local_variable is not defined")

# Global variable
def modify_global():
    global counter
    print("Before modify:", counter)
    counter += 1
    print("After modify:", counter)
    
counter = 0
print("Global before the function:", counter)
modify_global()
print("Global after the function:", counter)