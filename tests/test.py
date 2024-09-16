import os
import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

@cocotb.test()
async def test_case(dut):
    # Create a clock
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset sequence
    dut.RST_N.value = 1
    await Timer(1, "ns")
    dut.RST_N.value = 0
    await Timer(1, "ns")
    await RisingEdge(dut.CLK)
    dut.RST_N.value = 1

    # Test sequence
    dut.EN_next.value = 0
    dut.EN_start.value = 0
    await Timer(10, "ns")
    await RisingEdge(dut.CLK)
    dut.EN_start.value = 1
    await RisingEdge(dut.CLK)
    dut.EN_start.value = 0
    values = range(5)
    results = []
    for idx, v in enumerate(values):
        dut.EN_next.value = 1
        dut.next_k.value = v
        await RisingEdge(dut.CLK)
        results.append(dut.next.value.integer)
    cocotb.log.info(f"Output is {hex(sum(results))}")
