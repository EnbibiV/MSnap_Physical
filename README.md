# Physical–Digital Marvel Snap Project

A hybrid board game experience that combines **physical Marvel Snap cards** (embedded with NFC tags) and a **Raspberry Pi 4** running a **Python** application. The goal is to have the Pi handle random effects, track turn order and initiative, calculate power totals at each location, and display a scoreboard on a **7″ touchscreen**.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Hardware Requirements](#hardware-requirements)
4. [Software Requirements](#software-requirements)
5. [Project Plan (Phases)](#project-plan-phases)
   1. [Phase 1: Requirements & Scope Finalization](#phase-1-requirements--scope-finalization)
   2. [Phase 2: Hardware Setup & Assembly](#phase-2-hardware-setup--assembly)
   3. [Phase 3: Raspberry-Pi-OS--Environment-Configuration](#phase-3-raspberry-pi-os--environment-configuration)
   4. [Phase 4: Basic-NFC-Scanning-Prototype](#phase-4-basic-nfc-scanning-prototype)
   5. [Phase 5: Data-Collection--Card-Database](#phase-5-data-collection--card-database)
   6. [Phase 6: Game-Logic--Rules-Implementation](#phase-6-game-logic--rules-implementation)
   7. [Phase 7: User-Interface--Touchscreen-Integration](#phase-7-user-interface--touchscreen-integration)
   8. [Phase 8: Testing--Refinement](#phase-8-testing--refinement)
   9. [Phase 9: Final-Assembly--Presentation](#phase-9-final-assembly--presentation)
   10. [Phase 10: Future-Expansion--Advanced-Features](#phase-10-future-expansion--advanced-features)
6. [Usage](#usage)
7. [Roadmap](#roadmap)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

---

## Introduction

This project aims to bring **Marvel Snap** into a **physical–digital** environment, similar to *Fantasy Realms* or *Marvel Remix*. Physical cards are equipped with **NFC tags**, and a **Raspberry Pi** application handles the random draws, discards, initiative, turn timer, and final power calculations—offloading the complex math from players. 

A **7″ Pi touchscreen** serves as a **scoreboard** and allows players to **manually choose** where they place each card after scanning it with a **single NFC reader**. The final result is a compact, portable system that keeps track of game flow, letting you focus on the fun of playing Marvel Snap in person.

---

## Features

- **Single NFC Reader (PN532):** Tap a card once to identify it.  
- **Touchscreen Scoreboard:** Shows location names, power totals, turn timer, and plays in correct order.  
- **Deck Management:** Players shuffle physical decks, then scan each card in deck order for software to track.  
- **Initiative Logic:** Automatically determines who reveals first each turn (including tie-breaks).  
- **Undo/Back Button:** Fix scanning mistakes easily.  
- **Action Logging:** Saves each game action (scans, random draws/discards) to a file for debugging.

---

## Hardware Requirements

1. **Raspberry Pi 4** (CanaKit or similar, 4 GB+ recommended)  
2. **7″ Raspberry Pi Touchscreen** (official or 3rd-party)  
3. **PN532 NFC Reader** (compatible with Raspberry Pi via SPI or I²C)  
4. **NFC Tags (NTAG213)** – one tag per card (flat enough to fit inside card sleeves)  
5. **Power Supply** (5V, 3A or higher for the Pi)  
6. Optional: A **custom enclosure** that holds the Pi, screen, and NFC reader

---

## Software Requirements

1. **Raspberry Pi OS** (via NOOBS or Raspberry Pi Imager)  
2. **Python 3** + `pip`  
3. **PN532 Libraries for Python** (e.g., `Adafruit_PN532`)  
4. **JSON or SQLite** for card data storage  
5. *Optional:* Python libraries for UI (Tkinter, PyGame, or a web-based approach with Kivy, etc.)

---

## Project Plan (Phases)

Below is the high-level **10-phase** roadmap, from hardware assembly to final testing and future expansions.

### Phase 1: Requirements & Scope Finalization
- **Key Tasks**  
  1. Document final ruleset for in-person Marvel Snap (6 or 7 turns, 3 locations, no snapping).  
  2. Confirm single NFC reader station.  
  3. Confirm minimal location effects (or none initially).  
  4. Finalize UI goals (7″ scoreboard with card play order & a 2-minute turn timer).

- **Deliverables**  
  - Final project scope agreement (this README).  
  - Clear success criteria (accurate scanning, scoreboard UI, correct turn order & initiative).

### Phase 2: Hardware Setup & Assembly
- **Key Tasks**  
  1. Assemble Raspberry Pi 4 in chosen case (e.g., KKSB Aluminum Case).  
  2. Attach and test the 7″ touchscreen (in landscape).  
  3. Connect PN532 breakout board to the Pi (SPI/I²C).  
  4. Acquire & test a few NTAG213 tags in card sleeves.

- **Deliverables**  
  - A physically secure, portable Pi + screen + NFC reader arrangement.  
  - Working hardware test: power on, touchscreen functional, PN532 recognized by Pi.

### Phase 3: Raspberry Pi OS & Environment Configuration
- **Key Tasks**  
  1. Install Raspberry Pi OS and run `sudo apt update && sudo apt upgrade`.  
  2. Enable SPI or I²C via `raspi-config`.  
  3. Install Python and PN532 libraries.  
  4. Calibrate touchscreen, ensure landscape orientation.

- **Deliverables**  
  - Raspberry Pi environment ready for development (Python, PN532 library).  
  - Touchscreen set correctly in landscape mode.

### Phase 4: Basic NFC Scanning Prototype
- **Key Tasks**  
  1. Wire PN532 to Pi’s GPIO (SPI or I²C).  
  2. Run sample Python scripts to read tag UIDs.  
  3. Print or log each scanned card’s UID to confirm scanning reliability.

- **Deliverables**  
  - Proof-of-concept Python script that detects NFC tags and logs UIDs.  
  - Confirm speed & clarity (avoid scanning multiple cards simultaneously).

### Phase 5: Data Collection & Card Database
- **Key Tasks**  
  1. Gather Marvel Snap card data (cost, power, ability).  
  2. Store data in JSON or a lightweight DB (like SQLite).  
  3. Implement monthly script to fetch updated data from fan sites.  
  4. Let players register deck order by scanning each card prior to game start.

- **Deliverables**  
  - Local JSON/DB of official Snap cards.  
  - Basic deck input routine (record deck order after a shuffle).

### Phase 6: Game Logic & Rules Implementation
- **Key Tasks**  
  1. Implement 6-turn structure, plus optional 7th turn logic.  
  2. Manage initiative (compare locations won, total power, ties → random).  
  3. Enforce 4-card max per location.  
  4. Handle random discards or additions (e.g., Korg’s rock, Thor’s Mjolnir).  
  5. Keep track of card order for “On Reveal” priority.

- **Deliverables**  
  - Python module(s) for turn flow, initiative, scoreboard updates, random discards.  
  - Basic error handling if multiple scans happen too quickly.

### Phase 7: User Interface & Touchscreen Integration
- **Key Tasks**  
  1. Design scoreboard in **landscape**: 3 locations (left to right), each location has top (P1) & bottom (P2) rows.  
  2. Show 2-minute turn timer.  
  3. Prompt for location after scanning a card. Grey out full locations.  
  4. Implement “Undo” for mistakes.  
  5. Log actions to a file (e.g., `game_log.txt`).

- **Deliverables**  
  - A functional UI that displays location power totals, card order, timer countdown, and logs all events.  
  - Minimal design enhancements (hexagon shapes, bolded text for big power changes, etc.).

### Phase 8: Testing & Refinement
- **Key Tasks**  
  1. Internal playtests to ensure scanning + location selection works smoothly.  
  2. Fix bugs in initiative or scoring logic.  
  3. Fine-tune the timer or UI layout if players get confused.

- **Deliverables**  
  - Stable, near-final version of the code ready for friend playtesting.  
  - A record of known issues or improvements to address.

### Phase 9: Final Assembly & Presentation
- **Key Tasks**  
  1. Integrate Pi + screen + NFC reader into a polished case.  
  2. Optionally brand or decorate the enclosure or the playing mat.  
  3. Write simple instructions for setup and gameplay.  

- **Deliverables**  
  - A finished, portable device suitable for tabletop play.  
  - Basic user guide (this README plus a quick-start PDF or doc).

### Phase 10: Future Expansion & Advanced Features
- **Key Tasks**  
  1. Add or refine location effects (e.g., Bar with No Name, Limbo, etc.).  
  2. Potentially support multiple screens for private decision phases.  
  3. Incorporate monthly new cards from official Snap updates via fan site data.  

- **Deliverables**  
  - Enhanced rule modules and updates for new abilities.  
  - Multi-display or web-based expansions, if desired.  

---

## Usage

1. **Power On the Pi** with the NFC reader and 7″ touchscreen connected.  
2. **Launch the Python Application** (instructions to come in a future `run.sh` or direct command).  
3. **Register Decks**: Players shuffle their decks, then scan each card in order to store deck order.  
4. **Turn Structure**:  
   - Each turn has a 2-minute timer (1 minute for decision, 1 minute for scanning).  
   - Player scans a card → UI prompts for location choice → location is selected → scoreboard updates.  
5. **End of Game**: After 6 turns (7 if triggered by an effect), the program calculates final location winners and total power for tie-breaks.

---

## Roadmap

- **Short Term**:  
  - Complete stable MVP with scanning, scoreboard, initiative, and basic random discards.  
  - Playtest with full 12-card decks.
- **Long Term**:  
  - Implement location effects.  
  - Automated monthly card data fetch from fan site APIs.  
  - Potential multi-screen or online expansions.

---