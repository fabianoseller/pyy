
CREATE DATABASE telepizza;

CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);


CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    data_hora_pedido DATETIME NOT NULL,
    forma_pagamento VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);


CREATE TABLE Pizzas (
    pizza_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    tamanho VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);


CREATE TABLE Itens_pedido (
    item_pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT NOT NULL,
    pizza_id INT NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
    FOREIGN KEY (pizza_id) REFERENCES Pizzas(pizza_id)
);


CREATE TABLE Ingredientes (
    ingrediente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL
);

CREATE TABLE Pizza_Ingredientes (
    pizza_ingrediente_id INT PRIMARY KEY AUTO_INCREMENT,
    pizza_id INT NOT NULL,
    ingrediente_id INT NOT NULL,
    FOREIGN KEY (pizza_id) REFERENCES Pizzas(pizza_id),
    FOREIGN KEY (ingrediente_id) REFERENCES Ingredientes(ingrediente_id)
);