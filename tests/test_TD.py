# tests/test_td.py
import brickalistest.TD as td

def test_import():
    # Module imports and has the main() entrypoint
    assert hasattr(td, "main") and callable(td.main)

def test_main_runs(monkeypatch):
    # Stub both Tk and Label so no tkinter internals run:
    #  - Tk() returns an object with only mainloop()
    #  - Label(...) returns an object with only pack()
    monkeypatch.setattr(td.tk, "Tk", lambda: type("D", (), {"mainloop": lambda self: None})())
    monkeypatch.setattr(
        td.tk,
        "Label",
        lambda *args, **kwargs: type("L", (), {"pack": lambda self, **k: None})()
    )

    # Should execute without error or hanging
    assert td.main() is None
