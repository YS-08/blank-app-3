# streamlit_app.py
import streamlit as st
import random

def get_recommendation(answers):
    """
    사용자의 답변을 기반으로 간식을 추천하고 판매처 정보를 반환하는 함수.
    
    :param answers: 사용자의 응답을 담고 있는 딕셔너리
    :return: 추천 간식(str), 판매처(str)
    """
    snacks = [
        {"name": "새우깡", "place": "편의점, 마트"},
        {"name": "초코파이", "place": "편의점, 마트"},
        {"name": "꼬북칩", "place": "편의점, 마트"},
        {"name": "마가렛트", "place": "편의점, 마트"},
        {"name": "칸쵸", "place": "편의점, 마트"},
        {"name": "빼빼로", "place": "편의점, 마트"},
        {"name": "홈런볼", "place": "편의점, 마트"},
        {"name": "버터와플", "place": "편의점, 마트"},
        {"name": "오징어집", "place": "편의점, 마트, 슈퍼"},
        {"name": "웨하스", "place": "편의점, 마트, 슈퍼"},
        {"name": "사탕 (츄파츕스)", "place": "편의점, 마트"},
        {"name": "젤리 (하리보)", "place": "편의점, 마트"},
        {"name": "감자깡", "place": "편의점, 마트"},
        {"name": "프링글스", "place": "편의점, 마트"}
    ]
    
    selected_snack = random.choice(snacks)
    return selected_snack["name"], selected_snack["place"]

def main():
    """
    Streamlit 앱의 메인 로직을 담고 있는 함수.
    """
    st.title("😋 오늘의 간식은?")
    
    # 세션 상태 초기화 (초기 화면 표시)
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if not st.session_state.submitted:
        # 사용자로부터 간식 취향을 묻는 폼
        with st.form(key='snack_form'):
            st.markdown("간식 취향에 맞는 항목을 선택해주세요!")
            
            st.session_state.q1 = st.radio("✅ **1. 지금 짠맛이 당기나요, 단맛이 당기나요?**", ('짠맛', '단맛'))
            st.session_state.q2 = st.radio("✅ **2. 바삭바삭한 과자가 좋나요, 부드러운 과자가 좋나요?**", ('바삭바삭', '부드러운'))
            st.session_state.q3 = st.radio("✅ **3. 입이 심심할 때 가볍게 먹을 수 있는 간식이 좋나요?**", ('네', '아니요'))
            st.session_state.q4 = st.radio("✅ **4. 손에 묻는 간식이 괜찮나요?**", ('네, 괜찮아요', '아니요, 묻는 건 싫어요'))
            st.session_state.q5 = st.radio("✅ **5. 양이 많아서 나눠 먹기 좋은 간식이 좋나요?**", ('네', '아니요'))
            st.session_state.q6 = st.radio("✅ **6. 봉지에 든 간식과 상자에 든 간식 중 어느 것을 선호하시나요?**", ('봉지', '상자'))
            st.session_state.q7 = st.radio("✅ **7. 초콜릿, 젤리, 사탕 중 하나를 고른다면?**", ('초콜릿', '젤리', '사탕'))

            # 제출 버튼
            submit_button = st.form_submit_button(label='결과 보기')
            
            # 제출 버튼 클릭 시 결과 화면으로 전환
            if submit_button:
                st.session_state.submitted = True
                st.rerun()
    else:
        # 결과 화면
        st.header("✨ 당신에게 어울리는 간식은...")
        
        user_answers = {
            'q1': st.session_state.q1,
            'q2': st.session_state.q2,
            'q3': st.session_state.q3,
            'q4': st.session_state