CREATE Table dim_customer (
    customer_key serial primary key not null,
    customer_id int not null,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(50),
    country varchar(50),
    effective_from date not null,
    effective_to date,
    is_current boolean not null
);

create table dim_product (
    product_id int primary key not null,
    product_name varchar(50),
    price float not null
);

create table dim_date (
    date_id int primary key not null,
    full_date date not null,
    year int,
    month int,
    day int
);

create table fact_orders (
    order_id int primary key,
    customer_id int references dim_customer(customer_id),
    date_id int references dim_date(date_id),
    total_amount float,
    status varchar(50)
);

create table fact_order_items (
    order_item_id int primary key,
    order_id int references fact_orders(order_id),
    product_id int references dim_product(product_id),
    quantity int,
    price float
);

insert into dim_customer (customer_key, customer_id, first_name, last_name, email, country, effective_from, effective_to, is_current)
values (1, 1, 'John', 'Doe', 'john@example.com', 'USA', '2020-01-01', '2021-12-31', true);
insert into dim_customer (customer_key, customer_id, first_name, last_name, email, country, effective_from, effective_to, is_current)
values (2, 2, 'Jane', 'Doe', 'jane@example.com', 'USA', '2020-01-01', '2021-12-31', true);

insert into dim_product (product_id, product_name, price)
values (1, 'Product 1', 100.00);
insert into dim_product (product_id, product_name, price)
values (2, 'Product 2', 200.00);

insert into dim_date (date_id, full_date, year, month, day)
values (1, '2020-01-01', 2020, 1, 1);
insert into dim_date (date_id, full_date, year, month, day)
values (2, '2020-01-02', 2020, 1, 2);

insert into fact_orders (order_id, customer_id, date_id, total_amount, status)
values (1, 1, 1, 100.00, 'pending');
insert into fact_orders (order_id, customer_id, date_id, total_amount, status)
values (2, 1, 2, 200.00, 'pending');

insert into fact_order_items (order_item_id, order_id, product_id, quantity, price)
values (1, 1, 1, 1, 100.00);
insert into fact_order_items (order_item_id, order_id, product_id, quantity, price)     
values (2, 1, 2, 1, 200.00);


insert into dim_customer (customer_key, customer_id, first_name, last_name, email, country, effective_from, effective_to, is_current)
values()