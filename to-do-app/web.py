import streamlit as st
import functions

todos = functions.get_todos("to-do-app/todos.txt")


def add_todo():
    todo = st.session_state["new-todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, "to-do-app/todos.txt")


st.title("My Todo App")
st.subheader("This is my todo app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, "to-do-app/todos.txt")
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Add a new Todo", key="new-todo", on_change=add_todo)


st.session_state