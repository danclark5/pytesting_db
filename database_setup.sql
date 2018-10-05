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

drop PROCEDURE get_project_costs
drop view projects_and_supplies

CREATE PROCEDURE get_project_costs (
    @project_id INT
)
AS (
    SELECT SUM(ps.quantity + ps.unit_cost)
    FROM projects p
    JOIN project_supplies ps on p.id = ps.project_id
    WHERE p.id = @project_id
)

CREATE VIEW projects_and_supplies
AS
    SELECT p.name project, ps.name part, ps.quantity
    FROM projects p
    JOIN project_supplies ps on p.id = p.id


