import cmd
import datetime


class Stopwatch:
    def __init__(self):
        super().__init__()
        self._initialise()

    def _initialise(self):
        self._start_time = None
        self.total = datetime.timedelta(0)

    def _get_datetime_now(self):
        return datetime.datetime.now(datetime.timezone.utc)

    def _start(self):
        self._start_time = self._get_datetime_now()
        print("Started...")

    def _stop(self):
        self.total += (self._get_datetime_now() - self._start_time)
        self._start_time = None
        print("Total:", self.total)

    def start_or_stop(self):
        self._stop() if self._start_time else self._start()

    def reset(self):
        self._initialise()
        print("Reset.")


class CommandInterpreter(cmd.Cmd):
    prompt = "(Stopwatch) "

    def preloop(self):
        self.stopwatch = Stopwatch()

    def postloop(self):
        print()

    def do_EOF(self, line):
        return True  # returning any truthy value tells cmdloop to end

    def do_exit(self, line):
        # Ctrl-d for EOF doesn't work on Windows, so we need another way to
        # exit...
        return True

    def emptyline(self):
        self.stopwatch.start_or_stop()

    def do_reset(self, line):
        self.stopwatch.reset()

    def default(self, line):
        return  # don't display error message


def main():
    return CommandInterpreter().cmdloop()


if __name__ == "__main__":
    main()
