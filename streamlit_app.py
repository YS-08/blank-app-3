# streamlit_app.py

# ... (기존 코드 생략)

def main():
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
                st.rerun() # <-- 이 부분을 st.rerun()으로 수정
    else:
        # 결과 화면
        st.header("✨ 당신에게 어울리는 간식은...")
        
        user_answers = {
            'q1': st.session_state.q1,
            'q2': st.session_state.q2,
            'q3': st.session_state.q3,
            'q4': st.session_state.q4,
            'q5': st.session_state.q5,
            'q6': st.session_state.q6,
            'q7': st.session_state.q7
        }
        
        recommended_snack, place = get_recommendation(user_answers)
        
        st.success(f"**{recommended_snack}** 입니다!")
        st.info(f"📍 **판매처:** {place}")
        
        # 다시 시작 버튼
        if st.button("다시 추천받기"):
            st.session_state.submitted = False
            st.rerun() # <-- 이 부분을 st.rerun()으로 수정

# 앱 실행
if __name__ == "__main__":
    main()