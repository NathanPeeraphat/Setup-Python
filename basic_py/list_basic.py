quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']
print(quests[1])
quests[1] = 'ขูดมะพร้าว'
print(quests)

quests.append('หอมแก้มแฟน')
print(quests)

quests.insert(1, 'ซักผ้า')
print(quests)

quests.remove('ไล่ศัตรูพืช')
print(quests)
