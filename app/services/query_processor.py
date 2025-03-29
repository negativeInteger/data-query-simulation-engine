import re

mock_data = {
    "sales": [
        {"id": 1, "region": "North", "revenue": 5000},
        {"id": 2, "region": "South", "revenue": 3000}
    ],
    "transactions": [
        {"id": 101, "amount": 250, "status": "completed"},
        {"id": 102, "amount": 500, "status": "pending"}
    ]
}

def process_query(natural_query: str):
    """Convert a natural language query into pseudo-SQL and return mock data."""
    natural_query = natural_query.lower()

    # Identify table
    table = None
    for tbl in mock_data.keys():
        if tbl in natural_query:
            table = tbl
            break
    if not table:
        return "INVALID_QUERY", []

    sql_query = f"SELECT * FROM {table}"
    mock_result = mock_data[table]

    # Extract filtering condition (e.g., "where amount is greater than 300")
    filter_match = re.search(r"where (\w+) is (greater than|smaller than|equal to) (\d+)", natural_query)
    if filter_match:
        column, operator, value = filter_match.groups()
        value = int(value)
        operator_map = {"greater than": ">", "smaller than": "<", "equal to": "="}
        sql_operator = operator_map.get(operator, "=")
        sql_query += f" WHERE {column} {sql_operator} {value}"
        mock_result = [row for row in mock_result if eval(f"row.get('{column}', 0) {sql_operator} {value}")]

     # Extract sorting (e.g., "sort sales by region in ascending order")
    sort_match = re.search(r"sort (\w+) by (\w+) in (ascending|descending) order", natural_query)
    if sort_match:
        table_match, column, order = sort_match.groups()
        if table_match == table:  # Ensure sorting is applied to the correct table
            order_desc = order == "descending"
            sql_query += f" ORDER BY {column} {order.upper()}"
            mock_result = sorted(mock_result, key=lambda x: x.get(column, ""), reverse=order_desc)

     # Extract aggregation (e.g., "What is the total revenue by sales?")
    aggregate_match = re.search(r"what is the total (\w+) by (\w+)", natural_query)
    if aggregate_match:
        column, table_match = aggregate_match.groups()
        if table_match == table:  # Ensure the table matches
            total = sum(row.get(column, 0) for row in mock_result)
            sql_query = f"SELECT SUM({column}) FROM {table}"
            return sql_query, [{"total": total}]

    return sql_query + ";", mock_result
def explain_query(natural_query: str):
    """Break down a query into its components."""
    natural_query = natural_query.lower()
    components = {
        "action": "fetch",
        "table": None,
        "filter": None,
        "sort": None,
        "aggregation": None
    }

    # Identify table
    for tbl in mock_data.keys():
        if tbl in natural_query:
            components["table"] = tbl
            break

    if not components["table"]:
        return {"error": "No valid table found in query."}

    # Extract filter (e.g., "where amount is greater than 300")
    filter_match = re.search(r"where (\w+) is (greater than|smaller than|equal to) (\d+)", natural_query)
    if filter_match:
        components["filter"] = f"{filter_match.group(1)} {filter_match.group(2)} {filter_match.group(3)}"

    # Extract sorting (e.g., "sort sales by region in ascending order")
    sort_match = re.search(r"sort (\w+) by (\w+) in (ascending|descending) order", natural_query)
    if sort_match:
        table_match, column, order = sort_match.groups()
        if table_match == components["table"]:  
            components["sort"] = f"ORDER BY {column} {order.upper()}"

    # Extract aggregation (e.g., "What is the total revenue by sales?")
    aggregate_match = re.search(r"what is the total (\w+) by (\w+)", natural_query)
    if aggregate_match:
        column, table_match = aggregate_match.groups()
        if table_match == components["table"]:  
            components["aggregation"] = f"SUM({column})"

    return components

def validate_query(natural_query: str) -> bool:
    """Check if the query references a supported dataset and follows a valid structure."""
    natural_query = natural_query.lower()
    return any(tbl in natural_query for tbl in mock_data.keys())
