from functions import upload_file
from funtions import download_file

from classes import S3FileManager

manager = S3FileManager()

if __name__ == "__main__":
  manager.upload_file("test.txt", "gloxon")
  manager.download_file("gloxon/test.txt", "test.txt")