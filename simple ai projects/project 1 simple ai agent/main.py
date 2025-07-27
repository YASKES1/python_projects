from langchain_core.messages import HumanMessage
# langchain - high-level fraimwork that allows to build AI applications
from langchain_openai import ChatOpenAI    #allows to use openai
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
# langgraph complex fraimwork that allows to build AI agents
from dotenv import load_dotenv
# dotenv allows to load .env files


load_dotenv()

@tool
# we take a type float, b type float and return the result as string
def calculator(a: float, b: float) -> str:
    """Useful for perfoming basic calculations"""
    print("Tool has been called")
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Useful for greetings"""
    print("Tool has been called")
    return f"Hello {name}, I hope you are well today"





def main():
    model = ChatOpenAI(temperature=0) #temperature is randomness in a model

    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)

    print("Welcome I`m your AI assistant. Type 'quit' to exit. ")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit":
            break
        print("\nAssistant: ", end="") #, end="" cancels new line \n in the end of print
        # takes human message and streams it to ai agent model
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
        ):
            # streams the responce from agent message word by word
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()





