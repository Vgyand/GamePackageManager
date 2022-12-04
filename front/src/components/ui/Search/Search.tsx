import { useAppDispatch, useAppSelector } from 'hooks/hooks'

import { onFilterSearchChange } from 'store/filterSlice'

import styles from './Search.module.scss'

const Search = () => {
	const search = useAppSelector((state) => state.filter.search)
	const dispatch = useAppDispatch()

	const onSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		dispatch(onFilterSearchChange(event.target.value))
	}

	return (
		<form className={styles.input}>
			<input
				type="text"
				id="message"
				name="message"
				onChange={onSearchChange}
				placeholder={'Search'}
				value={search}
			/>
		</form>
	)
}

export default Search
