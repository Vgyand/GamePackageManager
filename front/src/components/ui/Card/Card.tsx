import { useState } from 'react'

import { useAppDispatch, useAppSelector } from 'hooks/hooks'

import { ICard } from 'shared/card'

import download from 'assets/icons/download.png'
import like from 'assets/icons/heart.svg'

import { onLiked } from 'store/likedSlice'
import { useDownloadPackMutation, useLikePackMutation } from 'store/packsApi'

import styles from './Card.module.scss'

const Card = ({
	id,
	name,
	downloadCount,
	likesCount,
	color,
	refetch,
}: ICard) => {
	const flag = useAppSelector((state) => state.like[id]?.flag)
	const [likeApi] = useLikePackMutation()
	const [downloadApi] = useDownloadPackMutation()
	const [likes, setLikes] = useState(likesCount)
	const [downloads, setDownloads] = useState(downloadCount)
	const dispatch = useAppDispatch()
	const likeHandler = async () => {
		await likeApi({ id })
		setLikes(+likes + 1)
		dispatch(
			onLiked({
				id: +id,
				flag: true,
				value: +likes + 1,
			})
		)

		refetch()
	}

	const downloadHandler = () => {
		setDownloads(+downloads + 1)
		downloadApi({ id })
		refetch()
	}

	return (
		<div className={styles.card} style={{ backgroundColor: color }}>
			<div className={styles.card_info} style={{ backgroundColor: color }}>
				name desc
			</div>
			<h2 className={styles.card_title}>{name}</h2>
			<div className={styles.card_buttons}>
				{flag ? (
					<button disabled={flag} onClick={likeHandler}>
						<div className={styles.card_button}>
							<img src={like} alt="heart" /> : {likes}
						</div>
					</button>
				) : (
					<button onClick={likeHandler}>
						<div className={styles.card_button}>
							<img src={like} alt="heart" /> : {likes}
						</div>
					</button>
				)}

				<button onClick={downloadHandler}>
					<div className={styles.card_button}>
						<img src={download} alt="heart" /> :{downloads}
					</div>
				</button>
			</div>
		</div>
	)
}

export default Card
