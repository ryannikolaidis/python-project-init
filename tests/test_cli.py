"""Tests for CLI module."""

from python_project_init.cli import snake_case, validate_email, validate_project_name


def test_validate_project_name():
    """Test project name validation."""
    # Valid names
    assert validate_project_name("test-project") is True
    assert validate_project_name("test_project") is True
    assert validate_project_name("TestProject") is True
    assert validate_project_name("test123") is True
    assert validate_project_name("a") is True

    # Invalid names
    assert validate_project_name("123test") is False  # starts with number
    assert validate_project_name("-test") is False  # starts with hyphen
    assert validate_project_name("test project") is False  # contains space
    assert validate_project_name("test@project") is False  # contains @
    assert validate_project_name("") is False  # empty


def test_validate_email():
    """Test email validation."""
    # Valid emails
    assert validate_email("test@example.com") is True
    assert validate_email("user+tag@domain.org") is True
    assert validate_email("first.last@sub.domain.co.uk") is True

    # Invalid emails
    assert validate_email("invalid") is False
    assert validate_email("@example.com") is False
    assert validate_email("test@") is False
    assert validate_email("test.example.com") is False
    assert validate_email("") is False


def test_snake_case():
    """Test snake_case conversion."""
    assert snake_case("TestProject") == "test_project"
    assert snake_case("test-project") == "test_project"
    assert snake_case("test project") == "test_project"
    assert snake_case("MyAwesome-App_Name") == "my_awesome_app_name"
    assert snake_case("already_snake") == "already_snake"
    assert snake_case("UPPERCASE") == "uppercase"
