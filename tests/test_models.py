"""Tests for models module."""

from pathlib import Path

from python_project_init.models import ProjectConfig


def test_project_config_creation():
    """Test ProjectConfig creation."""
    config = ProjectConfig(
        project_name="test-project",
        project_type="python",
        description="A test project",
        author_name="Test Author",
        author_email="test@example.com",
        github_username="testuser",
        target_directory=Path("/tmp/test-project"),
        python_version="3.12",
        package_name="test_project",
        entry_point=True,
        create_api=False,
        extra_context={},
    )

    assert config.project_name == "test-project"
    assert config.project_type == "python"
    assert config.description == "A test project"
    assert config.author_name == "Test Author"
    assert config.author_email == "test@example.com"
    assert config.python_version == "3.12"
    assert config.package_name == "test_project"
    assert config.entry_point is True
    assert config.create_api is False
    assert config.github_username == "testuser"
    assert config.target_directory == Path("/tmp/test-project")
    assert config.extra_context == {}


def test_to_template_vars():
    """Test converting ProjectConfig to template variables."""
    config = ProjectConfig(
        project_name="test-project",
        project_type="python",
        description="A test project",
        author_name="Test Author",
        author_email="test@example.com",
        github_username="testuser",
        target_directory=Path("/tmp/test-project"),
        python_version="3.12",
        package_name="test_project",
        entry_point=False,
        create_api=False,
        extra_context={"script_name": "run.sh"},
    )

    variables = config.to_template_vars()

    assert variables["project_name"] == "test-project"
    assert variables["project_type"] == "python"
    assert variables["description"] == "A test project"
    assert variables["author_name"] == "Test Author"
    assert variables["author_email"] == "test@example.com"
    assert variables["python_version"] == "3.12"
    assert variables["package_name"] == "test_project"
    assert variables["entry_point"] is False
    assert variables["create_api"] is False
    assert variables["github_username"] == "testuser"
    assert variables["script_name"] == "run.sh"
    assert "current_year" in variables
