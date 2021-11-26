#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 03:25:49 2021

@author: abhijithneilabraham
"""
from transformers import pipeline
import numpy as np

class Classify:
    def __init__(self,model="valhalla/distilbart-mnli-12-6"):
        self.generator=pipeline("zero-shot-classification",model=model)
    def return_tag(self,textlist,labels):
        labels=labels+",other" # to add "other" to the classes, to avoid bias in prediction
        out={"text":[],"label":[]}
        for text in textlist:
            res=self.generator(text,labels)
            max_index=np.argmax(res["scores"])
            out_label= res["labels"][max_index] if res["scores"][max_index] >0.5 else None
            if out_label and out_label!="other":
                out["text"].append(text)
                out["label"].append(out_label)
        return out
        