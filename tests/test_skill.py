from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent


def test_skill_frontmatter_and_sections() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\n")
    assert "name: destructive-action-guard" in text
    assert "## Trigger Actions" in text
    assert "## Mandatory 3-Step Gate" in text
    assert "gh repo delete" in text


def test_install_script_syntax() -> None:
    res = subprocess.run(["bash", "-n", str(ROOT / "install.sh")], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
