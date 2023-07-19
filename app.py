import streamlit as st 
import cv2
import AnalyzerModule as pm
import numpy as np
import mediapipe as mp
import tempfile
import os
import time

import matplotlib.pyplot as plt
from ffmpy import FFmpeg

           
joints = [pm.SHOULDER_RIGHT,pm.HIP_RIGHT,pm.KNEE_RIGHT,pm.ANKLE_RIGHT,pm.ELBOW_RIGHT]
limbs = [pm.ARM_LOWER_RIGHT,pm.ARM_UPPER_RIGHT,pm.UPPER_BODY_RIGHT,pm.LEG_UPPER_RIGHT,pm.LEG_LOWER_RIGHT, pm.FOOT_RIGHT]

        
video = st.file_uploader('upload your video')
analyzer = pm.Analyzer()
col1, col2 = st.columns()
if video is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video.read())
    ff = FFmpeg(inputs={tfile.name:None},outputs={'user.MOV':None})
    ff.run()
    st.write('Video Conversion Done')
    st.video(tfile.name)
    path = tfile.name
    analyzer.analyze(tfile.name,joints)
    st.write('Overall Score: ',analyzer.score_motion())
    st.write(analyzer.give_suggestions())
    os.remove('user.MOV')
    col1.pyplot(analyzer.output_graph())
    analyzer.output_video(name = 'user', limbs = limbs, out_frame_rate = 12)
    fr = FFmpeg(inputs={'user.avi':None},outputs={'user.mov':None})
    fr.run()
    st.write('the output video is being processed')
    col2.video('user.mov')
    time.sleep(15)
    os.remove('user.mov')


    
    
    
   
