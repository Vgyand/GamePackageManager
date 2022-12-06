import React, { useState } from 'react'

import AdminPostForm from 'components/ui/AdminPostForm/AdminPostForm'
import AdminTableItem from 'components/ui/AdminTableItem/AdminTableItem'

import { useAppSelector } from 'hooks/hooks'

import { useGetAllPacksQuery } from 'store/packsApi'

import styles from './AdminTable.module.scss'

const AdminTable = () => {
	const [openForm, setOpenForm] = useState(false)
	const filter = useAppSelector((state) => state.filter)

	const { data = [], isLoading } = useGetAllPacksQuery(filter, {
		refetchOnMountOrArgChange: true,
	})
	console.log(data)
	return (
		<div>
			<div className={styles.content}>
				<button
					onClick={() => setOpenForm(!openForm)}
					className={styles.admin_btn}
				>
					{openForm ? 'close' : 'open'}
				</button>
				{openForm ? <AdminPostForm /> : ''}
				<table className={styles.admin_table}>
					<tr>
						<th>id</th>
						<th>name</th>
						<th>downloads</th>
						<th>likes</th>
					</tr>
					{isLoading ? (
						'load'
					) : (
						<>
							{data.map((pack: any, index: number) => (
								<AdminTableItem
									index={index}
									key={pack.id}
									id={pack.id}
									name={pack.name}
									likeCount={pack.like_count}
									downloadCount={pack.download_count}
								/>
							))}
						</>
					)}
				</table>
			</div>
		</div>
	)
}

export default AdminTable
