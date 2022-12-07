import styles from './Pagination.module.scss'

const Pagination = ({
	postsPerPage,
	totalPosts,
	paginate,
	currentPage,
}: any) => {
	const pageNumbers: Array<number> = []
	for (let i = 1; i <= Math.ceil(totalPosts / postsPerPage); i++) {
		pageNumbers.push(i)
	}

	return (
		<ul className={styles.pagination}>
			{pageNumbers.map((number: number) => (
				<li
					key={number}
					className={
						(currentPage === number ? `${styles.active} ` : '') +
						styles.controls
					}
				>
					<a
						onClick={(event: React.MouseEvent<HTMLAnchorElement, MouseEvent>) =>
							paginate(number, event)
						}
					>
						{number}
					</a>
				</li>
			))}
		</ul>
	)
}

export default Pagination
