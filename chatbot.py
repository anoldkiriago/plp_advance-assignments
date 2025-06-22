# ------------------------------------------
# 👋 Hi there! This is my first chatbot project.
# It's a Crypto Advisor that helps you decide 
# whether to invest in certain cryptocurrencies.
# ------------------------------------------

# 🔸 Step 1: Some mock data (like a tiny database)
# Each crypto has 3 key things:
# - price_change (%)
# - energy_use (low/medium/high)
# - viability (how promising the project is)

cryptos = {
    "Bitcoin": {
        "price_change": 5.4,
        "energy_use": "high",
        "viability": "stable"
    },
    "Ethereum": {
        "price_change": 3.1,
        "energy_use": "medium",
        "viability": "strong"
    },
    "Dogecoin": {
        "price_change": -2.3,
        "energy_use": "low",
        "viability": "weak"
    }
}

# 🔸 Step 2: A function to "analyze" the crypto and give advice
# It looks up the coin you typed, checks its data, and builds a response.

def analyze_crypto(name):
    # Capitalize name just in case someone types "bitcoin" in lowercase
    crypto = cryptos.get(name.title())
    
    if not crypto:
        return "❌ Oops! I don’t have any info on that coin."

    # 🔍 Profitability check
    if crypto["price_change"] > 0:
        profit_msg = f"{name.title()} is currently profitable with a {crypto['price_change']}% price increase. 📈"
    else:
        profit_msg = f"{name.title()} has dropped by {crypto['price_change']}%. Might not be the best time. 📉"

    # 🌱 Sustainability check
    if crypto["energy_use"] == "low" and crypto["viability"] in ["strong", "stable"]:
        sustain_msg = "👍 It's also considered eco-friendly and a promising project."
    elif crypto["energy_use"] == "high":
        sustain_msg = "⚠️ But it uses a lot of energy, so there are environmental concerns."
    else:
        sustain_msg = "🤔 It's okay, but not the most sustainable choice."

    # Combine both answers
    return f"{profit_msg} {sustain_msg}"

# 🔸 Step 3: The chatbot loop
# This is where the "chat" happens.

print("🤖 Hello! I’m your Crypto Advisor Bot.")
print("You can ask me about Bitcoin, Ethereum, or Dogecoin.")
print("Type 'exit' to end the chat.\n")

while True:
    # Get user input
    user_input = input("🧠 You: ").strip()
    
    # Exit the chatbot
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Okay, bye! Invest wisely! 💰")
        break

    # Show the bot's response
    response = analyze_crypto(user_input)
    print(f"🤖 Bot: {response}\n")
