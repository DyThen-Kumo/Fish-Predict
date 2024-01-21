import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import joblib
import pandas as pd

path = r"D:\My Project\Predict Fish"
dictionary = {'Perch': 'Cá rô phi', 'Bream': 'Cá chép', 'Roach': 'Cá bống', 'Pike': 'Cá lóc', 'Smelt': 'Cá trích', 'Parkki': 'Cá hồi', 'Whitefish': 'Cá tuyết'}
fish = "unknown"

def predict(Weight, LengthVer, LengthDia, LengthCro, Height, Width, img, answer):
    model = joblib.load("model.pkl")
    x = pd.DataFrame({
        "Weight":       [Weight],
        "LengthVer":    [LengthVer],
        "LengthDia":    [LengthDia],
        "LengthCro":    [LengthCro],
        "Height":       [Height],
        "Width":        [Width]
    })
    y_pred = model.predict(x)
    fish = y_pred[0]
    
    image = Image.open(path + r"\img\image_" + f"{fish}.png")
    image = image.resize((150,100))
    photo = ImageTk.PhotoImage(image)
    img.config(image=photo)
    img.image = photo

    answer.delete(1.0, END)
    answer.insert(END,"Loài cá bạn đang tìm là:\n          "+ dictionary[fish])