from runtime.runtime import run

if __name__ == "__main__":

    entity = "CHAOS"

    print("Devines Runtime Started")

    while True:

        user_input = input("You: ")

        response = run(entity, user_input)

        print(f"{entity}:", response)
