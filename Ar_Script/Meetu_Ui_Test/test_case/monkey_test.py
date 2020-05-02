from Ar_Script.Meetu_Ui_Test.common.monkey_runner import monkey_run
from Ar_Script.Meetu_Ui_Test.common.get_info import get_meminfo_data

class Monkey_test:

    def __init__(self):
        self.package='com.meetu.android'
        self.start_meminfo=get_meminfo_data(self.package)
        self.result=[]

    def meminfo_run_test(self):
        monkey_run(self.package)
        tmp_result=get_meminfo_data(self.package)
        self.result.append(tmp_result)
        return self.result