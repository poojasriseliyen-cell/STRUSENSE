# STRUSENSE — Technical Design Note (Planning Draft)

**Team:** TeamAlpha | **Team ID:** HSC|TN|02150 | **State:** Tamil Nadu
**Theme:** AI & GIS (confirm exact portal category)
**Status:** Concept stage; prototype not built.

## 1. Objective
Create a safe, model-scale proof of concept that records vibration/acceleration readings, compares them with a baseline, and flags unusual measurements for human review. It does not certify structural safety or prove the presence of microcracks.

## 2. Proposed architecture

`Motion sensor → ESP32 → serial/Wi-Fi data stream → dashboard → threshold warning → human review`

Optional later modules: a GIS map for sensor/test-site context; Python signal analysis; AI/ML only after collecting labelled and representative data.

## 3. Proposed components
- ESP32 development board.
- Accelerometer/vibration sensor (e.g., MPU6050 if available and suitable).
- Small bridge/track model, stable sensor mounting, breadboard, jumpers and USB power.
- Laptop/phone browser for dashboard.
- Arduino IDE; HTML/CSS/JavaScript dashboard; optional Python analysis.

Confirm exact sensor, voltage, wiring and component availability before implementation.

## 4. Implementation stages
1. Confirm requirements, permissions, sensor datasheet and safe model setup.
2. Read sensor data and verify units/ranges; log stationary baseline.
3. Repeat controlled model vibrations under safe, repeatable conditions.
4. Choose a threshold from collected baseline and test data; document why it was selected.
5. Build dashboard charts and visible warning states.
6. Repeat trials and record false alerts, missed alerts and variation.
7. Consider GIS and AI only as separately evaluated extensions.

## 5. Test plan (not yet performed)
- Test A: stationary model, repeated readings.
- Test B: controlled, repeatable vibration.
- Test C: repeat B across several trials and compare.
- Test D: a safe, controlled change to the model only with faculty guidance.
- Report number of trials, sensor settings, threshold, observed alerts, false positives and false negatives.

## 6. Risks and limitations
Sensor mounting and noise affect measurements; thresholds may trigger on harmless changes; vibration alone cannot reliably prove a crack; a model does not represent a full-scale bridge; AI requires labelled data; GIS mapping provides context but not diagnosis. No deployment on real bridges or active railway infrastructure. Seek faculty and structural/civil expert guidance.

## 7. Acceptance criteria to agree before tests
- Data can be collected and saved with timestamps.
- Readings are repeatable enough for the defined demonstration.
- Alerts behave as documented for the chosen test conditions.
- Results and limitations are reported without overstating detection capability.

## 8. Repository structure (suggested)
- `firmware/` — ESP32 sensor sketch.
- `dashboard/` — browser UI.
- `analysis/` — optional offline analysis script.
- `data/` — clearly labelled simulated sample data until real measurements exist.
- `tests/` — software logic tests.
- `docs/` — architecture, wiring, setup, safety and test results.
- `README.md`, `LICENSE`.
