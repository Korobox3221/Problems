hard_lane = 0
mid_lane = 15
easy_lane = 0
BB,FALCONS = '35%','65%'
PARI,LIQUID = '60%','40%'
BB_ODDS = 2.26
FALCONS_ODDS = 1.64
PARI_ODDS = 1.52
LIQUID_ODDS = 2.46
balance = 4500
prob = float(input("Winning chance%: "))/100 + hard_lane/100+mid_lane/100+easy_lane/100
print(prob)
team_a_factor = float(input("Enter Team's odds: "))
bank_percent_a = ((prob * team_a_factor)-1)/ (team_a_factor-1)
print(f"Team A bet: {round(bank_percent_a*100)}%")
print(f"{round(balance*bank_percent_a)} rubles")
