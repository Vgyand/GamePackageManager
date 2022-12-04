import React from 'react'

import AdminTableItem from 'components/ui/AdminTableItem/AdminTableItem'

import { useAppSelector } from 'hooks/hooks'

import { useGetAllPacksQuery } from 'store/packsApi'

import styles from './AdminTable.module.scss'

const AdminTable = () => {
	const filter = useAppSelector((state) => state.filter)
	const { data = [], isLoading } = useGetAllPacksQuery(filter)
	console.log(data)
	return (
		<div>
			<div className={styles.content}>
				<button>post a new pack</button>
				{isLoading ? (
					'load'
				) : (
					<>
						{data.map((pack: any) => (
							<AdminTableItem
								key={pack.id}
								id={pack.id}
								name={pack.name}
								likeCount={pack.like_count}
								downloadCount={pack.download_count}
							/>
						))}
					</>
				)}
			</div>
		</div>
	)
}

export default AdminTable
