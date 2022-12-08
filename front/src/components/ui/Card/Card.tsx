import { useState } from 'react'

import { useAppDispatch } from 'hooks/hooks'

import { ICard } from 'shared/card'

import download from 'assets/icons/download.png'
import like from 'assets/icons/heart.svg'

import { onLiked } from 'store/likedSlice'
import { useDownloadPackMutation, useLikePackMutation } from 'store/packsApi'

import styles from './Card.module.scss'

const Card = ({ id, name, downloadCount, likesCount, refetch }: ICard) => {
	const [likeApi] = useLikePackMutation()
	const [downloadApi] = useDownloadPackMutation()

	const likeHandler = async () => {
		likeApi({ id })
		refetch()
	}

	const downloadHandler = () => {
		downloadApi({ id })
		refetch()
	}

	return (
		<div className={styles.card}>
			<div className={styles.card_info}>name desc</div>
			<h2 className={styles.card_title}>{name}</h2>
			<div className={styles.card_buttons}>
				<button onClick={likeHandler}>
					<div className={styles.card_button}>
						<img src={like} alt="heart" /> : {likesCount}
					</div>
				</button>
				<button onClick={downloadHandler}>
					<div className={styles.card_button}>
						<img src={download} alt="heart" /> : {downloadCount}
					</div>
				</button>
			</div>
		</div>
	)
}

export default Card
