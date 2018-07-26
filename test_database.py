import pytest
import pyodbc

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

def test_delivered_product_table_row_count(cursor):
    cursor.execute('select name from saleslt.product')
    rs = cursor.fetchall()
    assert len(rs) == 295

def test_delivered_customer_table_row_count(cursor):
    cursor.execute('select firstname from saleslt.customer')
    rs = cursor.fetchall()
    assert len(rs) == 847 

def test_update_customers(cursor):
    lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
    print(lastname)
    assert lastname == 'McGee'
    cursor.execute("update saleslt.customer set lastname = 'Gibbs' where customerid = 1")
    lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
    print(lastname)
    assert lastname == 'Gibbs'


def test_update_customers_again(cursor):
    lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
    print(lastname)
    assert lastname == 'McGee'
    cursor.execute("update saleslt.customer set lastname = 'Gibbs' where customerid = 1")
    lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
    print(lastname)
    assert lastname == 'Gibbs'
