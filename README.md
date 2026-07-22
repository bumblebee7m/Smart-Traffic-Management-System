# POLYMORPHISM - Smart Traffic Management System

**Name:** [OWUSU NANA KWARTENG]  
**Index Number:** [FOE.41.006.140.25]  
**Course:** Object Oriented Programming (EL 162 / 234)  

---

## Overview
This repository contains the solution for the **Week 6 OOP Lab Activity** on **Polymorphism in Python** under Dr. Matthew Cobbinah.

The project models a smart city infrastructure where multiple intelligent devices receive a uniform command (`activate()`), but each device exhibits distinct, task-specific behavior through **Run-Time Polymorphism (Method Overriding)**.

---

## Implementation Details
* **Parent Class (`TrafficDevice`)**: Defines the unified interface method `activate()`.
* **Child Classes**:
  * `TrafficLight`: Overrides `activate()` to handle signal phase changes.
  * `SpeedCamera`: Overrides `activate()` to begin tracking speed violations.
  * `PedestrianSignal`: Overrides `activate()` to grant safe crosswalk crossing.
  * `EmergencySiren`: Overrides `activate()` to sound an alert for emergency lanes.
* **Polymorphic Execution**: A single `for` loop iterates through all devices and calls `.activate()` dynamically without type checking.

---

## How to Run

1. Make sure Python is installed.
2. Open your terminal or command prompt in this folder.
3. Run:
   ```bash
   python main.py
