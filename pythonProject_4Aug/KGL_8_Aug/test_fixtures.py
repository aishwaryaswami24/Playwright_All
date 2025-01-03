#Fixtures
import pytest

#When you use fixtures and scope fuction it will run all time fixtures as well as test functions statments

@pytest.fixture(scope='function')
def checking_fixtures():
    print('How function fixtures work')


def test_initial_fixture(checking_fixtures):
    print('this is first fixture testing')


def test_second_fixture(checking_fixtures):
    print('this is second fixtures testing')

#output when scope=function
# ============================= test session starts =============================
# collecting ... collected 2 items
#
# test_fixtures.py::test_initial_fixture How fixtures work
# PASSED                            [ 50%]this is first fixture testing
#
# test_fixtures.py::test_second_fixture How fixtures work
# PASSED                             [100%]this is second fixtures testing
#
#
# ============================== 2 passed in 0.04s ==============================

@pytest.fixture(scope='module')
def checking_fixtures():
    print('How module fixture work')


def test_initial_fixture(checking_fixtures):
    print('this is third fixture testing')


def test_second_fixture(checking_fixtures):
    print('this is forth fixtures testing')

# ============================= test session starts =============================
# collecting ... collected 2 items
#
# test_fixtures.py::test_initial_fixture How module fixture work
# PASSED                            [ 50%]this is third fixture testing
#
# test_fixtures.py::test_second_fixture PASSED                             [100%]this is forth fixtures testing
#
#
# ============================== 2 passed in 0.02s ==============================