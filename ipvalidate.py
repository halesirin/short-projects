#validates IP address using regular expressions
import re
def main():
    ip = input("IPv4 Address: ").strip()
    if (validate(ip)):
        print("True")
    else:
        print("False")


def validate(ip):
    if re.search(r"^((([0-9])|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])?$", ip, re.IGNORECASE):
        return True
    else:
        return False



if __name__ == "__main__":
    main()

