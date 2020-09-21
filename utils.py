import numpy as np
import cv2
import imutils

class TemplateMatcher:
    def __init__(self, template):
        self.template = template
        self.w, self.h = template.shape[::-1]
        self.w_2, self.h_2 = self.w // 2, self.h // 2
    
    def match_image(self, img, method=cv2.TM_CCOEFF_NORMED, threshold=0.65):
        res = cv2.matchTemplate(img, self.template, method) 

        loc = np.where( res >= threshold) 

        if len(loc[0]) < 1:
            return None

        pt = next(zip(*loc[::-1]))

        return ((pt[0], pt[1]), (pt[0] + self.w, pt[1] + self.h))

    def match_image_all(self, img, method=cv2.TM_CCOEFF_NORMED, threshold=0.65):
        res = cv2.matchTemplate(img, self.template, method) 
        
        loc = np.where(res >= threshold) 

        points = []

        for point in zip(*loc[::-1]): 
            points.append((point[0] + self.w // 2, point[1] + self.h // 2))
            
        return points

class Action:
    DOWN = "s"
    UP = "w"
    BACK = "a"

class Bot:
    def __init__(self, template_matcher, action):
        self.template_matcher = template_matcher
        self.action = action

    def match_image(self, img, method=cv2.TM_CCOEFF_NORMED, threshold=0.65):
        return self.template_matcher.match_image(img, method, threshold)