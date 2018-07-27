
def test_project_table_exists(cursor, first_project):
    cursor.execute('select id from projects')
    rs = cursor.fetchall()
    assert len(rs) == 1 

def test_project_supplies_table_exists(cursor):
    cursor.execute('select id from project_supplies')
    rs = cursor.fetchall()
    assert len(rs) == 0 

def test_project_steps_table_exists(cursor):
    cursor.execute('select id from project_steps')
    rs = cursor.fetchall()
    assert len(rs) == 0 

# def test_update_customers(cursor):
#     lastname = cursor.execute('').fetchval()
#     print(lastname)
#     assert lastname == 'McGee'
#     cursor.execute("update saleslt.customer set lastname = 'Gibbs' where customerid = 1")
#     lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
#     print(lastname)
#     assert lastname == 'Gibbs'
# 
# 
# def test_update_customers_again(cursor):
#     lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
#     print(lastname)
#     assert lastname == 'McGee'
#     cursor.execute("update saleslt.customer set lastname = 'Gibbs' where customerid = 1")
#     lastname = cursor.execute('select lastname from saleslt.customer where customerid = 1').fetchval()
#     print(lastname)
#     assert lastname == 'Gibbs'
