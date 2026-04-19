# ISP Network Automation Framework (OLT + WAC)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Netmiko](https://img.shields.io/badge/Netmiko-Automation-green)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

## Overview
This project is an ISP-grade network automation framework designed to simplify deployment and configuration of:

- Optical Line Terminals (OLT)
- Wireless Access Controllers (WAC)
- GPON services
- WiFi infrastructure
- VLAN and user provisioning

It reduces manual configuration errors and standardizes ISP rollout procedures using Python automation.

## Key Features

### OLT Automation
- Base system configuration
- VLAN provisioning (Internet, Management, Public WiFi)
- User and SSH setup
- GPON service readiness
- ONT onboarding support

### WAC Automation
- Wireless controller setup
- VLAN segmentation for services
- CAPWAP configuration for APs
- DHCP, DNS, STP setup
- Uplink trunk configuration

## Architecture
```bash
ISP Core Network
│
├── OLT (Fiber Access Layer)
│ └── ONT Devices
│
└── WAC (Wireless Access Layer)
└── Access Points (APs)
```

## Tech Stack
- Python 3
- Netmiko (SSH Automation)
- Huawei OLT/WAC CLI
- VLAN & GPON networking concepts


## Project Modules

| Module | Purpose |
|--------|--------|
| olt_base.py | OLT system initialization |
| olt_users.py | User and SSH configuration |
| wac_base.py | Wireless controller setup |
| wac_ap.py | AP and CAPWAP configuration |

## ▶How to Run

```bash
pip install -r requirements.txt

python main.py
```

## Security Note

- Default credentials should be changed in production
- SSH recommended over Telnet
- VLAN isolation is enforced

## Use Case

- ISP fiber deployment
- Enterprise WiFi rollout
- Smart campus networks
- Managed service providers (MSP)
