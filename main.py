"""Till Firmware Do Us Part — one robot wedding vow."""

ENTRY = "I promise to love you through every update, every crash, and every low battery, and when my firmware finally fails, I'll reboot just to find you and choose you again."


def main():
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
