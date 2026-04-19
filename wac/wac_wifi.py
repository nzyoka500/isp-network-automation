# ============================================
# WAC AP CONFIGURATION
# Purpose: CAPWAP, AP control, uplinks
# ============================================

from netmiko import ConnectHandler

device = {
    "device_type": "huawei",
    "host": "192.168.2.1",
    "username": "admin",
    "password": "admin123",
}

ap_config = [
    # CAPWAP source
    "capwap source interface Vlanif2024",

    # Uplink to APs
    "interface GigabitEthernet0/0/1",
    "port link-type trunk",
    "port trunk allow-pass vlan 2024 to 2027",
    "quit",
]

def configure_ap():
    try:
        conn = ConnectHandler(**device)

        print("[INFO] Configuring AP control...")
        conn.send_config_set(ap_config)

        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")

        print("[SUCCESS] AP configuration done.")
        conn.disconnect()

    except Exception as e:
        print("[ERROR]", str(e))


if __name__ == "__main__":
    configure_ap()