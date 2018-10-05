
ALTER PROCEDURE get_project_costs (
    @project_id INT
)
AS (
    SELECT SUM(ps.quantity * ps.unit_cost)
    FROM projects p
    JOIN project_supplies ps on p.id = ps.project_id
    WHERE p.id = @project_id
)

ALTER VIEW projects_and_supplies
AS
    SELECT p.name project, ps.name part, ps.quantity
    FROM projects p
    JOIN project_supplies ps on p.id = ps.project_id


