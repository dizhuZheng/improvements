import pytest
from app import create_app
from app.auth.models import User, Role
from app.extensions import bcrypt, csrf

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    csrf.init_app(flask_app)
    flask_app.config.update({
        "TESTING": True
    })
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  


@pytest.fixture(scope='module')
def new_user():
    user = User(name='fake', email='patkennedy79@gmail.com', password_hash=bcrypt.generate_password_hash('FlaskIsAwesome').decode('utf-8'))
    return user


@pytest.fixture(scope='module')
def new_role():
    role = Role(name='VIP')
    return role


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()
