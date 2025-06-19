#
# testdrive/td.py

import Brickalistest.TD as td

def test_import():
    # smoke-test: module loads and has main()
    assert hasattr(td, "main")

def test_main_runs(monkeypatch):
    # monkey-patch tk.Tk so it never opens a window
    class DummyTk:
        def __init__(self): pass
        def title(self, *args): pass
        def configure(self, *args): pass
        def geometry(self, *args): pass
        def mainloop(self): pass

    monkeypatch.setattr(td.tk, "Tk", DummyTk)
    # should return None and not hang
    assert td.main() is None
