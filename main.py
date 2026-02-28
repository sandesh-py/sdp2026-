
from agents.supervisor import route_query
from agents.communication_agent import draft_email
from rag_query import query_rag

def main():
    query = input("Ask your campus question: ")
    actions = route_query(query)

    if "rag" in actions:
        print("\n--- Policy Answer ---")
        print(query_rag(query))

    if "communication" in actions:
        print("\n--- Drafted Email ---")
        print(draft_email("Sandesh N", "AIML", query))

if __name__ == "__main__":
    main()
