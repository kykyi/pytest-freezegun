import nox


@nox.session(python=["3.6", "3.7", "3.8", "3.9"])
def tests(session):
    # Install dependencies
    session.install(".")
    session.install("-r", "requirements.txt")

    # Determine pytest version based on session name (session.python)
    pytest_version = session.python.replace("3.", "")
    if pytest_version == "5":
        session.install("pytest>=3,<4")
    elif pytest_version == "6":
        session.install("pytest>=4,<5")
    elif pytest_version == "7":
        session.install("pytest>=5,<6")
    elif pytest_version == "8":
        session.install("git+https://github.com/pytest-dev/pytest/")
        session.install("git+https://github.com/spulec/freezegun/")

    # Run tests
    session.run("pytest", "tests/")
