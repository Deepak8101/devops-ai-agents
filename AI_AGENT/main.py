from linux_agent import run_agent


def main():
    user_question = input("Ask your Linux question: ")

    result = run_agent(user_question)

    print("\nAI RESPONSE:")
    print(result)


if __name__ == "__main__":
    main()
