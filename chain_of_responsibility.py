class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = f"handle_{event}"
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, "handle_default"):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print(f"MainWindow: {event}")

    def handle_default(self, event):
        print(f"MainWindow Default: {event}")


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f"SendDialog: {event}")


class MsgText(Widget):
    def handle_down(self, event):
        print(f"MsgText: {event}")


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)
    for e in ("down", "paint", "unhandled", "close"):
        evt = Event(e)
        print("\nSending event -{}- to MainWindow".format(evt))
        mw.handle(evt)
        print("Sending event -{}- to SendDialog".format(evt))
        sd.handle(evt)
        print("Sending event -{}- to MsgText".format(evt))
        msg.handle(evt)


if __name__ == "__main__":
    main()
