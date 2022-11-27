import { useState } from 'react'

import Search from 'components/ui/Search/Search'

import close from 'assets/icons/close.png'
import filter from 'assets/icons/filter.png'

import styles from './Filter.module.scss'

const Filter = () => {
	const [open, setOpen] = useState(false)

	return (
		<div>
			<div className={styles.filter}>
				<Search />
				selectors
			</div>
			<div className={styles.filterIcon} onClick={() => setOpen(!open)}>
				{open ? (
					<img src={close} alt="close" />
				) : (
					<img src={filter} alt="filter" />
				)}
			</div>
			<div
				className={styles.filterAdapt}
				style={{ display: `${open ? 'block' : 'none'}` }}
			>
				<Search />
				selectors
			</div>
		</div>
	)
}

export default Filter
