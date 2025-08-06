from dotenv import load_dotenv
from strands import Agent, tool
from strands_tools import calculator, current_time, python_repl

load_dotenv()


# Define a custom tool as a Python function using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


# Create an agent with tools from the strands-tools example tools package
# as well as our custom letter_counter tool
agent = Agent(tools=[calculator, current_time, python_repl, letter_counter])

# Ask the agent a question that uses the available tools
message = """
4つのリクエストがあります：

1. 今の時刻は何時ですか？
2. 3111696 / 74088 を計算してください
3. "strawberry" 🍓という単語に文字「R」はいくつ含まれていますか？
4. 今話したことを実行するスクリプトを出力してください！
   スクリプトが動作することを出力前にPythonツールで確認してください
"""
agent(message)
