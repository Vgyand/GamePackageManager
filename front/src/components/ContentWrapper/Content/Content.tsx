import randomColor from 'randomcolor'

import Card from 'components/ui/Card/Card'

import styles from './Content.module.scss'

const Content = () => {
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
