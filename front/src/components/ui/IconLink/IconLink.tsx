import { Link } from 'react-router-dom'

import styles from './IconLink.module.scss'

interface Icon {
	url: string
	img: string
}

const IconLink = ({ url, img }: Icon) => {
	return (
		<div className={styles.nav_icon}>
			<Link to={url}>
				<img src={img} alt="icon" className={styles.nav_icon__img} />
			</Link>
		</div>
	)
}

export default IconLink
