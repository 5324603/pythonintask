# ������ 4. ������� 49
# �������� ���������, ������� ������� ���, ��� ������� ���������� ����-��������� ���������. # ������������� ���������� ������� ������� ��������� ��������� ��������, ����� ��������, ���� # �������� � ������ (���� ������� ����), ��������� ������� �� ������ ������ (��� ������ # ������). ��� �������� ���� ����������� ������ ��������� ������������ ����������. ����� ������ # ���������� ��������� ������ ���������� ���� ������������ ������ Enter ��� ������.

# Ametova M. M.
# 31.03.2016


name = "����-��������� ���������"
famousName = "����"
interests = ["��������", "������������ �������", "������"]
birthPlace = "�������"
day = 0
month = 1
year = 2
daysInYear = 365
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
birthday = [27, 4, 1878]
deathday = [15, 7, 1954]

def getAge(birthDate, deathDate):
    if birthDate[month] == deathDate[month]:
        if birthDate[day] >= deathDate[day]:
            return deathDate[year] - birthDate[year] - 1
    if birthDate[month] > deathDate[month]:
        return deathDate[year] - birthDate[year] - 1
    return deathDate[year] - birthDate[year]
    
def printDate(date):
    dateStr = ''
    if date[day] < 10:
        dateStr += '0'
    dateStr += str(date[day]) + '.'
    if date[month] < 10:
        dateStr += '0'
    dateStr += str(date[month]) + '.' + str(date[year])
    print(dateStr)

print(name, ", ����� ���������� ��� ", famousName, sep = '', end = ".\n\n")
print ("��������\t:", end = ' ')
i = 0
for interest in interests:
    if (i < interests.__len__() - 1):
        print (interest, end = ", ")
        i += 1
    else:
        print (interest, end = ".\n")
print("���� ��������\t:", end = ' ')
printDate(birthday)
print("���� ������\t:", end = ' ')
printDate(deathday)
print("������� �� ������ ������:", getAge(birthday, deathday), "���")
input("\n������� Enter ��� ������.")