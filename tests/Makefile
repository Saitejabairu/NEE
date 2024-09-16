SIM ?= icarus
TOPLEVEL_LANG = verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/tests/test.py

or:
	$(MAKE) sim MODULE=test TOPLEVEL=test
include $(shell cocotb-config --makefiles)/Makefile.sim
