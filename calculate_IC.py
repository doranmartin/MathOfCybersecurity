alphabet = [chr(ord('a') + x) for x in range(26)]

dict = {x: 0 for x in alphabet}

text = 'rsoborgwuvrvviakorgjafskxmnxygaehitvjmolyenuojtykgignirzyqoeuelgnebvzmckninknikrymsboxejzhovyrtykpplyenpnswtgrwvzilclvodzlejzerkcleknirfxrokurefxqoikelgnebvzwaikfeztkujkhtykmdvgleikmsknetknifikuuvtgykgflvujaeswcjnsucjpofqpibkxhvurewuvskgrdrxheempijnnujzaiknxhvritkkvsdgxcyorguojfvxinklvehaintoiskniwreaerixurrpyxuebfaxmvgwuiorgknmszyelzzxlvjmfwkveezjrfsxhzyfukoxgvzwakzlejgqeknmnxciujkxhvordvdsftumntoheeii'

length = len(text)

for char in text:
    dict.update({char: dict.get(char) + 1})

print(dict)
print(length)
