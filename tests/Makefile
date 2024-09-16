# Define the Icarus Verilog executable
IVL = iverilog

# Define the test file
TEST_FILE = test.py

# Define the DUT file
DUT_FILE = dut.v

# Target to compile the Verilog design
compile:
    @echo "Compiling Verilog design..."
    @$(IVL) -o dut.vvp $(DUT_FILE)

# Target to run the simulation
run-sim:
    @echo "Running simulation..."
    @vvp dut.vvp

# Target to run the test
run-test:
    @echo "Running test..."
    @python $(TEST_FILE)

# Target to clean up
clean:
    @echo "Cleaning up..."
    @-rm -rf dut.vvp

# Default target
all: compile run-sim run-test
