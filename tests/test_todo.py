from pylenium.driver import Pylenium


def test_check_first_item(py: Pylenium):
    py.visit('https://lambdatest.github.io/sample-todo-app/')
    checkbox = py.getx("//*[text()='First Item']").parent().get('input')
    checkbox.click()
    assert checkbox.should().be_checked()
