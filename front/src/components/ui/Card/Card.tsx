import { ICard } from 'shared/card'

import download from 'assets/icons/download.png'
import likes from 'assets/icons/heart.svg'

import styles from './Card.module.scss'

const Card = ({ name, downloadCount, likesCount, color }: ICard) => {
	return (
		<div className={styles.card} style={{ backgroundColor: color }}>
			<h2 className={styles.card_title}>{name}</h2>
			<div className={styles.card_buttons}>
				<button>
					<div className={styles.card_button}>
						<img src={likes} alt="heart" /> :{' ' + likesCount}
					</div>
				</button>
				<button>
					<div className={styles.card_button}>
						<img src={download} alt="heart" /> :{' ' + downloadCount}
					</div>
				</button>
			</div>
		</div>
	)
}

export default Card
