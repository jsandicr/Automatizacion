

import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

log_path = os.path.join(project_path, "report", "logs")

img_path = os.path.join(project_path, "report", "img")

report_path = os.path.join(project_path, "report", "report")

case_path = os.path.join(project_path, 'testCase')
