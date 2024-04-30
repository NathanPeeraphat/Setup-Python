quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']
max_quests = 5
if 'ไล่ศัตรูพืช' in quests:
    print('u can go in!')

if len(quests) < max_quests:
    quests.append('จับปลาดุก')

for i in range(len(quests)):
    print(str(i + 1) + '. ' + quests[i])
