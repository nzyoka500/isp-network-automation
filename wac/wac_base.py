# ============================================
# WAC BASE CONFIGURATION
# Purpose: VLANs, DHCP, routing, security
# ============================================

from netmiko import ConnectHandler

device = {
    "device_type": "huawei",
    "host": "192.168.2.1",
    "username": "admin",
    "password": "admin123",
}

base_config = [
    # System name
    "sysname DCC-WAC-9700-M1",

    # VLAN setup
    "vlan batch 797 to 800 2024 to 2027",

    # Enable services
    "stp enable",
    "dhcp enable",
    "dns resolve",
    "dns proxy enable",

    # Security
    "management-port isolate enable",
    "management-plane isolate enable",
]

def run_wac_base():
    try:
        conn = ConnectHandler(**device)

        print("[INFO] Configuring WAC base...")
        conn.send_config_set(base_config)

        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")

        print("[SUCCESS] WAC base configured.")
        conn.disconnect()

    except Exception as e:
        print("[ERROR]", str(e))


if __name__ == "__main__":
    run_wac_base()