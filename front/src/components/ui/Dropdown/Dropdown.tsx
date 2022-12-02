import { Dispatch, SetStateAction } from 'react'

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
	return (
		<>
			<p className={styles.inputTitle}>{inputTitle}</p>
			<label className={styles.dropdown_label}>
				<select
					value={selectedOption}
					onChange={(e) => setSelectedOption(e.target.value)}
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
