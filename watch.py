#Extracts a shareable link from youtube embed code
import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(embed):
    matches = re.search(r"src=\"(https?://)(?:www\.)?(youtube)\.com/embed(/\w+)", embed, re.IGNORECASE)
    if matches:
        protocol, domain, id = matches.group(1), matches.group(2), matches.group(3)
        if domain != "youtube":
            return None
        if protocol == "http://":
            protocol = "https://"
        new_domain = domain[:5] + '.' + domain[-2:]
        return(f"{protocol}{new_domain}{id}")
    else:
        return None



if __name__ == "__main__":
    main()
