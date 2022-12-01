export const EmailValidationReg = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i

export const cardsOnPage = 25

export const sort: { value: string; label: string }[] = [
	{ value: '', label: '' },
	{ value: 'date', label: 'По дате создания' },
	{ value: 'like', label: 'По кол-ву лайков' },
	{ value: 'download', label: 'По кол-ву скачиваний' },
]
