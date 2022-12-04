import close from 'assets/icons/close.png'

import styles from './AdminTableItem.module.scss'

const AdminTableItem = ({ id, name, downloadCount, likeCount }: any) => {
	return (
		<div>
			<div
				key={id}
				className={styles.pack_table}
				style={{
					backgroundColor: `${id % 2 == 0 ? 'grey' : 'white'}`,
				}}
			>
				<div>id: {id}</div>
				<div>name: {name}</div>
				<div>download count: {downloadCount}</div>
				<div>likes: {likeCount}</div>
				<button>
					<img src={close} alt="delete" className={styles.pack_table__img} />
				</button>
			</div>
		</div>
	)
}

export default AdminTableItem
