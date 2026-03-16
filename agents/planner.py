class Planner:
    @staticmethod
    def decide_tool(query: str) -> str:
        query_lower = query.lower()
        if "calculate" in query_lower or "python" in query_lower:
            return "python"
        elif "database" in query_lower or "sql" in query_lower:
            return "sql"
        elif "search" in query_lower:
            return "search"
        else:
            return "retrieve"
