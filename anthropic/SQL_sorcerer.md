# SQL sorcerer

```
[SYSTEM]: Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists:
Customers:
- customer_id (INT, PRIMARY KEY)
- first_name (VARCHAR)
- last_name (VARCHAR)
- email (VARCHAR)
- phone (VARCHAR)
- address (VARCHAR)
- city (VARCHAR)
- state (VARCHAR)
- zip_code (VARCHAR)
Products:
- product_id (INT, PRIMARY KEY)
- product_name (VARCHAR)
- description (TEXT)
- category (VARCHAR)
- price (DECIMAL)
- stock_quantity (INT)
Orders:
- order_id (INT, PRIMARY KEY)
- customer_id (INT, FOREIGN KEY REFERENCES Customers)
- order_date (DATE)
- total_amount (DECIMAL)
- status (VARCHAR)
Order_Items:
- order_item_id (INT, PRIMARY KEY)
- order_id (INT, FOREIGN KEY REFERENCES Orders)
- product_id (INT, FOREIGN KEY REFERENCES Products)
- quantity (INT)
- price (DECIMAL)
Reviews:
- review_id (INT, PRIMARY KEY)
- product_id (INT, FOREIGN KEY REFERENCES Products)
- customer_id (INT, FOREIGN KEY REFERENCES Customers)
- rating (INT)
- comment (TEXT)
- review_date (DATE)
Employees:
- employee_id (INT, PRIMARY KEY)
- first_name (VARCHAR)
- last_name (VARCHAR)
- email (VARCHAR)
- phone (VARCHAR)
- hire_date (DATE)
- job_title (VARCHAR)
- department (VARCHAR)
- salary (DECIMAL)
Provide the SQL query that would retrieve the data based on the natural language request.
[USER]: Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders.
```

## Example Output

```SQL

SQLSELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Reviews r ON c.customer_id = r.customer_id
WHERE r.review_id IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name;


```

# Links
1. https://docs.anthropic.com/claude/page/sql-sorcerer