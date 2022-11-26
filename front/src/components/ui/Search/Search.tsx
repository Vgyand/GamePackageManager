import { useState } from 'react'

import Button from '../Button/Button'

import styles from './Search.module.scss'

const Search = () => {
	const [search, setSearch] = useState('')

	const onSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setSearch(event.target.value)
	}

	return (
		<div className={styles.input}>
			<input
				type="text"
				id="message"
				name="message"
				onChange={onSearchChange}
				value={search}
				placeholder={'Search'}
			/>
			<Button text={'Apply'} handler={() => console.log('jija')} />
		</div>
	)
}

export default Search
