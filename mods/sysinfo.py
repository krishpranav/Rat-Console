class SYSINFO:

    DATA_STRING = ""

    def __init__(self):
        self.sysinfo = self.get_sys_info()
        self.boot_time = self.get_cpu_info()
        self.cpu_info = self.get_cpu_info()
        self.mem_usage = self.get_mem_usage()
        self.disk_info = self.get_disk_info()  
        self.net_info = self.get_net_info()


        def get_size(self, bolter, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bolter < factor:
                    return f"{bolter:.2f}{unit}{suifiX}"

                bolter /= factor 