import os
import sys
import site


def main() -> None:
    print("LABORATORY STATUS:", end=" ")

    if sys.prefix != sys.base_prefix:
        print("The laboratory is sealed")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You are working in as isolated environment!")
        print("\nReagent installation path:")

        for path in site.getsitepackages():
            print(path)
    else:
        print("You are working in the open")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate")
        print("lab_env\\Scripts\\activate")
        print("\nThen run this program again.")

        print("\nGlobal package locations:")
        for path in site.getsitepackages():
            print(path)


if __name__ == "__main__":
    main()
