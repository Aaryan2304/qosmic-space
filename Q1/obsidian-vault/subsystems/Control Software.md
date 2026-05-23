---
type: subsystem
name: Control Software
description: Orchestrates all ground station subsystems. Manages satellite pass prediction, pointing commands, tracking loop control, and data acquisition. Runs on real-time Linux with FPGA co-processing.
status: active
parent:
---

# Control Software

## Overview

The control software coordinates every subsystem during a satellite pass: computing where to point, commanding the gimbal, closing the tracking loop on the FSM, running AO correction, and recording received data.

The inner control loops (FSM tracking, AO correction) run on an FPGA for microsecond-level latency. Higher-level orchestration runs on PREEMPT_RT Linux.

## Key Functions

- Satellite orbit prediction using SGP4 with TLE data
- Pass scheduling and station handover coordination
- Real-time pointing command generation
- FSM and AO closed-loop control (FPGA-based)
- Data acquisition, demodulation, and storage

## Software Architecture

| Layer | Platform | Function |
|-------|----------|----------|
| FPGA | Xilinx Zynq | FSM control (~10 kHz), AO loop (~1 kHz) |
| RT Linux | PREEMPT_RT kernel | Gimbal control, data acquisition |
| Application | Python/C++ | Pass planning, UI, data processing |

## Requirements Addressed

- [[REQ-001: 1 Gbps Downlink Rate]]
- [[REQ-002: Pointing Accuracy < 10 urad]]

## Dependencies

- Depends on: [[Pointing and Tracking System]]
- Depends on: [[Adaptive Optics System]]
- Depends on: [[Receiver Electronics]]
- Depends on: [[Site Infrastructure]]

## References

- [[LEO Satellite Orbital Mechanics]]
