import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to improve productivity")

todos = functions.get_todos()

for index,todo in enumerate(todos):
    check_box = st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",placeholder="Add New todo", on_change=add_todo, key="new_todo")
#st.session_state

#print("Hello")