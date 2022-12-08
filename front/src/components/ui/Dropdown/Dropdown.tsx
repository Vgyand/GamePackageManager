import { Dispatch, SetStateAction } from 'react'

import { useAppDispatch, useAppSelector } from 'hooks/hooks'

import { onFilterSelectChange } from 'store/filterSlice'
import { useGetAllPacksQuery } from 'store/packsApi'

import styles from './Dropdown.module.scss'

export interface DropdownTypes {
	options: { value: string; label: string }[]
	selectedOption: string
	setSelectedOption: Dispatch<SetStateAction<string>>
	inputTitle: string
}

const Dropdown = ({
	options,
	selectedOption,
	setSelectedOption,
	inputTitle,
}: DropdownTypes) => {
	const filter = useAppSelector((state) => state.filter)
	const { refetch } = useGetAllPacksQuery(filter)
	const dispatch = useAppDispatch()
	const selectOptionHandler = (event: any) => {
		setSelectedOption(event.target.value)
		const obj = {
			val: event.target.value.split('_')[0],
			mod: event.target.value.split('_')[1],
		}
		refetch()
		dispatch(onFilterSelectChange(obj))
	}
	return (
		<>
			<p className={styles.inputTitle}>{inputTitle}</p>
			<label className={styles.dropdown_label}>
				<select
					value={selectedOption}
					onChange={selectOptionHandler}
					className={styles.dropdown_select}
				>
					{options.map((o) => (
						<option key={o.value} value={o.value}>
							{o.label}
						</option>
					))}
				</select>
			</label>
		</>
	)
}

export default Dropdown
