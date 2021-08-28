DROP TABLE IF EXISTS entradas;

CREATE TABLE entradas(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Não poderia ser int?
    titulo STRING NOT NULL,
    texto STRING NOT NULL
);

