from src.app import App
import src.system_functions as sys_func


if __name__ == '__main__':
    if sys_func.is_first_run(): sys_func.setup_app_first_run()  # Setup app when it's first run
    App(False).MainLoop()