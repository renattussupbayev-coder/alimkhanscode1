import streamlit as st
import random

st.set_page_config(page_title="Honey Badger Pacman", layout="centered")

# -----------------------------
# НАСТРОЙКА ИГРЫ
# -----------------------------

WIDTH = 10
HEIGHT = 10

# -----------------------------
# ИНИЦИАЛИЗАЦИЯ
# -----------------------------
if "x" not in st.session_state:
    st.session_state.x = 5
    st.session_state.y = 5
    st.session_state.score = 0
    st.session_state.food = [(random.randint(0,9), random.randint(0,9)) for _ in range(10)]

# -----------------------------
# ДВИЖЕНИЕ
# -----------------------------
def move(dx, dy):
    st.session_state.x = max(0, min(WIDTH-1, st.session_state.x + dx))
    st.session_state.y = max(0, min(HEIGHT-1, st.session_state.y + dy))

    # проверка еды
    pos = (st.session_state.x, st.session_state.y)
    if pos in st.session_state.food:
        st.session_state.food.remove(pos)
        st.session_state.score += 1

# -----------------------------
# UI
# -----------------------------
st.title("🦡 Honey Badger Pacman")

st.write("Score:", st.session_state.score)

# поле
for y in range(HEIGHT):
    row = ""
    for x in range(WIDTH):
        if x == st.session_state.x and y == st.session_state.y:
            row += "🦡 "
        elif (x, y) in st.session_state.food:
            row += "🍯 "
        else:
            row += "⬛ "
    st.text(row)

# -----------------------------
# КНОПКИ УПРАВЛЕНИЯ
# -----------------------------
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("⬆️"):
        move(0, -1)

with col1:
    if st.button("⬅️"):
        move(-1, 0)

with col3:
    if st.button("➡️"):
        move(1, 0)

if st.button("⬇️"):
    move(0, 1)

st.button("🔄 Restart")
if st.session_state.get("restart"):
    st.session_state.x = 5
    st.session_state.y = 5
    st.session_state.score = 0
