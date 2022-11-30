import { useState } from 'react'

import Button from '../Button/Button'

import styles from './Search.module.scss'

const Search = () => {
	const [search, setSearch] = useState('')

	const onSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setSearch(event.target.value)
	}

	const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault()
		console.log('submit')
	}

	return (
		<form onSubmit={handleSubmit} className={styles.input}>
			<input
				type="text"
				id="message"
				name="message"
				onChange={onSearchChange}
				value={search}
				placeholder={'Search'}
			/>
			<Button text={'Apply'} handler={() => console.log('jij')} />
		</form>
	)
}

export default Search
