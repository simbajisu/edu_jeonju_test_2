import streamlit as st

# 상태 저장
if "num1" not in st.session_state:
    st.session_state.num1 = ""
if "num2" not in st.session_state:
    st.session_state.num2 = ""
if "operator" not in st.session_state:
    st.session_state.operator = ""
if "result" not in st.session_state:
    st.session_state.result = None

# 숫자 버튼 함수
def append_number(n):
    if not st.session_state.operator:  # 연산자가 선택되지 않았을 때 첫 번째 숫자 입력
        st.session_state.num1 += str(n)
    else:  # 연산자가 선택된 후 두 번째 숫자 입력
        st.session_state.num2 += str(n)

# 연산자 버튼 함수
def set_operator(op):
    if st.session_state.num1:  # 첫 번째 숫자가 입력된 상태에서만 연산자 선택 가능
        st.session_state.operator = op

# 계산 함수
def calculate():
    try:
        num1 = float(st.session_state.num1)
        num2 = float(st.session_state.num2)
        if st.session_state.operator == "더하기":
            st.session_state.result = num1 + num2
        elif st.session_state.operator == "빼기":
            st.session_state.result = num1 - num2
        elif st.session_state.operator == "곱하기":
            st.session_state.result = num1 * num2
        elif st.session_state.operator == "나누기":
            st.session_state.result = num1 / num2 if num2 != 0 else "오류: 0으로 나눌 수 없습니다."
    except ValueError:
        st.session_state.result = "오류: 잘못된 입력입니다."

# UI 구성
st.title("🦁 크아아앙 심바의 계산기 🦁")

# 숫자 버튼
n1, n2, n3 = st.columns(3)
if n1.button("1", use_container_width=True): append_number(1)
if n2.button("2", use_container_width=True): append_number(2)
if n3.button("3", use_container_width=True): append_number(3)

n4, n5, n6 = st.columns(3)
if n4.button("4", use_container_width=True): append_number(4)
if n5.button("5", use_container_width=True): append_number(5)
if n6.button("6", use_container_width=True): append_number(6)

n7, n8, n9 = st.columns(3)
if n7.button("7", use_container_width=True): append_number(7)
if n8.button("8", use_container_width=True): append_number(8)
if n9.button("9", use_container_width=True): append_number(9)

n0 = st.columns(1)[0]
if n0.button("0", use_container_width=True): append_number(0)

# 연산자 버튼
n10, n11, n12, n13 = st.columns(4)
if n10.button("더하기", use_container_width=True): set_operator("더하기")
if n11.button("빼기", use_container_width=True): set_operator("빼기")
if n12.button("곱하기", use_container_width=True): set_operator("곱하기")
if n13.button("나누기", use_container_width=True): set_operator("나누기")

# 계산 버튼
if st.button("계산하기", use_container_width=True):
    calculate()

# 입력 및 결과 표시
st.write("**입력한 숫자 및 연산자:**")
st.write(f"첫 번째 숫자: {st.session_state.num1}")
st.write(f"연산자: {st.session_state.operator}")
st.write(f"두 번째 숫자: {st.session_state.num2}")

if st.session_state.result is not None:
    st.write("**결과:**")
    st.write(st.session_state.result)
