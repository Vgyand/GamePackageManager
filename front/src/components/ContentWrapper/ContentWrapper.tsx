import { useState } from 'react'

import Pagination from 'components/Pagination/Pagination'

import { useAppSelector } from 'hooks/hooks'

import { useGetAllPacksQuery } from 'store/packsApi'

import Content from './Content/Content'

const ContentWrapper = () => {
	const filter = useAppSelector((state) => state.filter)

	const { data, isLoading, isError, refetch } = useGetAllPacksQuery(filter)

	const [currentPage, setCurrentPage] = useState(1)
	const [cardsPerPage] = useState(10)

	const indexOfLastCard = currentPage * cardsPerPage
	const indexOfFirdsCard = indexOfLastCard - cardsPerPage
	const cards = data?.slice(indexOfFirdsCard, indexOfLastCard)

	const paginate = (pageNumber: number) => {
		setCurrentPage(pageNumber)
	}

	if (isLoading) return <div>loading</div>
	console.log(cards)
	return (
		<>
			<Content
				data={cards}
				isLoading={isLoading}
				isError={isError}
				refetch={refetch}
			/>
			{data ? (
				<Pagination
					postsPerPage={cardsPerPage}
					totalPosts={data.length}
					paginate={paginate}
					currentPage={currentPage}
				/>
			) : (
				''
			)}
		</>
	)
}

export default ContentWrapper
