import cv2.os
import numpy as np
from PIL import Image
import pickle
import sqlite3

recognizer=cv2.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
