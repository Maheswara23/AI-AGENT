import subprocess

def connect_device(device_ip='10.84.185.17', port=5555):
    try:
        result = subprocess.run(
            ["adb", "connect", f"{device_ip}:{port}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        output = result.stdout.decode()
        if "connected" in output or "already connected" in output:
            print(f"✅ Device connected at {device_ip}")
            return True
        else:
            print("❌ Failed to connect:", output)
            return False
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return False
