import pytest
import pyodbc
import textwrap

@pytest.fixture(scope='module')
def password():
    with open('pass.word') as f:
        pw = f.readline().strip()
    yield pw

@pytest.fixture(scope='module')
def cnxn(password):
    cnxn = pyodbc.connect('DSN=bruisedthumb;UID=bruised;PWD={}'.format(password))
    yield cnxn
    cnxn.close()

@pytest.fixture
def cursor(cnxn):
    cursor = cnxn.cursor()
    yield cursor
    cnxn.rollback()

@pytest.fixture
def birch_bookshelf_project(cursor):
    stmt = textwrap.dedent('''
    INSERT INTO projects(name, description)
    VALUES ('bookshelf', 'Building a bookshelf from birch plywood')
    ''')
    cursor.execute(stmt)
    stmt = 'SELECT @@IDENTITY'
    project_id = cursor.execute(stmt).fetchval()
    stmt = textwrap.dedent('''
    INSERT INTO project_supplies(project_id, name, quantity, unit_cost)
    VALUES ({project_id}, 'Birch Plywood', 3, 48.50),
           ({project_id}, 'Wood Glue', 1, 5.99),
           ({project_id}, 'Screws', 2, 8.97),
           ({project_id}, 'Stain', 1, 30.99)
    ''')
    cursor.execute(stmt.format(project_id = project_id))
    yield project_id

@pytest.fixture
def raised_garden_bed_project(cursor):
    stmt = textwrap.dedent('''
    INSERT INTO projects(name, description)
    VALUES ('bookshelf', 'Assemble a raised garden bed')
    ''')
    cursor.execute(stmt)
    stmt = 'SELECT @@IDENTITY'
    project_id = cursor.execute(stmt).fetchval()
    stmt = textwrap.dedent('''
    INSERT INTO project_supplies(project_id, name, quantity, unit_cost)
    VALUES ({project_id}, '4x4', 3, 3.75),
           ({project_id}, '2x8', 8, 4.50),
           ({project_id}, '2x4', 8, 2.50),
           ({project_id}, 'Screws', 2, 8.97)
    ''')
    cursor.execute(stmt.format(project_id = project_id))
    yield project_id

