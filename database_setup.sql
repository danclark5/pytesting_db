CREATE TABLE projects (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    description VARCHAR(2000) NOT NULL
)

CREATE TABLE project_supplies (
    id INT IDENTITY(1,1) PRIMARY KEY,
    project_id INT REFERENCES projects(id),
    name VARCHAR(250) NOT NULL,
    quantity INT NOT NULL,
    unit_cost MONEY NOT NULL
)

CREATE TABLE project_steps (
    id INT IDENTITY(1,1) PRIMARY KEY,
    project_id INT REFERENCES projects(id),
    description VARCHAR(2000) NOT NULL,
    step_number VARCHAR(20) NOT NULL
)


