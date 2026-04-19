# ============================================
# OLT USER & SECURITY CONFIG
# File: olt_service.py
# Purpose: Create admin users and SSH access
# ============================================

from netmiko import ConnectHandler

device = {
    "device_type": "huawei",
    "host": "192.168.1.1",
    "username": "root",
    "password": "admin123",
}

user_config = [
    # User 1
    "terminal user name nofbiadmin",
    "OGN-T@ifa@2019!@",
    "OGN-T@ifa@2019!@",
    "3",
    "10",

    # User 2
    "terminal user name kplcadmin",
    "Kplcadmin@2025",
    "Kplcadmin@2025",
    "3",
    "10",

    # SSH enable
    "config",
    "ssh user nofbiadmin authentication-type password",
    "ssh user kplcadmin authentication-type password",
]

def apply_users():
    try:
        conn = ConnectHandler(**device)

        print("[INFO] Creating users...")
        conn.send_config_set(user_config)

        conn.send_command("save", expect_string=r"]")
        conn.send_command("Y")

        print("[SUCCESS] Users configured.")
        conn.disconnect()

    except Exception as e:
        print("[ERROR]", str(e))


if __name__ == "__main__":
    apply_users()