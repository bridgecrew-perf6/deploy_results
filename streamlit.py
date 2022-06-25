import streamlit as st
import json

def main():
    st.title("Video Captioning Demo【2022-07-01】")
    # if "count" not in st.session_state: # (C)
    #     st.session_state.count = 0 # (A)

    # increment = st.button("Increment") # (B)
    # if increment:
    #     st.session_state.count += 1 # (A)

    # st.write("Count = ", st.session_state.count) # (A)

    video_id = st.selectbox(
        'Video Captions',
        ('video7013', 'video7014', 'video7015', 'video7016', 'video8000')
    )

    st.write('Yu selected:', video_id)


    results = json.load(open("results/S2VTAttModel.json"))
    st.write('Generated caption :', results["predictions"][video_id][0]["caption"])
    # st.write('Generated caption :', results["predictions"][video_id]["caption"])

    if video_id :
        video_file = open('data/test_videos/TestVideo/' + video_id + '.mp4', 'rb')
        video_bytes = video_file.read()

    st.video(video_bytes)

    # if "video_id" not in st.session_state: # (C)
    #     print(st.session_state.count)

if __name__ == "__main__":
    main()