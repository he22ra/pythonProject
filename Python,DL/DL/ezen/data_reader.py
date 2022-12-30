# 데이터 처리 클래스
import os
import random
import time

#로그레벨이 3이 되면 warning이 뜨지 않음
os. environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

try:
    from matplotlib import pyplot as plt
except ModuleNotFoundError:
    import pip

    pip.main(['install', 'matplotlib'])
    try:
        from matplotlib import pyplot as plt
        try:

class DataReader():
    def __init__(self):
        print("===데이터 읽기 완료===")
