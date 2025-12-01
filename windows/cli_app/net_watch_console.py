import cmd
import shlex
from datetime import datetime
from windows.sniff_service import start_sniff
from windows.sniff_service import DeviceEvent
import threading

class NetWatch(cmd.Cmd):

    prompt = "NetWatch>"

    def __init__(self):
        super().__init__()
        self.sniff_thread: threading.Thread | None = None

    def do_exit(self, arg):
        """exit"""
        print("bye")
        return True

    def emptyline(self):
        pass

    def show_msg(self, arg:DeviceEvent):
        print(f"[{datetime.now()}]  {arg.ip or "unknown"}  {arg.mac}  {arg.info}  {arg.time}")

    def do_start(self, arg):
        """start watch"""
        def _work():
            print("start watch")
            start_sniff(event_callback=self.show_msg)
        
        if self.sniff_thread and self.sniff_thread.is_alive():
            print("[*]正在抓包中，请勿重复启动，stop停止抓包")
            return 
        self.sniff_thread = threading.Thread(target=_work, daemon=True)
        self.sniff_thread.start()

    def do_stop(self, arg):
        """stop sniff"""
        


if __name__ == "__main__":
    NetWatch().cmdloop()