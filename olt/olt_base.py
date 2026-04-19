# ============================================
# OLT BASE CONFIGURATION
# File: olt_base.py
# Purpose: Basic system setup (hostname, VLANs, users, security)
# ============================================

from netmiko import ConnectHandler

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

    # Time settings
    "timezone GMT+03:00",

    # Enable logs/alarms
    "alarm output all",
    "event output all",

    # VLAN creation (basic structure)
    "vlan 2024 to 2027 smart",
    "vlan name 2024 OLT_MGMT",
    "vlan name 2025 GOK_OFFICE",
    "vlan name 2026 SCHOOL_NET",
    "vlan name 2027 PUBLIC_WIFI",
]

# -------- FUNCTION --------
def run_config():
    try:
        print("[INFO] Connecting to OLT...")
        conn = ConnectHandler(**device)

        print("[INFO] Sending base configuration...")
        output = conn.send_config_set(base_config)

        # Save config
        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")

        print("[SUCCESS] Base configuration applied.")
        conn.disconnect()

    except Exception as e:
        print("[ERROR]", str(e))


# -------- EXECUTE --------
if __name__ == "__main__":
    run_config()