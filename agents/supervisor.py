
def route_query(query):
    query = query.lower()
    actions = []
    if "leave" in query or "policy" in query or "attendance" in query:
        actions.append("rag")
    if "date" in query or "exam" in query:
        actions.append("rag")
    if "draft" in query or "email" in query:
        actions.append("communication")
    return actions
