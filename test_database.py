from decimal import Decimal

def run_sproc(cursor, project_id):
    stmt = 'exec get_project_costs @project_id=?'
    cursor.execute(stmt, project_id)
    return cursor.fetchval()

def test_project_table_exists(cursor, birch_bookshelf_project):
    cursor.execute('select id from projects')
    rs = cursor.fetchall()
    assert len(rs) == 1 

def test_project_supplies_table_exists(cursor, birch_bookshelf_project):
    cursor.execute('select id from project_supplies')
    rs = cursor.fetchall()
    assert len(rs) == 4 

def test_project_steps_table_exists(cursor):
    cursor.execute('select id from project_steps')
    rs = cursor.fetchall()
    assert len(rs) == 0 

def test_get_project_costs(cursor, birch_bookshelf_project):
    cost = run_sproc(cursor, birch_bookshelf_project)
    assert cost == Decimal('200.42')

def test_projects_and_supplies(cursor, raised_garden_bed_project, birch_bookshelf_project):
    stmt = 'SELECT * from projects_and_supplies'
    rs = cursor.execute(stmt).fetchall()
    assert len(rs) == 8

    

