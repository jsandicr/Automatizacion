import os
from posixpath import basename
import time
from unittest import defaultTestLoader
from common.HTMLReport import HTMLTestRunner
from common.globalparam import report_path, case_path

discover = defaultTestLoader.discover(start_dir=case_path, pattern='ZonasGeograficas.py', top_level_dir=None)
timeStrmap = time.strftime('%d_%m_%Y_%H_%M_%S')
if not os.path.exists(report_path + '/' + str(time.strftime("%Y"))):
    os.makedirs(report_path + '/' + str(time.strftime("%Y")))

if not os.path.exists(report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b"))):
    os.makedirs(report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")))

if not os.path.exists(
        report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")) + '/' + str(time.strftime("%d"))):
    os.makedirs(
        report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")) + '/' + str(time.strftime("%d")))

file_name = report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")) + '/' + str(
    time.strftime("%d")) + '/' + "{}-{}.htmlexecute".format("Reporte de pruebas", str(timeStrmap))
fp = open(file_name, 'wb')
new_path = file_name[0:-13] + ".html"

if __name__ == "__main__":
    runner = HTMLTestRunner(stream=fp, title=u'Reporte de pruebas', description='Detalles')
    runner.run(discover)
    fp.close()
    os.rename(file_name, new_path)