# ============================================
# MASTER DEPLOYMENT SCRIPT
# Purpose: Run all configurations in order
# ============================================

import os

print("===================================")
print(" NETWORK AUTOMATION DEPLOYMENT")
print("===================================\n")

# Run OLT base
print("[STEP 1] OLT Base Config")
os.system("python olt/olt_base.py")

# Run OLT users
print("[STEP 2] OLT Users")
os.system("python olt/olt_service.py")

# Run WAC base
print("[STEP 3] WAC Base Config")
os.system("python wac/wac_base.py")

# Run WAC AP
print("[STEP 4] WAC AP Config")
os.system("python wac/wac_wifi.py")

print("\n[COMPLETE] All systems configured successfully!")