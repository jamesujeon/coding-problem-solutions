# 문제 링크: https://www.acmicpc.net/problem/9654

shipNames = ['N2 Bomber', 'J-Type 327', 'NX Cruiser', 'N1 Starfighter', 'Royal Cruiser']
classes = ['Heavy Fighter', 'Light Combat', 'Medium Fighter', 'Medium Fighter', 'Light Combat']
deployments = ['Limited', 'Unlimited', 'Limited', 'Unlimited', 'Limited']
services = [21, 1, 18, 25, 4]

print(f"{'SHIP NAME':<15}{'CLASS':<15}{'DEPLOYMENT':<11}{'IN SERVICE':<10}")
for i in range(5):
    print(f"{shipNames[i]:<15}{classes[i]:<15}{deployments[i]:<11}{services[i]:<10}")
