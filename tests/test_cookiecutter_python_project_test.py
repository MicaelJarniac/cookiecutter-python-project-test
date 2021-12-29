from cookiecutter_python_project_test import make_greeting


def test_make_greeting():
    assert (
        make_greeting("Micael Jarniac")
        == "Hello, Micael Jarniac. Welcome to your new project!"
    )
