from unittest.mock import MagicMock, patch
from app.infrastructure.adapters.input.cli import run


class TestCLI:
    def test_valid_input_prints_result(self, capsys):
        use_case = MagicMock()
        use_case.execute.return_value = 3
        with patch("builtins.input", side_effect=["rabbbit", "rabbit"]):
            run(use_case)
        captured = capsys.readouterr()
        assert "3" in captured.out

    def test_valid_input_calls_use_case(self):
        use_case = MagicMock()
        use_case.execute.return_value = 5
        with patch("builtins.input", side_effect=["babgbag", "bag"]):
            run(use_case)
        use_case.execute.assert_called_once()

    def test_empty_source_prints_invalid_input(self, capsys):
        use_case = MagicMock()
        with patch("builtins.input", side_effect=["", "rabbit"]):
            run(use_case)
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
        use_case.execute.assert_not_called()

    def test_non_english_chars_prints_invalid_input(self, capsys):
        use_case = MagicMock()
        with patch("builtins.input", side_effect=["abc123", "abc"]):
            run(use_case)
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
        use_case.execute.assert_not_called()
