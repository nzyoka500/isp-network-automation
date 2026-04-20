# ============================================
# WAC AP CONFIGURATION MODULE
# File: wac_ap_management.py
# Purpose: AP onboarding, CAPWAP setup, trunk configuration
# Mode: Supports STEP-BY-STEP execution (ISP controlled deployment)
# Author: Eric Nzyoka
# Date: 2026-04-20
# ============================================

from netmiko import ConnectHandler
import logging

# -------- LOGGING CONFIG --------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -------- DEVICE DETAILS --------
DEVICE = {
    "device_type": "huawei",
    "host": "192.168.2.1",
    "username": "admin",
    "password": "admin123",
}

# -------- STEP MODE CONTROL --------
STEP_MODE = True  # Supervisor requirement: step-by-step confirmation

# -------- AP CONFIGURATION COMMANDS --------
AP_CONFIG = [
    # CAPWAP configuration (AP control tunnel)
    "capwap source interface Vlanif2024",

    # Uplink configuration (trunk to carry multiple VLANs)
    "interface GigabitEthernet0/0/1",
    "port link-type trunk",
    "port trunk allow-pass vlan 2024 to 2027",
    "quit"
]


# -------- CORE FUNCTION --------
def configure_ap():
    try:
        logging.info("Starting WAC AP configuration module")

        # ---- STEP CONFIRMATION (SUPERVISOR REQUIREMENT) ----
        input("\n[STEP] Confirm AP configuration execution (Press ENTER to continue)")

        logging.info("Connecting to WAC device...")
        conn = ConnectHandler(**DEVICE)

        logging.info("Device connected successfully")

        # ---- APPLY CONFIG STEP BY STEP ----
        for cmd in AP_CONFIG:
            print(f"[APPLY] {cmd}")

            if STEP_MODE:
                input("Press ENTER to apply this command...")

            conn.send_config_set([cmd])

        # ---- SAVE CONFIG ----
        input("\nSave configuration? (Press ENTER to continue)")
        logging.info("Saving configuration to device...")

        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")

        logging.info("AP configuration completed successfully")
        conn.disconnect()

    except Exception as e:
        logging.error(f"AP configuration failed: {e}")


# -------- ENTRY POINT --------
if __name__ == "__main__":
    configure_ap()