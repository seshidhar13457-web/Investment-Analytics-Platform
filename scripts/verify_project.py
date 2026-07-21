from pathlib import Path
import csv


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():

    print("=" * 70)
    print(" INVESTMENT ANALYTICS PLATFORM")
    print(" PROJECT VERIFICATION")
    print("=" * 70)


    print("\nChecking project folders...")

    folders = [
        "config",
        "producer",
        "data",
        "scripts"
    ]

    for folder in folders:
        path = PROJECT_ROOT / folder

        if path.exists():
            print(f"[OK] {folder}")
        else:
            print(f"[MISSING] {folder}")


    print("\nChecking project files...")

    files = [
        "config/settings.py",
        "producer/trade_generator.py",
        "scripts/verify_project.py"
    ]

    for file in files:
        path = PROJECT_ROOT / file

        if path.exists():
            print(f"[OK] {file}")
        else:
            print(f"[MISSING] {file}")


    print("\nChecking CSV file...")

    csv_file = PROJECT_ROOT / "data" / "trades.csv"


    if csv_file.exists():

        print("[OK] data/trades.csv exists")


        with open(csv_file, encoding="utf-8") as f:

            reader = csv.reader(f)

            header = next(reader)

            rows = sum(1 for _ in reader)


        print(f"[OK] Columns found: {len(header)}")
        print(f"[OK] Trade records: {rows}")


    else:

        print("[MISSING] data/trades.csv")


    print("\n" + "=" * 70)
    print("PROJECT VERIFICATION COMPLETE")
    print("=" * 70)



if __name__ == "__main__":
    main()