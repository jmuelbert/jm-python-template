import pytest
from jm_python_template.buildprocess import core


class TestBuildProcess:
    def test_add(self):
        assert core.add(2, 3) == 5

    def test_divide_normal(self):
        assert core.divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            core.divide(10, 0)

    def test_build_pipeline_empty(self):
        assert core.build_pipeline([]) == "No steps to run."

    def test_build_pipeline_steps(self):
        result = core.build_pipeline(["compile", "test", "package"])
        assert "Executed compile" in result
        assert result.endswith("Executed package")

    @pytest.mark.parametrize(
        "flag,expected", [(True, "Process executed."), (False, "Process skipped.")]
    )
    def test_conditional_process(self, flag, expected):
        assert core.conditional_process(flag) == expected
