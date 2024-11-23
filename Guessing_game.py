import streamlit as st
import random

def start_game():
    st.session_state['number_to_guess'] = random.randint(1, 100)
    st.session_state['attempts'] = 0
    st.session_state['GAME OVER :('] = False

if 'number_to_guess' not in st.session_state:
    start_game()

st.title("Guess the Number!")

guess = st.number_input("Enter your guess (between 1 and 100):", min_value=1, max_value=100)

if st.button("Submit Guess"):
    st.session_state['attempts'] += 1
    if guess < st.session_state['number_to_guess']:
        st.warning("You're guess is too low... Try again!")
    elif guess > st.session_state['number_to_guess']:
        st.warning("You're guess is too high... Try again!")
    else:
        st.success(f"Congratulations! You've guessed the number {st.session_state['number_to_guess']} in {st.session_state['attempts']} attempts!")
        st.session_state['game_over'] = True

if st.session_state.get('game_over', False):
    if st.button("Play Again"):
        start_game()

if not st.session_state.get('game_over', False):
    st.write(f"Attempts: {st.session_state['attempts']}")