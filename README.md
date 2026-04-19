# 📡 ISP NETWORK AUTOMATION FRAMEWORK (OLT + WAC)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Netmiko](https://img.shields.io/badge/Netmiko-SSH%20Automation-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Environment](https://img.shields.io/badge/Use-ISP%20Deployment%20Tool-orange)

## Project Overview

This project is a **ISP network automation framework** designed to standardize and automate configuration of core ISP infrastructure.

It is used for deployment and management of:

* Optical Line Terminals (OLT) – Fiber Access Layer
* Wireless Access Controllers (WAC) – WiFi Access Layer
* GPON service provisioning
* VLAN segmentation and management
* Customer onboarding (ONT & AP provisioning)

The system reduces manual CLI configuration, improves deployment speed, and ensures **consistent ISP rollout standards across multiple sites**.


## Network Architecture

```text
                         INTERNET
                             │
                     ┌───────▼────────┐
                     │  ISP CORE CORE  │
                     └───────┬────────┘
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
   ┌──────▼──────┐                     ┌───────▼────────┐
   │     OLT      │                     │      WAC        │
   │ Fiber Access │                     │ WiFi Controller │
   └──────┬──────┘                     └───────┬────────┘
          │ GPON                               │ CAPWAP
   ┌──────▼────────┐                 ┌────────▼────────┐
   │  ONT Devices   │                │     Access Points│
   └──────┬────────┘                 └────────┬────────┘
          │                                  │
   End Users (LAN)                 Wireless Clients (WiFi)
```


## Key Features

### 🔹 OLT Automation (Fiber Layer)

* Device initialization (hostname, timezone, alarms)
* VLAN provisioning (Management, Office, School, Public WiFi)
* Admin user creation and SSH access
* GPON service readiness configuration
* ONT onboarding support (manual provisioning enabled)


### 🔹 WAC Automation (Wireless Layer)

* Wireless controller system configuration
* VLAN segmentation for services
* CAPWAP configuration for AP management
* DHCP, DNS, STP enablement
* Secure uplink trunk configuration
* Centralized AP control and provisioning


## Technology Stack

* Python 3.10+
* Netmiko (SSH automation)
* Paramiko (secure device communication)
* Huawei OLT & WAC CLI
* GPON, VLAN, CAPWAP networking standards

---

## Project Structure

```text
isp-network-automation/
│
├── olt/
│   ├── olt_base.py          # OLT system initialization
│   ├── olt_users.py         # User & SSH configuration
│
├── wac/
│   ├── wac_base.py          # WAC system setup
│   ├── wac_ap.py            # AP & CAPWAP configuration
│
├── configs/
│   ├── olt_config.txt       # Reference OLT configs
│   ├── wac_config.txt       # Reference WAC configs
│
├── diagrams/
│   ├── architecture.png     # Network architecture
│   ├── olt_flow.png         # OLT provisioning flow
│   ├── wac_flow.png         # WAC provisioning flow
│
├── main.py                  # Master deployment controller
├── requirements.txt         # Dependencies
└── README.md
```


## Deployment Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/your-org/isp-network-automation.git
cd isp-network-automation
```


### Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```


### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```


### Step 4: Run Full Deployment

```bash
python main.py
```


## Execution Workflow

When executed, the system performs:

1. OLT Base Configuration
2. OLT User & SSH Setup
3. WAC Base Configuration
4. AP & CAPWAP Deployment
5. VLAN & Service Readiness Validation


## Security & Compliance

* Default credentials must be changed before production use
* SSH preferred over Telnet for secure access
* VLAN segmentation enforced for service isolation
* Management VLAN isolated (VLAN 2024)
* Access control implemented via ACLs and AAA policies


## Business Use Cases

This system is used in ISP environments for:

* Fiber broadband deployment (FTTH)
* Enterprise WiFi provisioning
* Smart campus network rollout
* Managed network service operations (MSP)
* Multi-site ISP infrastructure standardization


## Operational Impact

* ⏱ Reduces deployment time significantly
* ⚙ Eliminates manual CLI configuration errors
* 📡 Standardizes ISP rollout process
* 🔁 Enables repeatable multi-site deployments
* 🧠 Improves operational consistency across engineers


## Project Status

- ✔ Production Deployment Ready
- ✔ Modular Automation Architecture
- ✔ ISP Field Tested Structure
- 🚧 Future: Centralized GUI Dashboard + API Integration
