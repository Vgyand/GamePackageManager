import { useState } from 'react'

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
			/>
		</div>
	)
}

export default Search
