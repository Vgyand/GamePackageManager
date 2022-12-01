import { Link } from 'react-router-dom'

import styles from './IconLink.module.scss'

const IconLink = ({ url, img }: any) => {
	return (
		<div className={styles.nav_icon}>
			<Link to={url}>
				<img src={img} alt="icon" className={styles.nav_icon__img} />
			</Link>
		</div>
	)
}

export default IconLink
