# import streamlit as st
# import json

# def main():
#     st.title("Video Captioning Demo【2022-07-01】")
#     # if "count" not in st.session_state: # (C)
#     #     st.session_state.count = 0 # (A)

#     # increment = st.button("Increment") # (B)
#     # if increment:
#     #     st.session_state.count += 1 # (A)

#     # st.write("Count = ", st.session_state.count) # (A)

#     video_id = st.selectbox(
#         'Video Captions',
#         (
#             'video7010',
#             'video7011',
#             'video7012',
#             'video7013',
#             'video7014',
#             'video7015',
#             'video7016',
#             'video7017',
#             'video7018',
#             'video7019',
#             'video7020',
#             'video7021',
#             'video7022',
#             'video7023',
#             'video7024',
#             'video7025',
#         )
#     )

#     st.write('Yu selected:', video_id)


#     results = json.load(open("results/S2VTAttModel.json"))
#     st.write('Generated caption :', results["predictions"][video_id][0]["caption"])
#     # st.write('Generated caption :', results["predictions"][video_id]["caption"])

#     if video_id :
#         video_file = open('test_videos/' + video_id + '.mp4', 'rb')
#         video_bytes = video_file.read()

#     st.video(video_bytes)

#     # if "video_id" not in st.session_state: # (C)
#     #     print(st.session_state.count)

# if __name__ == "__main__":
#     main()

import streamlit as st
import json
import pandas as pd
import numpy as np
import matplotlib

def main():
    epoch_list = [0, 50, 100, 150, 200, 300, 400, 500, 750, 1000, 1500, 2000, 3000,]
    st.title("Seminar 07/01")

    col1, col2 = st.columns(2)

    with col1:
        # Select Video
        st.header("Select Video")

    with col2:
        video_id = st.selectbox(
            '',
            ('video7013', 'video7014', 'video7015', 'video7016', 'video8000')
        )

    # Play Video
    if video_id :
        video_file = open('test_videos/' + video_id + '.mp4', 'rb')
        video_bytes = video_file.read()

    st.video(video_bytes)

    # Select Epoch
    st.header("Select Epoch")
    epoch = st.select_slider('', options=epoch_list)

    # Get Results from json
    results = json.load(open("results/model_" + str(epoch) + ".json"))
    st.subheader(results["predictions"][video_id][0]["caption"])

    df1 = pd.DataFrame(
        data = list(results["scores"].values()),
        index = ["BLEU_1", "BLEU_2", "BLEU_3", "BLEU_4", "METEOR", "ROUGE_L", "CIDEr"],
        columns= ["Score"]
    )
    st.table(df1)

    # Show Captions at each epoch
    st.header("Generated Caption")
    sentence_list = []
    score_list = []
    for e in epoch_list :
        j = json.load(open("results/model_" + str(e) + ".json"))
        sentence = j["predictions"][video_id][0]["caption"]
        sentence_list.append(sentence)
        score = list(j["scores"].values())
        score_list.append(score)

    df2 = pd.DataFrame(
        data = sentence_list,
        index = epoch_list,
        columns = ["Generated Caption"]
    )
    st.table(df2)

    # Show Score List
    st.header("Score")

    df3 = pd.DataFrame(
        data = score_list,
        index = epoch_list,
        columns = ["BLEU_1", "BLEU_2", "BLEU_3", "BLEU_4", "METEOR", "ROUGE_L", "CIDEr"]
    ).style.background_gradient(axis=0)
    st.table(df3)

    # st.header("Detail")

    # chart_data = pd.DataFrame(
    #     pd.read_csv("results/run-20220624-tag-TRAIN_LOSS.csv"),
    #     columns=['Train Loss']
    # )

    # st.line_chart(chart_data)

if __name__ == "__main__":
    main()