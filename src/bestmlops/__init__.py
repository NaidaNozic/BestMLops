import random
import time


def generate_fun_fact() -> str:
    facts = [
        "MLops combines ML and DevOps to streamline model deployment.",
        "Python was released in 1991 — it's older than Google!",
        "Ruff is a super-fast Python linter written in Rust.",
        "Git was created by Linus Torvalds — the same guy behind Linux.",
        "The word 'algorithm' comes from a Persian mathematician: Al-Khwarizmi.",
    ]
    return random.choice(facts)


def main() -> None:
    print("Hello from bestmlops!")
    time.sleep(1)
    print("Here's a fun fact for you:")
    print(f"👉 {generate_fun_fact()}")


if __name__ == "__main__":
    main()
