# ============================================
# MASTER DEPLOYMENT SCRIPT (INTERACTIVE MENU)
# File: deployment_menu.py
# Purpose: Menu-driven deployment system for OLT and WAC automation
# Features: step-by-step control, confirmations, structured execution
# Author: Eric Nzyoka
# Date: 2026-04-20
# ============================================

import os
import logging

# -------- LOGGING SETUP --------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# -------- CONFIRM FUNCTION --------
def confirm(step_name):
    choice = input(f"\nProceed with {step_name}? (y/n): ").strip().lower()
    return choice == "y"


# -------- RUN COMMAND --------
def run_script(script_path, description):
    if confirm(description):
        logger.info(f"Running: {description}")
        os.system(f"python {script_path}")
    else:
        logger.warning(f"Skipped: {description}")


# -------- MENU DISPLAY --------
def show_menu():
    print("\n===================================")
    print(" NETWORK AUTOMATION DEPLOYMENT MENU")
    print("===================================")
    print("1. OLT System Setup")
    print("2. OLT User Management")
    print("3. WAC Controller Setup")
    print("4. WAC AP Management")
    print("5. Run FULL Deployment")
    print("0. Exit")
    print("===================================")


# -------- MENU HANDLER --------
def handle_choice(choice):
    if choice == "1":
        run_script("olt/olt_system_setup.py", "OLT System Setup")

    elif choice == "2":
        run_script("olt/olt_user_management.py", "OLT User Management")

    elif choice == "3":
        run_script("wac/wac_controller_setup.py", "WAC Controller Setup")

    elif choice == "4":
        run_script("wac/wac_ap_management.py", "WAC AP Management")

    elif choice == "5":
        logger.info("Starting FULL deployment sequence...")

        run_script("olt/olt_system_setup.py", "OLT System Setup")
        run_script("olt/olt_user_management.py", "OLT User Management")
        run_script("wac/wac_controller_setup.py", "WAC Controller Setup")
        run_script("wac/wac_ap_management.py", "WAC AP Management")

        logger.info("FULL deployment completed.")

    elif choice == "0":
        logger.info("Exiting deployment system...")
        exit()

    else:
        logger.error("Invalid option selected.")


# -------- MAIN LOOP --------
def main():
    while True:
        show_menu()
        user_choice = input("Select an option: ").strip()
        handle_choice(user_choice)


# -------- ENTRY POINT --------
if __name__ == "__main__":
    main()