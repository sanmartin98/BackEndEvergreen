CREATE TABLE proyectos_analitica (
	id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_proyecto VARCHAR(50) NOT NULL,
    desc_proyecto VARCHAR(100),
    modulo_encargado VARCHAR(25) NOT NULL,
    persona_encargada VARCHAR(25) NOT NULL,
    desc_dataset VARCHAR(100),
    tipo_proyecto VARCHAR(25) NOT NULL,
    estado VARCHAR(25) NOT NULL
)