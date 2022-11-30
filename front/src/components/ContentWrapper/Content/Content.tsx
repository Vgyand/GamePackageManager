import randomColor from 'randomcolor'

import Card from 'components/ui/Card/Card'

import { useGetAllPacksQuery } from 'store/packsApi'

import styles from './Content.module.scss'

const Content = () => {
	const { data } = useGetAllPacksQuery('')
	return (
		<div className={styles.content}>
			<Card
				name="Packname"
				likesCount={2}
				downloadCount={4}
				color={randomColor()}
			/>
			<Card
				name="Packname"
				likesCount={2}
				downloadCount={4}
				color={randomColor()}
			/>
			<Card
				name="Packname"
				likesCount={2}
				downloadCount={4}
				color={randomColor()}
			/>
		</div>
	)
}

export default Content
