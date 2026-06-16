from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = (
    "postgresql://postgres:2869"
    "@localhost:5432/aiops_memory_db"
)
checkpointer = PostgresSaver.from_conn_string(
    DB_URI
)
