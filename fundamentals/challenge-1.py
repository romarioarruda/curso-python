# how much in
wage = 6800 + 600

# How much out
maria = 1800 + 370
light = 500
condominium = 150
food = 600
credit_card = 600 + 770 + 600
budget = maria + light + condominium + food + credit_card

# free amount
liquid_wage = wage - budget

# budget percent
percent = budget / wage * 100

print("budget total: ", budget)
print("budget percent: ", percent, "%")
print("Liquid wage: ", liquid_wage)