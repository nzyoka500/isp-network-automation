# ============================================
# OLT USER MANAGEMENT
# File: olt_user_management.py
# Purpose: Securely create OLT users and enable SSH access
# Features: dry-run mode, logging, step confirmation, structured flow
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
    "host": "192.168.1.1",
    "username": "root",
    "password": "admin123",
}

# -------- USERS CONFIG --------
users = [
    {
        "username": "nofbiadmin",
        "password": "OGN-T@ifa@2019!@",
        "level": "3"
    },
    {
        "username": "kplcadmin",
        "password": "Kplcadmin@2025",
        "level": "3"
    }
]


# -------- CONFIRM ACTION --------
def confirm_action(msg):
    reply = input(f"\n{msg} (yes/no): ").strip().lower()
    return reply == "yes"


# -------- CONNECT TO DEVICE --------
def connect_device():
    logger.info("Connecting to OLT device...")
    return ConnectHandler(**device)


# -------- CREATE USERS --------
def create_users(conn):
    logger.info("Starting user creation process...")

    for user in users:
        logger.info(f"Creating user: {user['username']}")

        cmds = [
            f"terminal user name {user['username']}",
            user["password"],
            user["password"],
            "",              # profile default
            user["level"],   # privilege level
            "10"             # retry attempts
        ]

        for cmd in cmds:
            logger.info(f"Sending command: {cmd}")

            if not DRY_RUN:
                conn.send_command(cmd, expect_string=r"#|Password|Confirm|User|Level|Reenter")
            else:
                logger.info("[DRY-RUN] skipped")

        logger.info(f"[OK] User {user['username']} created")


# -------- ENABLE SSH ACCESS --------
def enable_ssh(conn):
    logger.info("Enabling SSH for users...")

    cmds = [
        f"ssh user {u['username']} authentication-type password"
        for u in users
    ]

    if not DRY_RUN:
        conn.send_config_set(cmds)
    else:
        logger.info("[DRY-RUN] SSH configuration skipped")


# -------- SAVE CONFIG --------
def save_config(conn):
    logger.info("Saving configuration...")

    if not DRY_RUN:
        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")
    else:
        logger.info("[DRY-RUN] Save skipped")


# -------- MAIN FUNCTION --------
def apply_users():
    logger.info("OLT User Management Script Started")
    logger.info(f"DRY_RUN MODE = {DRY_RUN}")

    if not confirm_action("Proceed with OLT user configuration?"):
        logger.warning("Operation cancelled by user.")
        return

    try:
        conn = connect_device()

        create_users(conn)
        enable_ssh(conn)
        save_config(conn)

        logger.info("All operations completed successfully.")
        conn.disconnect()

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")


# -------- ENTRY POINT --------
if __name__ == "__main__":
    apply_users()