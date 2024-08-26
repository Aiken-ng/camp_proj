import cv2, winsound
import mediapipe as mp
import numpy as np
import threading
from winotify import Notification, audio

from timeit import default_timer as timer

reps = 0
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(1)

toast = Notification(app_id="NeuralNine Script", title="Password (Puzzle 1):", msg="deeploveofGod",duration="long")
toast.set_audio(audio.LoopingCall,loop=True)

def notification():
    toast.show()

def L():
    winsound.PlaySound("../l.wav",0)

def O():
    winsound.PlaySound("../o.wav",0)

def V():
    winsound.PlaySound("../v.wav",0)

def E():
    winsound.PlaySound("../e.wav",0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.7,  model_complexity=2) as pose:
    goingdown = False
    currentlet = ""
    wordlist = ""
    start = None
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        # # make detection (needed for draw_landmarks)
        results = pose.process(image)
        # # recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        try:
            landmarks = results.pose_landmarks.landmark
            mp_drawing.draw_landmarks(image, results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
            lw = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
            le = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
            ls = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
            rw = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
            re = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
            rs = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
            rh = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
            rk = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]
            ra = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
            def calangle(a1,b1,c1):
                radians = np.arctan2(c1.y - b1.y,c1.x - b1.x) - np.arctan2(a1.y - b1.y,a1.x - b1.x) 
                angle = np.abs(radians*180/np.pi)
                if angle > 180:
                    angle = 360 - angle
                return angle
            def findL(lw,le,ls,rw,re,rs):
                if (abs(lw.x-ls.x) < 0.05) and (abs(rw.y-rs.y) < 0.05) and (lw.y < le.y < ls.y) and (160 <= calangle(lw,le,ls) <= 180) and (lw.visibility > 0.5 and le.visibility > 0.5 and ls.visibility > 0.5 and rw.visibility > 0.5 and re.visibility > 0.5 and rs.visibility > 0.5 and lw.visibility > 0.5) and (160 <= calangle(rw,re,rs) <= 180):
                    return True
            def findO(lw,le,ls,rw,re,rs):
                if (85 <= calangle(lw,le,ls) <= 135) and (85 <= calangle(rw,re,rs) <= 135) and (lw.visibility > 0.5 and le.visibility > 0.5 and ls.visibility > 0.5 and rw.visibility > 0.5 and re.visibility > 0.5 and rs.visibility > 0.5 and lw.visibility > 0.5) and (ls.x < le.x) and (lw.x < le.x) and (lw.y < le.y < ls.y) and (rs.x > re.x) and (rw.x > re.x) and (rw.y < re.y < rs.y):
                    return True
            def findV(lw,le,ls,rw,re,rs):
                if (lw.y < le.y < ls.y) and (rw.y < re.y < rs.y) and (lw.x > le.x > ls.x) and (160 <= calangle(lw,le,ls) <= 180) and (160 <= calangle(rw,re,rs) <= 180) and (102 <= calangle(ls,rs,re) <= 135) and (101 <= calangle(rs,ls,le) <= 135):
                    return True
            def findE(lw,le,ls,re,rw,rh,rk,ra):
                if (74 <= calangle(lw,le,ls) <= 110) and (abs(re.y-rw.y) < 0.08) and (re.y < rh.y and re.y > rs.y) and (40 <= calangle(rh,rk,ra) <= 110) and (lw.visibility > 0.5 and le.visibility > 0.5 and ls.visibility > 0.5 and rw.visibility > 0.5 and re.visibility > 0.5 and rh.visibility > 0.5 and ra.visibility > 0.5):
                    return True
            if findL(lw,le,ls,rw,re,rs):
                if currentlet != "L":
                    currentlet = "L"
                    wordlist += "L"
                    threading.Thread(target=L).start()
            elif findO(lw,le,ls,rw,re,rs):
                if currentlet != "O":
                    currentlet = "O"
                    wordlist += "O"
                    threading.Thread(target=O).start()
            elif findV(lw,le,ls,rw,re,rs):
                if currentlet != "V":
                    currentlet = "V"
                    wordlist += "V"
                    threading.Thread(target=V).start()
            elif findE(lw,le,ls,re,rw,rh,rk,ra):
                if currentlet != "E":
                    currentlet = "E"
                    wordlist += "E"
                    threading.Thread(target=E).start()
            if wordlist[-4:] == "LOVE":
                threading.Thread(target=notification).start()
                wordlist = ""
        except:
            pass
        img_V = cv2.flip(image, 0)
        cv2.namedWindow("mediapipe Feed", cv2.WINDOW_KEEPRATIO)
        cv2.imshow("mediapipe Feed", image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()