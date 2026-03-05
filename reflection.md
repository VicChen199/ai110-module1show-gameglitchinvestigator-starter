# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1) When I chose a guess that was smaller than the secret number, I expected the hint to say to go higher. Instead, the game told me the opposite of going lower even thought my guess was smaller than the secret number. 
2) When I hit the attempt limit and wanted to start a new game, I expected for there to be a new secret number and for my attempts to be reset. However, instead, the game did not let me enter a new guess, stating the same message prior which was "Game over. Start a new game to try again."
3) When I hit the attempt limit, I was only on attempt number 7. The game did not let me use up all attempts. Instead, it stopped me from entering anymore guesses, saying I used all my attempts.
4) When changing the difficulty mode, the secret number's potential range did not change to match the range of the mode selected. Rather, secret numbers being generated were in the range of 1 and 100.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
