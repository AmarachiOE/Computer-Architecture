"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # DO NOT ADD COMMAS
        self.PC = 0  
        self.IR = None
        self.FL = 0
        self.MAR = None
        self.MDR = None
        self.reg = [0] * 8
        self.reg[7] = 0xF4
        self.ram = [0] * 256
        self.ram[0] = 0x00

        # self.reg[5] = IM
        # self.reg[6] = IS

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            # self.fl,
            # self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, address):
        """ram_read() should accept the address to read and return the value stored there."""
        self.MAR = address
        value = self.ram[self.MAR]

        return value

    def ram_write(self, value, address):
        """ raw_write() should accept a value to write, and the address to write it to."""
        self.MDR = value
        self.MAR = address

        self.ram[self.MAR] = self.MDR

    def run(self):
        """Run the CPU."""

        operand_a = self.ram_read(self.PC + 1)
        operand_b = self.ram_read(self.PC + 2)

        # From LS8 Cheatsheet:
        # ALU ops
        ADD = 0b10100000
        SUB = 0b10100001
        MUL = 0b10100010
        DIV = 0b10100011
        MOD = 0b10100100
        INC = 0b01100101
        DEC = 0b01100110
        CMP = 0b10100111
        AND = 0b10101000
        NOT = 0b01101001
        OR = 0b10101010
        XOR = 0b10101011
        SHL = 0b10101100
        SHR = 0b10101101

        # PC mutators
        CALL = 0b01010000
        RET = 0b00010001
        INT = 0b01010010
        IRET = 0b00010011
        JMP = 0b01010100
        JEQ = 0b01010101
        JNE = 0b01010110
        JGT = 0b01010111
        JLT = 0b01011000
        JLE = 0b01011001
        JGE = 0b01011010

        # Other
        NOP = 0b00000000
        HLT = 0b00000001
        LDI = 0b10000010
        LD = 0b10000011
        ST = 0b10000100
        PUSH = 0b01000101
        POP = 0b01000110
        PRN = 0b01000111
        PRA = 0b01001000

        running = True

        while running:
            pc = self.PC

            # read the memory address stored in register PC, and store in IR
            self.IR = self.ram[pc]

            # starting at beginning
            command = self.ram[pc]

            if command == LDI:
                print("LDI")
                self.reg[operand_a] = operand_b
                self.PC += 3

            elif command == PRN:
                print("PRN")
                print(self.reg[operand_a])
                self.PC += 2

            elif command == HLT:
                print("HLT")
                running = False
                self.PC += 1

            else:
                print(f"Unknown instruction: {command}")
                sys.exit(1)
