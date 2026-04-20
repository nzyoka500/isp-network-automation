# ============================================
# OLT SYSTEM SETUP
# File: olt_system_setup.py
# Purpose: Safe initial configuration of Huawei OLT (EA5801E)
# Features: logging, dry-run mode, confirmation steps, structured flow
# Author: Eric Nzyoka
# Date: 2026-04-20
# ============================================

from netmiko import ConnectHandler
import logging

# -------- LOGGING SETUP --------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# -------- MODE CONTROL --------
DRY_RUN = True   # Set False for real deployment

# -------- DEVICE DETAILS --------
device = {
    "device_type": "huawei",
    "host": "192.168.1.1",
    "username": "root",
    "password": "admin123",
}

# -------- BASE CONFIG --------
base_config = [
    # System identity
    "sysname DCC-OLT-EA5801E",

    # Time configuration
    "timezone GMT+03:00",

    # Logging & alarms
    "alarm output all",
    "event output all",

    # VLAN setup
    "vlan 2024 to 2027 smart",
    "vlan name 2024 OLT_MGMT",
    "vlan name 2025 GOK_OFFICE",
    "vlan name 2026 SCHOOL_NET",
    "vlan name 2027 PUBLIC_WIFI",
]


# -------- CONFIRM ACTION --------
def confirm_action(message):
    response = input(f"\n{message} (yes/no): ").strip().lower()
    return response == "yes"


# -------- CONNECT TO DEVICE --------
def connect_device():
    logger.info("Connecting to OLT device...")
    return ConnectHandler(**device)


# -------- APPLY CONFIGURATION --------
def apply_config(conn):
    logger.info("Applying base configuration...")

    for cmd in base_config:
        logger.info(f"Sending: {cmd}")

        if not DRY_RUN:
            conn.send_config_set([cmd])
        else:
            logger.info("[DRY-RUN] Command skipped")


# -------- SAVE CONFIGURATION --------
def save_config(conn):
    logger.info("Saving configuration...")

    if not DRY_RUN:
        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")
    else:
        logger.info("[DRY-RUN] Save skipped")


# -------- MAIN FUNCTION --------
def run_config():
    logger.info("OLT System Setup Script Started")
    logger.info(f"DRY_RUN MODE = {DRY_RUN}")

    if not confirm_action("Proceed with OLT system configuration?"):
        logger.warning("Operation cancelled by user.")
        return

    try:
        conn = connect_device()

        apply_config(conn)
        save_config(conn)

        logger.info("Base configuration applied successfully.")
        conn.disconnect()

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")


# -------- ENTRY POINT --------
if __name__ == "__main__":
    run_config()