##Criar o banco de dados
CREATE DATABASE pizzasnachtech;

##Conectar ao banco de dados
USE telepizza;

##Criar a tabela Clientes
CREATE TABLE Clientes (
  cliente_id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  telefone VARCHAR(20) NOT NULL
);

##Criar a tabela Pedidos
CREATE TABLE Pedidos (
  pedido_id INT PRIMARY KEY AUTO_INCREMENT,
  cliente_id INT NOT NULL,
  data_hora_pedido DATETIME NOT NULL,
  forma_pagamento VARCHAR(255) NOT NULL,
  status VARCHAR(255) NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);

##Criar a tabela Pizzas
CREATE TABLE Pizzas (
  pizza_id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  tamanho VARCHAR(255) NOT NULL,
  preco DECIMAL(10,2) NOT NULL
);

##Criar a tabela Itens_pedido
CREATE TABLE Itens_pedido (
  item_pedido_id INT PRIMARY KEY AUTO_INCREMENT,
  pedido_id INT NOT NULL,
  pizza_id INT NOT NULL,
  quantidade INT NOT NULL,
  FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
  FOREIGN KEY (pizza_id) REFERENCES Pizzas(pizza_id)
);

##Criar a tabela Ingredientes
CREATE TABLE Ingredientes (
  ingrediente_id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  tipo VARCHAR(255) NOT NULL
);

##Criar a tabela Pizza_Ingredientes
CREATE TABLE Pizza_Ingredientes (
  pizza_ingrediente_id INT PRIMARY KEY AUTO_INCREMENT,
  pizza_id INT NOT NULL,
  ingrediente_id INT NOT NULL,
  FOREIGN KEY (pizza_id) REFERENCES Pizzas(pizza_id),
  FOREIGN KEY (ingrediente_id) REFERENCES Ingredientes(ingrediente_id)
);
#

# CRIAÇÃO TABELA Pedidos

CREATE TABLE Pedido (
  pedido_id INT PRIMARY KEY AUTO_INCREMENT,
  dtPedido DATE NOT NULL,
  tamPizza VARCHAR(255) NOT NULL,
  vlTotal DECIMAL(10,2) NOT NULL
);