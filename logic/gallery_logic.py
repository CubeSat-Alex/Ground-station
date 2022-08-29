import os
import enum
import datetime
from logic.data import Data

imageFolder = "output\\images"
videosFolder = "output\\videos"


def getAllNames(path):
    path2 = os.getcwd() + "\\" + path
    isExist = os.path.exists(path2)
    names = []
    if isExist:
        files_in_dir = os.listdir(path2)
        for file in files_in_dir:
            names.append(GalleryFile(file, path2))
    return names


def sortGallery(files, sortType):
    if sortType == SortType.date:
        print("sor by date")
        return sorted(files, key=lambda x: x.date)
    elif sortType == sortType.mission:
        print("sort by mission")
        return sorted(files, key=lambda x: x.mission)
    elif sortType == sortType.duration:
        print("sort by duration ")
        return sorted(files, key=lambda x: x.duration)


class GalleryFile:
    def __init__(self, name, path):
        self.path = f'{path}/{name}'
        data = name.split('.')
        self.date = datetime.datetime.strptime(data[0], "%d_%m_%Y %H_%M_%S")
        self.mission = data[1]
        self.duration = data[2]
        self.x = data[3]
        self.y = data[4]


class SortType(enum.Enum):
    date = 0
    mission = 1
    duration = 2



