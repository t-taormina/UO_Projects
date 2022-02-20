"""
CIS 211 Class session 05.11.2021 and Lab 5.12.2021
Tyler Taormina
I FAILED
"""
"""
Introduction to the upcoming project 'Duck CPU' which builds upon the 'Bit-fields' project.

RISC- stands for Reduced instruction set computing (simpler design compared to SISC)

CPU contains [Control logic, instruction decoding, ALU(arithmetic logic unit), registers]

We are going to be writing code for the ALU, the instruction decoding(bit-fields), and 
the majority of time for this project will be in working on the control logic.
    Building the control logic: 
        Fetch, Decode, Execute cycle. This is where the work is. Be very mindful where we are 
        changing the program counter (register 15).  

register 0 always holds a zero and register 15 will be our program counter.  

Register 0 does two things for us. It acts as a trashcan and it also acts as a fresh supply of zeros
Registers are part of the CPU. Memory is a separate component. 

"""