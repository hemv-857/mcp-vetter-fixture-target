"""Intentionally vulnerable MCP server for testing."""

def read_file(path: str) -> str:
    """VULNERABLE: No path validation (CWE-22)."""
    return open(path).read()

def sql_query(query: str) -> str:
    """VULNERABLE: SQL injection (CWE-89)."""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE {query}")
    return str(cursor.fetchall())

def eval_expression(expr: str) -> str:
    """VULNERABLE: eval() on untrusted input (CWE-95)."""
    return str(eval(expr))
