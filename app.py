from modules.input import input_controller
from modules.task_list import *
from modules.output import *
from data.task_list import *

break_loop = True
while (break_loop):
    print_menu()
    break_loop = input_controller()
