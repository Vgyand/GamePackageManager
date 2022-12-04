import { useState } from 'react'

import Dropdown from 'components/ui/Dropdown/Dropdown'
import Search from 'components/ui/Search/Search'

import close from 'assets/icons/close.png'
import filterImg from 'assets/icons/filter.png'

import { sort } from 'config/consts'

import styles from './Filter.module.scss'

const Filter = () => {
	const [open, setOpen] = useState(false)
	const [filter, setFilter] = useState('')

	return (
		<div>
			<div className={styles.filter}>
				<Search />
				<Dropdown
					options={sort}
					selectedOption={filter}
					setSelectedOption={setFilter}
					inputTitle={'Select a filter'}
				/>
			</div>
			<div className={styles.filterIcon} onClick={() => setOpen(!open)}>
				{open ? (
					<img src={close} alt="close" />
				) : (
					<img src={filterImg} alt="filter" />
				)}
			</div>
			<div
				className={styles.filterAdapt}
				style={{ display: `${open ? 'block' : 'none'}` }}
			>
				<Search />
				<Dropdown
					options={sort}
					selectedOption={filter}
					setSelectedOption={setFilter}
					inputTitle={'Select a filter'}
				/>
			</div>
		</div>
	)
}

export default Filter
