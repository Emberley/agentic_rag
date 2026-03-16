# Python tool
def python_tool(code: str):
    try:
        return str(eval(code))
    except Exception as e:
        return str(e)

# SQL mock
def sql_tool(query: str):
    if "Python" in query:
        return "Found in doc1: Python is a high-level programming language."
    return "No results found."

# Web search mock
def web_search_tool(query: str):
    return f"Mock search result for '{query}'"
