#Fixtures
import pytest

#When you use fixtures and scope fuction it will run all time fixtures as well as test functions statments
#
# @pytest.fixture(scope='function')
# def checking_fixtures():
#     print('How function fixtures work')
#
#
# def test_initial_fixture(checking_fixtures):
#     print('this is first fixture testing')
#
#
# def test_second_fixture(checking_fixtures):
#     print('this is second fixtures testing')

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

# @pytest.fixture(scope='module')
# def checking_fixtures():
#     print('How module fixture work')
#
#
# def test_initial_fixture(checking_fixtures):
#     print('this is third fixture testing')
#
#
# def test_second_fixture(checking_fixtures):
#     print('this is forth fixtures testing')

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
#
# #testing conftest file scope=session fixture
#
#
# def test_initial_fixture(checking_session_fixtures):
#     print('this is fifth fixture testing')
#
#
# def test_second_fixture(checking_session_fixtures):
#     print('this is sixth fixtures testing')

#--------------------------------------------------------------------------------------------

#how yeild works once module runs once after that test function runs and once it completes
# it goes back and run below yeild execution steps

# @pytest.fixture(scope='module')
# def checking_fixtures():
#     print('How setup fixture')
#     yield  #yield means pause
#     print('teardown fixture')
#
#
# def test_initial_fixture(checking_fixtures):
#     print('this is seven fixture testing')
#
#
# def test_second_fixture(checking_fixtures):
#     print('this is eight fixtures testing')

# ============================= test session starts =============================
# collecting ... collected 2 items
#
# test_fixtures.py::test_initial_fixture How setup fixture
# PASSED                            [ 50%]this is seven fixture testing
#
# test_fixtures.py::test_second_fixture PASSED                             [100%]this is eight fixtures testing
# teardown fixture
#
#
# ============================== 2 passed in 0.03s ==============================

#returnning some value and we can put assertion to check the condition
@pytest.fixture(scope='module')
def checking_fixtures():
    print('How setup fixture')
    return 'pass'




def test_initial_fixture(checking_fixtures):
    print('this is nineth fixture testing')
    assert checking_fixtures=='pass'


def test_second_fixture(checking_fixtures):
    print('this is tenth fixtures testing')


#pytest commands:
#pytest
#pytest -s
#pytest -k test_case_name
#pytest test_file.py :: test_case_name
#pytest test_file.py :: test_case_name -s
#for skipping write before test_case_name @pytest.mark.skip
#for running specific test_cases then write before test_case @pytest.mark.smoke and run cmd: pytest -m smoke
