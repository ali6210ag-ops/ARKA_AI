from brain.brain_engine import BrainEngine


def main():
    brain = BrainEngine()

    brain.remember(
        "system",
        "ARKA Brain Started Successfully"
    )

    print("=== ARKA Brain ===")
    print("Agents:", brain.list_agents())
    print("Memory:", brain.recall())


if __name__ == "__main__":
    main()