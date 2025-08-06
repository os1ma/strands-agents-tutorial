from dotenv import load_dotenv
from strands import Agent
from strands.session.file_session_manager import FileSessionManager
from strands_tools import handoff_to_user

load_dotenv()

session_manager = FileSessionManager(session_id="test-session")
agent = Agent(tools=[handoff_to_user], session_manager=session_manager)

agent("人間に名前を聞いてください", breakout_of_loop=True)
