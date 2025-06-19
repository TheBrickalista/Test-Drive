# tests/test_td.py
import brickalistest.TD as td

def test_import():
    # Module imports and has the main() entrypoint
    assert hasattr(td, "main") and callable(td.main)

def test_main_runs(monkeypatch):
    # Stub out tkinter.Tk so this never pops open a real window
    class DummyTk:
        def __init__(self):
            # make tkinter.Label happy:
            #  - it reads master.tk
            #  - it tracks child counts in master._last_child_ids
            #  - and it uses master._w as the widget’s Tcl name
            self.tk = self
            self._last_child_ids = {}
            self._w = "."    # root widget name


        def title(self, *a, **kw): pass
        def configure(self, *a, **kw): pass
        def geometry(self, *a, **kw): pass
        def mainloop(self): pass

    # Monkey-patch td.tk.Tk to our dummy
    monkeypatch.setattr(td.tk, "Tk", DummyTk)

    # Should execute without error or hanging
    assert td.main() is None
