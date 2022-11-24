import ContentWrapper from 'components/ContentWrapper/ContentWrapper'
import Filter from 'components/Filter/Filter'
import Logo from 'components/Logo/Logo'

import styles from './MainPage.module.scss'

const MainPage = () => {
	return (
		<div className="mx-auto max-w-5xl container">
			<div className="grid grid-cols-12 mx-auto">
				<div className={styles.logo}>
					<Logo />
				</div>
				<div className={styles.content}>
					<ContentWrapper />
				</div>
				<div className={styles.filter}>
					<Filter />
				</div>
			</div>
		</div>
	)
}

export default MainPage
