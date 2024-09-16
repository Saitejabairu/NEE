# Set the simulator to be used for the simulation
SIM ?= icarus

# Specify the language of the top-level module
TOPLEVEL_LANG = verilog

# Add the Verilog sources
VERILOG_SOURCES += $(PWD)/../hdl/dut.v

# Specify the Python testbench file
TESTBENCH = $(PWD)/tests/test.py

# Include the Cocotb Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim
