import pickle
import numpy as np
import streamlit as st

fetalhealth_model = pickle.load(open('fetal_healthNew.sav', 'rb'))

st.title('Prediksi Kesehatan Janin')

col1, col2, col3 = st.columns(3)

with col1 :
    baseline_value = st.text_input('input nilai baseline dari sinyal ECG janin')

with col1 :
    accelerations = st.text_input('input nilai Jumlah percepatan jantung janin per detik')

with col1 :
    fetal_movement = st.text_input('input nilai Jumlah gerakan janin yang terdeteksi per detik')

with col1 :
    uterine_contractions = st.text_input('input nilai Jumlah kontraksi uterus per detik')

with col1 :
    light_decelerations	= st.text_input('input nilai Jumlah deceleration ringan dari jantung janin per detik')

with col1 :
    severe_decelerations = st.text_input('input nilai Jumlah deceleration parah dari jantung janin per detik')

with col1 :    
    prolongued_decelerations = st.text_input('input nilai Jumlah deceleration yang berlangsung lama dari jantung janin per detik')

with col2 :
    abnormal_short_term_variability	= st.text_input('input nilai Variabilitas jantung janin dalam jangka pendek yang abnormal')

with col2 :
    mean_value_of_short_term_variability = st.text_input('input nilai rata-rata variabilitas jantung janin dalam jangka pendek')

with col2 :
    percentage_of_time_with_abnormal_long_term_variability = st.text_input('input nilai Persentase waktu dengan variabilitas jantung janin dalam jangka panjang yang abnormal')

with col2 :
    mean_value_of_long_term_variability	= st.text_input('input nilai rata-rata variabilitas jantung janin dalam jangka panjang')

with col2 :
    histogram_width	= st.text_input('input nilai lebar dari histogram yang dibentuk oleh sinyal ECG janin')

with col2 :
    histogram_min = st.text_input('input nilai minimum dari histogram yang dibentuk oleh sinyal ECG janin')

with col2 :
    histogram_max = st.text_input('input nilai maksimum dari histogram yang dibentuk oleh sinyal ECG janin')

with col3 :
    histogram_number_of_peaks = st.text_input('input nilai Jumlah puncak dalam histogram sinyal ECG janin')

with col3 :
    histogram_number_of_zeroes = st.text_input('input nilai Jumlah nol dalam histogram sinyal ECG janin')

with col3 :
    histogram_mode = st.text_input('input nilai Modus dari histogram sinyal ECG janin')

with col3 :
    histogram_mean = st.text_input('input nilai  rata-rata dari histogram sinyal ECG janin')

with col3 :
    histogram_median = st.text_input('input nilai Median dari histogram sinyal ECG janin')

with col3 :
    histogram_variance = st.text_input('input nilai Varians dari histogram sinyal ECG janin')	

with col3 :
    histogram_tendency = st.text_input('input nilai Kemiringan histogram sinyal ECG janin')	
    
fetalhealth_diagnosis = ''

if st.button('Prediksi Kesehatan Janin'):
    fetalhealth_prediction = fetalhealth_model.predict([[baseline_value,accelerations,fetal_movement,uterine_contractions,light_decelerations,severe_decelerations,prolongued_decelerations,abnormal_short_term_variability,mean_value_of_short_term_variability,percentage_of_time_with_abnormal_long_term_variability,mean_value_of_long_term_variability,histogram_width,histogram_min,histogram_max,histogram_number_of_peaks,histogram_number_of_zeroes,histogram_mode,histogram_mean,histogram_median,histogram_variance,histogram_tendency]])
    st.info("prediksi sukses✔️")

    if(fetalhealth_prediction[0]==1):
        fetalhealth_diagnosis = 'kesehatan janin Normal'

    elif (fetalhealth_prediction[0]==2):
        fetalhealth_diagnosis = 'kesehatan janin Suspect (Mencurigakan)'

    else :
        fetalhealth_diagnosis = 'kesehatan janin Pathological (Patologis)'

    st.success(fetalhealth_diagnosis)
