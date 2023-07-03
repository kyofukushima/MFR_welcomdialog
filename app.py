import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")
txt = st.sidebar.text_area('テキストエリア','子育てタウンアプリにレコメンド機能が加わりました！レコメンド機能はお子さんの年齢情報をもとにオススメの情報を表示します。')
content_css = 'background-color: rgb(142, 142, 142);margin: 0 auto;width: 500px;height: 500px;padding: 50px 70px;'
container_css = 'margin: 0 auto;background-color: #FFFFFF;width: 344px;height: auto;border-radius: 20px;'
dialog_css = 'margin: 0 auto;padding: 10px 21px;'
close_css = 'margin:0 auto;padding-bottom: 20px;text-align: center;color: #0062FF;'
css_text = """
<style>
.content {
    background-color: rgb(142, 142, 142);
    margin: 0 auto;
    width: 500px;
    height: 500px;
    padding: 50px 70px;
}
.container {
    margin: 0 auto;
    background-color: #FFFFFF;
    width: 344px;
    height: auto;
    border-radius: 20px;
    
}
.dialog {
    margin: 0 auto;
    padding: 10px 21px;
}
.close {
    margin:0 auto ;
    padding-bottom: 20px;
    text-align: center;
    color: #0062FF;
}
</style>
"""
html_text = f"""
    <div style='{content_css}'>
    <div style='{container_css}'>
        <img src="./app/static/dialog1.png" alt="">
        <p style='{dialog_css}'>{txt}</p>
        <p style='{close_css}'>閉じる</p>
        
    </div><!-- ./container -->
    </div><!-- ./content -->
    
"""
outputhtml = str(css_text + html_text)
st.markdown(html_text, unsafe_allow_html=True)