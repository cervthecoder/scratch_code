from sys import stdout as st





alphabet_morse = {"A": ".-",
                  "B": "-...",
                  "C": "-.-.",
                  "D": "-..",
                  "E": ".",
                  "F": "..-.",
                  "G": "--.",
                  "H": "....",
                  "CH": "----",
                  "I": "..",
                  "J": ".---",
                  "K": "-.-",
                  "L": ".-..",
                  "M": "--",
                  "N": "-.",
                  "O": "---",
                  "P": ".--.",
                  "Q": "--.-",
                  "R": ".-.",
                  "S": "...",
                  "T": "-",
                  "U": "..-",
                  "V": "...-",
                  "W": ".--",
                  "X": "-..-",
                  "Y": "-.--",
                  "Z": "--..",
                  " ": " "}

morse_alphabet = {".-": "A",
                  "-...": "B",
                  "-.-.": "C",
                  "-..": "D",
                  ".": "E",
                  "..-.": "F",
                  "--.": "G",
                  "....": "H",
                  "----": "CH",
                  "..": "I",
                  ".---": "J",
                  "-.-": "K",
                  ".-..": "L",
                  "--": "M",
                  "-.": "N",
                  "---": "O",
                  ".--.": "P",
                  "--.-": "Q",
                  ".-.": "R",
                  "...": "S",
                  "-": "T",
                  "..-": "U",
                  "...-": "V",
                  ".--": "W",
                  "-..-": "X",
                  "-.--": "Y",
                  "--..": "Z",
                  " ": " "}

choice = input("1. alphabet -> morse\n2.morse -> alphabet\n: ")

if choice == "1":
    a_text = input("Enter text with spaces and lower characters: ")
    for char in a_text.upper():
        st.write(alphabet_morse[char] + "| ")


elif choice == "2":
    m_text = input("Enter morse: ")
    m_text_2 = m_text.split("| ")
    print(m_text_2)
    for char_1 in m_text_2:
        st.write(morse_alphabet[char_1])







