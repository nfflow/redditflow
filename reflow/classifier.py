#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 03:25:49 2021

@author: abhijithneilabraham
"""
from sentence_transformers import SentenceTransformer, util

class Classify:
    def __init__(self,model="paraphrase-multilingual-MiniLM-L12-v2"):
        self.model = SentenceTransformer(model)
        
    def return_tag(self,textlist,labels,threshold_cosine_score=0.5):
        text_embeds = self.model.encode(textlist, convert_to_tensor=True)
        label_embeds = self.model.encode(labels, convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(label_embeds, text_embeds)
        text=[]
        classes=[]
        for index in range(len(cosine_scores)):
            for i in range(len(textlist)):
                if cosine_scores[index][i]>threshold_cosine_score:
                    text.append(textlist[i])
                    classes.append(labels[index])
        return {"text":text,"label":classes}
    