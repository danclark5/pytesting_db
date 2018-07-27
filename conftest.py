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
def first_project(cursor):
    stmt = textwrap.dedent('''
    INSERT INTO projects(name, description)
    VALUES ('bookshelf', 'Building a bookshelf from birch plywood')
    ''')
    cursor.execute(stmt)
    stmt = 'SELECT @@IDENTITY'
    yield cursor.execute(stmt).fetchval()
