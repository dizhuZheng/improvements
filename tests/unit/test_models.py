from conftest import new_user, new_role
# This test doesn't access the underlying database; it only checks the interface class used by SQLAlchemy.
"""
GIVEN a Role model
WHEN a new Role is created
THEN check the names are defined correctly
"""
def test_new_user(new_user):
    """
    GIVEN a User model  
    """
    assert new_user.name == 'fake'
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password_hash != 'FlaskIsAwesome'
    
def test_new_role(new_role):
    assert new_role.name == 'VIP'
