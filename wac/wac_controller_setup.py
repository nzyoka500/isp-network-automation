# ============================================
# WAC CONTROLLER SETUP
# File: wac_controller_setup.py
# Purpose: Safe initial configuration of Huawei WAC 9700-M1
# Features: logging, dry-run mode, step confirmation, structured execution
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
DRY_RUN = True   # Set False to apply real changes

# -------- DEVICE DETAILS --------
device = {
    "device_type": "huawei",
    "host": "192.168.2.1",
    "username": "admin",
    "password": "admin123",
}

# -------- BASE CONFIG --------
base_config = [
    "sysname DCC-WAC-9700-M1",

    # VLAN setup
    "vlan batch 797 to 800 2024 to 2027",

    # Core services
    "stp enable",
    "dhcp enable",
    "dns resolve",
    "dns proxy enable",

    # Security controls (ISP-grade isolation)
    "management-port isolate enable",
    "management-plane isolate enable",
]


# -------- CONFIRMATION STEP --------
def confirm_action(message):
    response = input(f"\n{message} (yes/no): ").strip().lower()
    return response == "yes"


# -------- DEVICE CONNECTION --------
def connect_device():
    logger.info("Connecting to WAC device...")
    return ConnectHandler(**device)


# -------- APPLY CONFIGURATION --------
def apply_config(conn):
    logger.info("Applying configuration...")

    for cmd in base_config:
        logger.info(f"Sending: {cmd}")
        if not DRY_RUN:
            conn.send_config_set([cmd])
        else:
            logger.info("[DRY-RUN] Command skipped")


# -------- SAVE CONFIG --------
def save_config(conn):
    logger.info("Saving configuration...")

    if not DRY_RUN:
        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")
    else:
        logger.info("[DRY-RUN] Save skipped")


# -------- MAIN EXECUTION --------
def run_wac_base():
    logger.info("WAC Configuration Script Started")

    logger.info(f"DRY_RUN MODE = {DRY_RUN}")

    if not confirm_action("Do you want to proceed with WAC configuration?"):
        logger.warning("Operation cancelled by user.")
        return

    try:
        conn = connect_device()

        apply_config(conn)
        save_config(conn)

        logger.info("Configuration completed successfully.")
        conn.disconnect()

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")


# -------- ENTRY POINT --------
if __name__ == "__main__":
    run_wac_base()