import sys

PRINT_BEEJ      = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4
PRINT_REGISTER  = 5
ADD             = 6
PUSH            = 7 # for stack
POP             = 8 # for stack
CALL            = 9
RET             = 10

'''
SAVE takes 2 arguments
saves value in [ARG1] to register [ARG2]
'''

register = [0] * 8 # self.reg

memory = [0] * 128  # 128 bytes of RAM # self.ram

SP =  7 # self.reg[7] # stack pointer


def load_memory(filename):
    try:
        address = 0

        with open(filename) as f:
            for line in f:
                # print(line)
                
                # now want to parse each line
                # split before and after comment symbol
                comment_split = line.split("#")
    
                # convert pre-comment portion from binary to dec value
                # strip() removes extra white space that may be present
                num = comment_split[0].strip() 
                # Ignore blanks
                if num == "":
                    continue

                value = int(num) # for binary use int(num, 2)

                memory[address] = value

                address += 1

    except FileNotFoundError:
        print(f"{sys.argv[0]}: {sys.argv[1]} not found")
        sys.exit(2)




if len(sys.argv) != 2:
    print("usage: simple.py <filename>", file=sys.stderr)
    sys.exit(1)

filepath = sys.argv[1]
load_memory(filepath)

pc = 0
running = True

while running:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3

    elif command == PUSH:
        # do push
        """ Push the value in the given register on the stack.
        Decrement the SP.
        Copy the value in the given register to the address pointed to by SP."""

        reg = memory[pc + 1] # get the register
        value = register[reg] # get the value at that register
        register[SP] -= 1 # decrement SP
        memory[register[SP]] = value # set mem at SP register to value

        pc += 2


    elif command == POP:
        # do pop
        """ Pop the value at the top of the stack into the given register.
        Copy the value from the address pointed to by SP to the given register.
        Increment SP."""
        reg = memory[pc + 1]
        value = memory[register[SP]]
        register[reg] = value
        register[SP] += 1
        pc += 2

    elif command == CALL:
        # call
        """ Calls a subroutine (function) at the address stored in the register.

        The address of the instruction directly after CALL is pushed onto the stack. This allows us to return to where we left off when the subroutine finishes executing.
        The PC is set to the address stored in the given register. We jump to that location in RAM and execute the first instruction in the subroutine. The PC can move forward or backwards from its current location."""
        
        register[SP] -= 1
        memory[register[SP]] = pc + 2 # the next following instruction after the register

        reg = memory[pc + 1] # register where subroutine is stored
        pc = register[reg] # setting the pc to where that sroutine is in register

    elif command == RET:
        # return
        """" Return from subroutine.
        Pop the value from the top of the stack and store it in the PC."""
        pc = memory[register[SP]] # where is our next command
        register[SP] += 1 # move stack pointer back up
    
    elif command == HALT:
        running = False
        pc += 1

    else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)


