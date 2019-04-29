CREATE TABLE clave(
    id INT PRIMARY KEY AUTO_INCREMENT,
    clave VARCHAR(5) NOT NULL,
    materia VARCHAR(100) NOT NULL
);

CREATE TABLE seccion(
    id INT PRIMARY KEY AUTO_INCREMENT,
    seccion VARCHAR(3) NOT NULL
);

CREATE TABLE profesor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE hora(
    id INT PRIMARY KEY AUTO_INCREMENT,
    hora VARCHAR(5) NOT NULL
);

CREATE TABLE dia(
    id INT PRIMARY KEY AUTO_INCREMENT,
    dia VARCHAR(10) NOT NULL,
    identificador CHAR NOT NULL
);

CREATE TABLE edificio(
    id INT PRIMARY KEY AUTO_INCREMENT,
    edificio VARCHAR(50) NOT NULL
);

CREATE TABLE periodo(
    id INT PRIMARY KEY AUTO_INCREMENT,
    periodo VARCHAR(50) NOT NULL

);

CREATE TABLE aula(
    id INT PRIMARY KEY AUTO_INCREMENT,
    aula VARCHAR(10) NOT NULL,
    edificio INT,
    
    FOREIGN KEY(edificio)
    REFERENCES edificio(id)
);


CREATE TABLE horario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    hora_inicial INT,
    hora_final INT,
    periodo INT,
    
    FOREIGN KEY(hora_inicial)
    REFERENCES hora(id),
    
    FOREIGN KEY(hora_final)
    REFERENCES hora(id),
    
    FOREIGN KEY(periodo)
    REFERENCES periodo(id)
);


CREATE TABLE detalle(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nrc INT,
    creditos INT,
    cupos_totales INT,
    cupos_disponibles INT
);



CREATE TABLE oferta(
    nrc INT PRIMARY KEY,
    oferta VARCHAR(100) NOT NULL,
    id_clave  INT,
    id_seccion INT,
    id_detalle INT,
    id_profesor INT,
    
    FOREIGN KEY(id_clave)
    REFERENCES clave(id),
    
    FOREIGN KEY(id_seccion)
    REFERENCES seccion(id),
    
    FOREIGN KEY(id_detalle)
    REFERENCES detalle(id),
    
    FOREIGN KEY(id_profesor)
    REFERENCES profesor(id)
);


CREATE TABLE horarios(
    nrc INT,
    id_horario INT,
    
    FOREIGN KEY(nrc)
    REFERENCES oferta(nrc),
    
    FOREIGN KEY(id_horario)
    REFERENCES horario(id)
);

CREATE TABLE dias(
    nrc INT,
    id_dia INT,
    
    FOREIGN KEY(nrc)
    REFERENCES oferta(nrc),
    
    FOREIGN KEY(id_dia)
    REFERENCES dia(id)
);

CREATE TABLE aulas(
    nrc INT,
    id_aula INT,
    
    FOREIGN KEY(nrc)
    REFERENCES oferta(nrc),
    
    FOREIGN KEY(id_aula)
    REFERENCES aula(id)
);

CREATE TABLE edificios(
    nrc INT,
    id_edificio INT,
    
    FOREIGN KEY(nrc)
    REFERENCES oferta(nrc),
    
    FOREIGN KEY(id_edificio)
    REFERENCES edificio(id)
                      
);

create database materias;

grant all privileges on materias.* to 'miguel'@'localhost';




INSERT INTO dia(dia, identificador) VALUES ('Lunes', 'L');
INSERT INTO dia(dia, identificador) VALUES ('Martes', 'M');
INSERT INTO dia(dia, identificador) VALUES ('Miercoles', 'I');
INSERT INTO dia(dia, identificador) VALUES ('Jueves', 'J');
INSERT INTO dia(dia, identificador) VALUES ('Viernes', 'V');
INSERT INTO dia(dia, identificador) VALUES ('Sabado', 'S');
INSERT INTO dia(dia, identificador) VALUES('Domingo', 'D');
