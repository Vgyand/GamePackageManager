import Card from 'components/ui/Card/Card'
import SkeletonLoader from 'components/ui/SkeletonLoader/SkeletonLoader'

import styles from './Content.module.scss'

const Content = ({ data, isError, refetch, isLoading }: any) => {
	if (isError) return <div>An error has occurred!</div>

	return (
		<div className={styles.content}>
			{isLoading ? (
				<SkeletonLoader />
			) : (
				<>
					{data.map((pack: any, index: number) => (
						<Card
							refetch={refetch}
							id={pack.id}
							key={index}
							name={pack.name}
							likesCount={pack.like_count}
							downloadCount={pack.download_count}
						/>
					))}
				</>
			)}
		</div>
	)
}

export default Content
