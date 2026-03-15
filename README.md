# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

My game's purpose is a game guesser. The bugs I found were the followng:
1) When I chose a guess that was smaller than the secret number, I expected the hint to say to go higher. Instead, the game told me the opposite of going lower even thought my guess was smaller than the secret number. 
2) When I hit the attempt limit and wanted to start a new game, I expected for there to be a new secret number and for my attempts to be reset. However, instead, the game did not let me enter a new guess, stating the same message prior which was "Game over. Start a new game to try again."
3) When I hit the attempt limit, I was only on attempt number 7. The game did not let me use up all attempts. Instead, it stopped me from entering anymore guesses, saying I used all my attempts.
4) When changing the difficulty mode, the secret number's potential range did not change to match the range of the mode selected. Rather, secret numbers being generated were in the range of 1 and 100.
The fixes I applied mainly involved using AI to redo internal game logic, like reseting other variables with the new game button trigger event so that functionality actually led to a new game instead of being unable to start a new game.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
[Screenshot](https://github.com/VicChen199/ai110-module1show-gameglitchinvestigator-starter/blob/main/Screenshot%202026-03-15%20at%206.08.53%E2%80%AFPM.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
