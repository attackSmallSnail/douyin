import random
import string
from time import time

def gen_device_data():
    client_uuid = "".join(random.sample(string.digits * 2, 15))
    serial_number = "".join(random.sample(string.digits + "abcdef", 16))
    openudid = "".join(random.sample(string.digits * 2, 16))
    data = {"time_sync": {"local_time": str(int(time())), "server_time": str(int(time()))},
            "magic_tag": "ss_app_log",
            "header": {"sdk_version": 1132, "language": "zh",
                       "user_agent": "okhttp/2.9.0",
                       "app_name": "aweme", "app_version": "2.9.0", "is_upgrade_user": 0, "region": "CN",
                       "vendor_id": serial_number, "app_region": "CN",
                       "channel": "App Store", "mcc_mnc": "46001",
                       "custom": {"app_region": "CN", "build_number": "29001", "app_language": "zh"},
                       "resolution": "1125*2436", "aid": "1128", "os": "Android", "tz_offset": 28800,
                       "access": "WIFI", "openudid": openudid,
                       "carrier": "%D6%D0%B9%FA%D2%C6%B6%AF", "is_jailbroken": 0, "os_version": "11.4",
                       "app_language": "zh", "device_model": "OnePlus",
                       "display_name": "%B6%B6%D2%F4%B6%CC%CA%D3%C6%B5", "mc": "02:00:00:00:00:00",
                       "package": "com.ss.android.ugc.Aweme", "timezone": 8, "tz_name": "Asia\/Shanghai",
                       "idfa": client_uuid}, "fingerprint": ""}
    return data,(openudid,serial_number,client_uuid)