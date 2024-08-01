#!/usr/bin/python

from mcp23017 import *
from smbus2 import SMBus


i2c = bus = SMBus(1)  # creates a I2C Object as a wrapper for the SMBus
mcp = MCP23017(0x20, i2c)   # creates an MCP object with the given address

mcp.set_all_input()
resultat = mcp.digital_read(GPA0)