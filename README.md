# Smart Traffic Light System

**Author:** Vitalis Jerah  
**GitHub:** [DirectorGeneralVJ](https://github.com/DirectorGeneralVJ)  
**Project Type:** BSc Computer Science Portfolio Project  

---

## Table of Contents

- [Overview](#overview)  
- [Problem Statement](#problem-statement)  
- [Solution](#solution)  
- [Features](#features)  
- [Usage](#usage)  
- [Future Improvements](#future-improvements)  
- [Screenshots / Diagrams](#screenshots--diagrams)  

---

## Overview

This project simulates a **Smart Traffic Light System** capable of dynamically adjusting traffic light timings based on real-time traffic conditions and emergency vehicle signals. It logs traffic data for analysis and identifies speed violators. The system is designed as a **Python console application** with modular, object-oriented design.

---

## Problem Statement

Urban areas often face traffic congestion, delayed emergency responses and traffic violations. Traditional traffic lights operate on fixed timers, leading to:

- Long wait times at low-traffic intersections  
- Delays for emergency vehicles such as ambulances or motorcades  
- No automated detection or logging of traffic violations  

This project addresses these issues by providing a **dynamic, intelligent traffic light system**.

---

## Solution

The **Smart Traffic Light System**:

- Detects traffic density (`low`, `medium`, `high`) via simulated sensors  
- Adjusts green light duration dynamically  
- Prioritizes emergency vehicles (ambulances, motorcades) by extending green light time  
- Detects and counts speed violators  
- Logs traffic and emergency data to a CSV file for future analysis  

---

## Features

- **Dynamic Light Timing:** Adjusts green light duration based on traffic conditions  
- **Emergency Vehicle Priority:** Extends green light when ambulances or motorcades approach  
- **Speed Violation Detection:** Simulates detection of speeding vehicles  
- **Data Logging:** Records timestamp, traffic density, green light duration, and emergency alerts to a CSV file  
- **Console Display:** Shows real-time traffic status and emergency alerts  

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/DirectorGeneralVJ/smart-traffic-light-system.git
cd smart-traffic-light-system
## Usage

1. Run the simulation:
```bash
python smart_traffic_light.py
2. Observe the console outputs:

 * Real-time traffic conditions
 * Green light duration adjustments
 * Emergency vehicle alerts
 * Speed violator warnings
 * Check traffic_data.csv for logged data after simulation cycles.

## Future Improvements

 * Integrate real-time sensor APIs for actual traffic data
 * Add GUI dashboard for live traffic monitoring
 * Connect to a web-based mobile app for emergency signals
 * Implement machine learning for predictive traffic light adjustments

Screenshots / Diagrams
<img width="806" height="156" alt="image" src="https://github.com/user-attachments/assets/59921c9c-abad-40ac-a6e4-569675303c83" />
<img width="388" height="257" alt="image" src="https://github.com/user-attachments/assets/4f886115-9255-4867-b623-2491d5909ee7" />


Example console output:
C:\Users\Vitalis\PycharmProjects\pythonProject\.venv\Scripts\python.exe "C:\Users\Vitalis\Desktop\Bsc Computer Science Projects\smart-traffic-light-system\smart_traffic_light.py" 
🚦 Smart Traffic Light System Online
📟 DISPLAY: 🚦 Traffic: Low
🔄 Update | Traffic: low | Green: 7s
⚠️ 3 Speeding Vehicles Detected
📟 DISPLAY: 🚦 Traffic: Low
🔄 Update | Traffic: low | Green: 7s
📟 DISPLAY: 🚦 Traffic: Low
🔄 Update | Traffic: low | Green: 7s
⚠️ 5 Speeding Vehicles Detected
📟 DISPLAY: 🚦 Traffic: High
🔄 Update | Traffic: high | Green: 20s
⚠️ 5 Speeding Vehicles Detected
📟 DISPLAY: 🚦 Traffic: Medium
🔄 Update | Traffic: medium | Green: 12s
⚠️ 4 Speeding Vehicles Detected
