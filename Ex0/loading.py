
import importlib


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:")

    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready"
    }

    for name, purpose in packages.items():
        try:
            module = importlib.import_module(name)
            version = module.__version__
            print(f"[OK] {name} ({version}) - {purpose}")
        except ImportError:
            print(f"[MISSING] {name}")
            print(f"  pip: pip install {name}")
            print(f"  Poetry: poetry add {name}")

    print("\npip vs Poetry:")
    print("  requirements.txt declares what to install; \
          pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, \
          and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")


if __name__ == "__main__":
    main()
