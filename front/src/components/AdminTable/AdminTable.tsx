import React from 'react'

import close from 'assets/icons/close.png'

import { useGetAllPacksQuery } from 'store/packsApi'

import styles from './AdminTable.module.scss'

const AdminTable = () => {
	const { data = [], isLoading } = useGetAllPacksQuery('')
	console.log(data)
	return (
		<div>
			<div className={styles.content}>
				{isLoading ? (
					'load'
				) : (
					<>
						{data.map((pack: any) => (
							<div
								key={pack.id}
								className={styles.pack_table}
								style={{
									backgroundColor: `${pack.id % 2 == 0 ? 'grey' : 'white'}`,
								}}
							>
								<div>id: {pack.id}</div>
								<div>name: {pack.name}</div>
								<div>download count: {pack.download_count}</div>
								<div>likes: {pack.like_count}</div>
								<button>
									<img
										src={close}
										alt="delete"
										className={styles.pack_table__img}
									/>
								</button>
							</div>
						))}
					</>
				)}
			</div>
		</div>
	)
}

export default AdminTable
