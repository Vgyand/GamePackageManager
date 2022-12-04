export const EmailValidationReg = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i

export const cardsOnPage = 25

export const sort: { value: string; label: string }[] = [
	{ value: '', label: '' },
	{ value: 'likes_dec', label: 'По кол-ву лайков dec' },
	{ value: 'likes_inc', label: 'По дате создания inc' },
	{ value: 'downloads_dec', label: 'По кол-ву скачиваний dec' },
	{ value: 'downloads_inc', label: 'По кол-ву скачиваний inc' },
	{ value: 'weight_dec', label: 'По весу dec' },
	{ value: 'weight_inc', label: 'По весу inc' },
]
