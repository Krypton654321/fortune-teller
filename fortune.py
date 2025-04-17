# fortune.py - Version 1.0

def main():
    print("🔮 Welcome to Harshit Chauhan's Fortune Teller (21JE0388) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Harshit! Keep smiling. ✨")
    elif mood == "sad":
        print("💧 Your fortune: Storms don't last forever. Better days are coming. 💧")
    elif mood == "neutral":
        print("🌤️ Your fortune: A surprise will brighten your day soon. 🌤️")
    else:
        print("🤔 Sorry, I can't predict that mood yet. Try happy/sad/neutral.")

if __name__ == "__main__":
    main()
