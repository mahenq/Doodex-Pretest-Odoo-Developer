-- CREATE TABLE

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE SalesOrders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT REFERENCES Products(product_id),
    order_date DATE,
    quantity INT
);


--  INSERT DATA

INSERT INTO Products (product_id, product_name, category) VALUES
(1, 'Laptop', 'Gadget'),
(2, 'HP', 'Gadget'),
(3, 'Kaos', 'Pakaian'),
(4, 'Jaket', 'Pakaian');

INSERT INTO SalesOrders (order_id, customer_id, product_id, order_date, quantity) VALUES
(1, 101, 1, '2024-01-10', 300),
(2, 102, 2, '2024-01-15', 200),
(3, 103, 3, '2024-01-20', 200),
(4, 104, 3, '2024-02-05', 300),
(5, 105, 4, '2024-02-10', 150),
(6, 106, 1, '2024-02-15', 200),
(7, 107, 2, '2024-03-01', 250),
(8, 108, 3, '2024-03-10', 100);


-- QUERY 

SELECT 
    TO_CHAR(order_date, 'Mon') AS month,
    p.category,
    SUM(quantity) AS total_units_sold
FROM SalesOrders so
JOIN Products p ON so.product_id = p.product_id
WHERE order_date BETWEEN DATE '2024-01-01' AND DATE '2024-03-31'
GROUP BY 
    EXTRACT(MONTH FROM order_date),
    TO_CHAR(order_date, 'Mon'),
    p.category
ORDER BY 
    EXTRACT(MONTH FROM order_date),
    total_units_sold DESC;