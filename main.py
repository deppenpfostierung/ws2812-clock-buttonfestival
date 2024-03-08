import requests
import urllib.parse
import time

CLOCK_IP = "192.168.84.49"

TEXTS = [
    "YOLO",
    "OIDA",
    "TEST",
    "1337",
]

def set_text(text):
    if len(text) > 4:
        print("Warning: Text is too long, only the first 4 characters will be displayed.")
        text = text[:4]
    url = f"http://{CLOCK_IP}/api/v1/set?overrideDigits={urllib.parse.quote(text)}"
    response = requests.get(url)
    print(response.json())


def main():
    idx = 0
    try:
        while True:
            set_text(TEXTS[idx])
            idx = (idx + 1) % len(TEXTS)

            # wait 10s
            time.sleep(10)
    except KeyboardInterrupt:
        set_text("")
        print("Exiting...")


if __name__ == "__main__":
    main()
