import openai

# Replace 'YOUR_API_KEY' with your GPT-3 API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

def greet_customer():
    return "Hello! Welcome to our pizza counter. How can I assist you today?"

def take_order(order):
    prompt = f"I'd like to order a {order} pizza with the following toppings: "
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
    )
    return response.choices[0].text

def main():
    print(greet_customer())

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        order = take_order(user_input)
        print("Chatbot:", order)

if __name__ == "__main__":
    main()
