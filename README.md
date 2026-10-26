# STRUSENSE (starter repository)

TeamAlpha | HSC|TN|02150 | Tamil Nadu

**Status: starter scaffold only. The physical prototype has not been built or tested.** This repository is not evidence of working hardware.

## Goal
Explore model-scale vibration monitoring using an ESP32 and a suitable motion sensor. Threshold alerts indicate unusual readings only; they do not diagnose cracks or certify safety.

## Structure
- `firmware/strusense_esp32.ino`: illustrative ESP32 serial output scaffold; requires sensor-specific library, wiring and validation.
- `dashboard/index.html`: local dashboard demonstration using clearly labelled simulated data.
- `analysis/analyze_csv.py`: basic CSV summary helper.
- `data/sample_simulated.csv`: synthetic sample data, not measured from hardware.
- `tests/test_analysis.py`: small software test.
- `docs/TECHNICAL_DESIGN.md`: implementation and validation plan.

## Setup
1. Review the sensor datasheet and confirm exact hardware and voltage levels.
2. Install Arduino IDE and the appropriate ESP32 board support.
3. Select and install the library for the actual sensor; update the firmware scaffold to match its API.
4. Build on a small model only, with faculty guidance.
5. Run `python analysis/analyze_csv.py data/sample_simulated.csv` to inspect the synthetic example.
6. Open `dashboard/index.html` in a browser; the displayed sample is simulated.

## Before public submission
Replace scaffolds with tested code, add actual wiring/architecture diagrams, log real test cases and results, document dependencies, and verify all files. Do not claim crack detection based on vibration thresholds alone.
