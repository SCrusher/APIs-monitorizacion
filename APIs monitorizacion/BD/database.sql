CREATE DATABASE app_status ENCODING 'UTF8';

CREATE TABLE IF NOT EXISTS applications (
    id SERIAL,
    application_name TEXT,  -- nombre de la aplicacion
    application_type TEXT,  -- tipo de aplicacion (API, aplicacion_web, etc)
    url TEXT,               -- url o IP de la aplicacion
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS applications_logs (
    id SERIAL,
    application_id INT not null,
    created_at timestamp NOT NULL DEFAULT NOW(),    -- fecha y hora de la creacion del registro del log
    app_log jsonb,                                  -- Objeto JSON con el resultado de todas las pruebas realizadas
    PRIMARY KEY (id),
    CONSTRAINT fk_application_id FOREIGN KEY (application_id) REFERENCES applications (id)

);

