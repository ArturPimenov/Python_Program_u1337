# Все карты из обычной колоды.
from classes import *

standard_cards = []

# Девочки

standard_cards += [
	GirlCard('Полина Бурилло', 54, 119-54),
	GirlCard('Дарья Кравченко', 90, 119-90),
	GirlCard('Анастасия Никитина', 97, 119-97),
	GirlCard('Светлана Рыжкова', 89, 119-89),
	GirlCard('Ксения Ципилева', 76, 119-76)
]

# Мальчики

standard_cards += [
	BoyCard('Артем Артамонов', 56, 119-56),
	BoyCard('Никита Белов', 87, 119-87),
	BoyCard('Артем Воронов', 62, 119-62),
	BoyCard('Даниел Грэждиеру', 90, 119-90),
	BoyCard('Алексей Дыбов', 62, 119-62),
	BoyCard('Дык Фам Минь', 55, 119-55),
	BoyCard('Влад Заикин', 72, 119-72),
	BoyCard('Павел Ивин', 52, 119-52),
	BoyCard('Павел Коротнев', 84, 119-84),
	BoyCard('Александр Кочешков', 42, 119-42),
	BoyCard('Андрей Куликов', 87, 119-87),
	BoyCard('Вячеслав Локтистов', 75, 119-75),
	BoyCard('Игорь Макаров', 115, 119-115),
	BoyCard('Матвей Молчанов', 74, 119-74),
	BoyCard('Александр Пантелеев', 73, 119-73),
	BoyCard('Андрей Раевский', 8, 119-8),
	BoyCard('Алексей Сенников', 92, 119-92),
	BoyCard('Алексей Струнин', 39, 119-39),
	BoyCard('Александр Тихомиров', 94, 119-94)
]

# Преподы
standard_cards += [
	TeacherCard('Илья Апальков', 119, 119)
]

# Обычная колода содержит обычные карты.
standard_deck = Deck(standard_cards)

# Колоды игрока и противника — обычные колоды.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()