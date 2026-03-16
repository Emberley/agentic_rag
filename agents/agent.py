from .planner import Planner
from .reasoner import Reasoner
from .tools import python_tool, sql_tool, web_search_tool

class Agent:
    def __init__(self, vector_store, memory_manager):
        self.vs = vector_store
        self.memory = memory_manager
        self.reasoner = Reasoner()

    def retrieve_docs(self, query, k=2):
        docs = self.vs.retrieve(query, k=k)
        return "\n".join([d.page_content for d in docs])

    def act(self, query):
        tool = Planner.decide_tool(query)

        if tool == "retrieve":
            context = self.retrieve_docs(query)
            answer = self.reasoner.answer(query, context)
        elif tool == "sql":
            answer = sql_tool(query)
        elif tool == "search":
            answer = web_search_tool(query)
        else:
            answer = "I don't know how to handle that."

        self.memory.add(query, answer)
        return answer
