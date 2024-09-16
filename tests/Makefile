SIM ?= icarus
TOPLEVEL_LANG = verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v

# Specify the Python testbench file separately
TESTBENCH = $(PWD)/tests/test.py

# Include the Cocotb Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim
