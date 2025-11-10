CREATE TABLE Product (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

CREATE TABLE Customer (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE "Order" (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

CREATE TABLE OrderItem (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES "Order"(id),
    FOREIGN KEY (product_id) REFERENCES Product(id)
);

-- TEST DATA :
INSERT INTO Product VALUES (1, 'Молок0', 80.0);
INSERT INTO Product VALUES (2, 'Хлеб', 30.0);

INSERT INTO Customer VALUES (1, 'Иван Иванов');
INSERT INTO Customer VALUES (2, 'Петр Петров');

INSERT INTO "Order" VALUES (1, 1, '2025-11-01');
INSERT INTO "Order" VALUES (2, 2, '2025-11-02');

INSERT INTO OrderItem VALUES (1, 1, 1, 2);
INSERT INTO OrderItem VALUES (2, 1, 2, 5);
INSERT INTO OrderItem VALUES (3, 2, 1, 1);