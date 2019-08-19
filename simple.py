import sys

PRINT_BEEJ      = 1 # instruction 1
HALT            = 2 # instruction 2
PRINT_NUM       = 3 # instruction 3
SAVE            = 4 # instruction 4
PRINT_REGISTER  = 5 # instruction 5
ADD             = 6 # instruction 6

# 1 and 2 in binary
# 0b00000001 # 1, print beej
# 0b00000001 # 1, print beej
# 0b00000001 # 1, print beej
# 0b00000010 # 2, halt

# so instead of using dec numbers, will set these program names to binary values, then in memory, use the binary values instead of program names to provide instructions

memory = [
    PRINT_BEEJ,
    SAVE, # save 65 to register 2 
    65,
    2, 
    SAVE,
    20,
    3,
    ADD, # add register 2 + register 3 --> R2 += R3
    2,
    3,
    PRINT_REGISTER, # print value in register 2
    2,
    HALT,

    # PRINT_NUM, # prints next value
    # 1,
    # PRINT_BEEJ,
    # PRINT_BEEJ,
    # PRINT_NUM, # prints next value
    # 12,
    # PRINT_BEEJ,
    # HALT,
    # PRINT_NUM, # prints next value
    # 37,
]



"""
SAVE
save [arg1] to register[arg2]
"""

# 8 bytes of mem
# can store 8 items in register
register =  [0] * 8

# we need pointer, pc - program counter
pc = 0 # points to memory
running = True

while running:
    command = memory[pc] # starting at beginning

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc + 1] # next value
        print(num)
        pc += 2 # bc next value in mem is what it to be printed, not read as instructions
    
    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3 # to skip over args

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3
    
    elif command == HALT:
        running = False
        pc += 1

    else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)

    