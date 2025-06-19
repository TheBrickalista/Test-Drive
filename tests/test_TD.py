# tests/test_td.py
import brickalistest.TD as td

def test_import():
    # Module imports and has the main() entrypoint
    assert hasattr(td, "main") and callable(td.main)

def test_main_runs(monkeypatch):
    # Stub out tkinter.Tk so this never pops open a real window
    class DummyTk:
        def __init__(self):
            # tkinter.Label does master.tk and master._last_child_ids
            self.tk = self
            self._last_child_ids = {}

        def title(self, *a, **kw): pass
        def configure(self, *a, **kw): pass
        def geometry(self, *a, **kw): pass
        def mainloop(self): pass

    # Monkey-patch td.tk.Tk to our dummy
    monkeypatch.setattr(td.tk, "Tk", DummyTk)

    # Should execute without error or hanging
    assert td.main() is None
