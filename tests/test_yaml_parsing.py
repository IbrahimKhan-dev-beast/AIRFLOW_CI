import pytest
import yaml
from pathlib import Path


@pytest.fixture
def pipelines_dir():
    """Return pipelines directory."""
    return Path(__file__).parent.parent / "pipelines"


@pytest.fixture
def yaml_files(pipelines_dir):
    """Get all YAML files in pipelines/."""
    return list(pipelines_dir.glob("*.yml")) + list(pipelines_dir.glob("*.yaml"))


def test_yaml_syntax_valid(yaml_files):
    """Test all YAML files parse without syntax errors."""
    for yaml_file in yaml_files:
        with open(yaml_file, 'r') as f:
            try:
                yaml.safe_load(f)
            except yaml.YAMLError as e:
                pytest.fail(f"YAML syntax error in {yaml_file}: {e}")


def test_yaml_files_exist(pipelines_dir):
    """Test pipelines/ contains at least one YAML file."""
    yaml_files = list(pipelines_dir.glob("*.yml")) + list(pipelines_dir.glob("*.yaml"))
    assert len(yaml_files) > 0, "No YAML files found in pipelines/"


def test_yaml_structure_valid(yaml_files):
    """Test YAML has expected DAG structure."""
    required_dag_keys = {'default_args', 'schedule_interval', 'tasks', 'dependencies'}

    for yaml_file in yaml_files:
        with open(yaml_file) as f:
            config = yaml.safe_load(f)

        assert isinstance(config, dict), f"{yaml_file} must be a dict at root"

        for dag_id, dag_config in config.items():
            assert isinstance(dag_config, dict), f"DAG '{dag_id}' must be a dict"
            assert 'tasks' in dag_config, f"DAG '{dag_id}' missing 'tasks'"
            assert 'dependencies' in dag_config, f"DAG '{dag_id}' missing 'dependencies'"
