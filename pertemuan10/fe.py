import stack
import streamlit as st

#membuat visualisasi stack dengan streamlit 
st.set_page_config(page_title="📊Stack Visualizer", layout="wide")
# judul aplikasi
st.title("Stack Visualizer")

def display_stack():
    temp = st.session_state.stack.head
    while temp:
        st.write(temp.data)
        temp = temp.next
    st.write("None")

# inisialisasi stack
if 'stack' not in st.session_state:
    st.session_state.stack = stack.Stack()

#input data
with st.form("input_form"):
    data = st.text_input("masukan data")
    submit = st.form_submit_button("tambah ke stack")

    if submit and data:
        st.session_state.stack.push(data)
        st.rerun()
    
# tampilkan stack
st.subheader("stack visualization")
# tombol pop
if st.button("pop"):
    st.session_state.stack.pop()
    st.rerun()

# tampilkan stack teratas
st.subheader("apakah teratas?")
st.write(st.session_state.stack.peek())

#tampilan apakah stack kosong
st.subheader("apakah Stack kosong?")
st.write(st.session_state.stack.isEmpty())

# menampilkan seluruh isi stack
st.subheader("seluruh isi stack")
st.write(display_stack())