import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import tasklite


def test_add_and_load(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    tasklite.TASKS_FILE = Path("tasks.json")

    tasklite.add_task("write tests")
    tasks = tasklite.load_tasks()

    assert len(tasks) == 1
    assert tasks[0]["description"] == "write tests"
    assert tasks[0]["done"] is False
