"""Tests for template_engine module."""

import tempfile
from pathlib import Path

import pytest

from python_project_init.models import ProjectConfig
from python_project_init.template_engine import ProjectGenerator, TemplateEngine


@pytest.fixture
def temp_template_dir():
    """Create a temporary template directory."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        template_dir = Path(tmp_dir)

        # Create a simple template structure
        (template_dir / "README.md.j2").write_text("# {{ project_name }}\n{{ description }}")
        (template_dir / "{{package_name}}.py.j2").write_text("# Package: {{ package_name }}")

        package_dir = template_dir / "package_template"
        package_dir.mkdir()
        (package_dir / "__init__.py.j2").write_text(
            '"""{{ description }}"""\n__version__ = "0.1.0"'
        )

        yield template_dir


@pytest.fixture
def sample_config():
    """Create a sample project configuration."""
    return ProjectConfig(
        project_name="test-project",
        description="A test project",
        author_name="Test Author",
        author_email="test@example.com",
        python_version="3.12",
        package_name="test_project",
        entry_point=True,
        github_username="testuser",
        target_directory=Path("/tmp/test-output"),
    )


def test_template_engine_creation(temp_template_dir):
    """Test TemplateEngine creation."""
    engine = TemplateEngine(temp_template_dir)
    assert engine.template_path == temp_template_dir
    assert engine.env is not None


def test_snake_case_filter(temp_template_dir):
    """Test snake_case filter."""
    engine = TemplateEngine(temp_template_dir)

    assert engine._snake_case("TestProject") == "test_project"
    assert engine._snake_case("test-project") == "test_project"
    assert engine._snake_case("test project") == "test_project"
    assert engine._snake_case("MyAwesomeApp") == "my_awesome_app"


def test_render_template(temp_template_dir, sample_config):
    """Test template rendering."""
    engine = TemplateEngine(temp_template_dir)
    variables = sample_config.to_template_vars()

    content = engine.render_template("README.md.j2", variables)
    expected = "# test-project\nA test project"
    assert content == expected


def test_process_filename(temp_template_dir, sample_config):
    """Test filename processing."""
    engine = TemplateEngine(temp_template_dir)
    variables = sample_config.to_template_vars()

    # Test .j2 extension removal
    result = engine.process_filename("README.md.j2", variables)
    assert result == "README.md"

    # Test variable substitution
    result = engine.process_filename("{{package_name}}.py.j2", variables)
    assert result == "test_project.py"


def test_project_generator_creation(temp_template_dir):
    """Test ProjectGenerator creation."""
    engine = TemplateEngine(temp_template_dir)
    generator = ProjectGenerator(engine)
    assert generator.template_engine == engine


def test_project_generation(temp_template_dir, sample_config):
    """Test full project generation."""
    with tempfile.TemporaryDirectory() as tmp_output:
        config = ProjectConfig(
            project_name="test-project",
            description="A test project",
            author_name="Test Author",
            author_email="test@example.com",
            python_version="3.12",
            package_name="test_project",
            entry_point=True,
            github_username="testuser",
            target_directory=Path(tmp_output) / "test-project",
        )

        engine = TemplateEngine(temp_template_dir)
        generator = ProjectGenerator(engine)
        generator.generate_project(config)

        # Check that files were created
        target_dir = config.target_directory
        assert target_dir.exists()
        assert (target_dir / "README.md").exists()
        assert (target_dir / "test_project.py").exists()
        assert (target_dir / "test_project" / "__init__.py").exists()

        # Check content
        readme_content = (target_dir / "README.md").read_text()
        assert "# test-project" in readme_content
        assert "A test project" in readme_content

        init_content = (target_dir / "test_project" / "__init__.py").read_text()
        assert '"""A test project"""' in init_content
