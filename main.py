import json
import pyotp
import argparse
import subprocess


def load_config(path: str):
    with open(file=path, mode="r") as file:
        return json.load(file)


def otp(uri_otp: str):
    code = pyotp.parse_uri(uri=uri_otp)
    print("OTP: {}".format(code_now := code.now()))
    return code_now


def vpn_ipsec(config: dict):
    code_now = otp(config["otp"])
    print("Generate secret...")
    with open("/etc/ipsec.secrets", "w") as file:
        file.write(
            '''%any {} : PSK "{}"\n{} : XAUTH "{}{}"'''.format(
                config["host"], config["psk"], config['user'], config['password'], code_now
            )
        )
    subprocess.run(
        [
            "sudo",
            "ipsec",
            "start",
            "--nofork"
        ])


def vpn_ssl(config: dict):
    code_now = otp(config["otp"])
    subprocess.run(
        [
            "openfortivpn",
            f"{config['host']}:{config['port']}",
            f"--username={config['user']}",
            f"--password={config['password'] + code_now}",
            f"--trusted-cert={config['trusted-cert']}"
        ])


def vpn():
    parser = argparse.ArgumentParser(
        prog='VPN ssl/ipsec1',
        description='Runing ssl/ipsec1 vpn',
    )
    parser.add_argument(
        '--vpn', type=str, choices=["ssl", "ipsec"]
    )
    parser.add_argument(
        "-c", "--config", type=str, default="config.json"
    )
    args = parser.parse_args()
    try:
        for protocol, runnning in {"ssl": vpn_ssl, "ipsec": vpn_ipsec}.items():
            if protocol == args.vpn:
                print(f"Load Config: {args.config}")
                runnning(load_config(args.config)[protocol])
    except Exception as error:
        print(error)
    exit()


if __name__ == "__main__":
    vpn()
