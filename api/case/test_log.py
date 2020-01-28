import pytest
import pytest_assume

@pytest.mark.run(order=3)
def test_log_01():
    print("this is test log 01")
    assert 1==1


@pytest.mark.run(order=1)
def test_log_02():
    print("this is test log 02")
    assert 1 == 2


@pytest.mark.run(order=2)
def test_log_03():
    print("this is test log 03")
    assert 1 == 3


@pytest.mark.run(order=1)
def test_assume_1():
    print("this is test assume 01")
    pytest.assume(1==1)
    pytest.assume(1==2)
    pytest.assume(1==3)

if __name__ == '__main__':
    pytest.main(['-s', 'test_log.py'])

