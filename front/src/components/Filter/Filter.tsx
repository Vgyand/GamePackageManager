import { useState } from 'react'

import Search from 'components/ui/Search/Search'

import filter from 'assets/icons/filter.png'

import styles from './Filter.module.scss'

const Filter = () => {
	const [open, setOpen] = useState(false)
	return (
		<div>
			<div
				className={styles.filter}
				style={{ display: `${open ? 'block' : 'none'}` }}
			>
				<Search />
				selectors
			</div>
			<div className={styles.filterIcon} onClick={() => setOpen(!open)}>
				<img src={filter} alt="filter" />
			</div>
		</div>
	)
}

export default Filter
