# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger= order_numbers(100, 99)
print(smaller, bigger)


"""
print("cat" == "Cat")
print("cat" < "Cat")
print("cat" > "Cat")     # In Python uppercase letters are alphabetically sorted before lowercase letters.That's why, this comparison is  "True"
print("Yellow" >  "Cyan" and "Brown" > "Magenta")     #Because of the same reason as previous line, this line also produce "False"
"""

'''
If a filesystem has a block size of 4096 bytes, 
this means that a file comprised of only one byte
 will still use 4096 bytes of storage. A file made up of 
 4097 bytes will use 4096*2=8192 bytes of storage. 
 Knowing this, can you fill in the gaps in the calculate_storage function below,
  which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks+1)*4096
    return 4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
'''