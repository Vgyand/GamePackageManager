import randomColor from 'randomcolor'

import Card from 'components/ui/Card/Card'

import { useGetAllPacksQuery } from 'store/packsApi'

import styles from './Content.module.scss'

const Content = () => {
	const { data = [], isLoading, isError } = useGetAllPacksQuery('')

	if (isError) return <div>An error has occurred!</div>
	if (isLoading) return <div>skelet</div>
	Object.keys(data).map((item: any) => console.log(data[item]))

	return (
		<div className={styles.content}>
			{Object.keys(data).map((pack: any, index: number) => (
				<Card
					key={index}
					name={data[pack].name}
					likesCount={data[pack].like_count}
					downloadCount={data[pack].download_count}
					color={randomColor()}
				/>
			))}
		</div>
	)
}

export default Content
