print("Zadanie 1")
shopping = {
    "piekarnia": ["chleb", "bułki", "pączek", "ptyś"],
    "warzywniak": ["marchew", "seler", "jabłka"]
}
for key, value in shopping.items():
    print(f"Idę do", key.capitalize(),
          "kupuję tu następujące rzeczy:", str(value).title())
print(f"W sumie kupuję", sum(len(i) for i in shopping.values()), "produktów")
print("'Martwa papuga' to najlepszy skecz grupy Monty Pythona")
print("'Hiszpańska inkwizycja' to najlepszy skecz grupy Monty Pythona")
