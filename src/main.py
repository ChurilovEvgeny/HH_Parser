from src.hh import HH
from src.user_interface import UserInterface
from src.file_workers.JSON_worker import JSONWorker

if __name__ == "__main__":
    UserInterface(HH(), JSONWorker()).run_user_interface()
